from confighandler import ConfigHandler
from paho.mqtt.client import Client, CONNACK_ACCEPTED
from threading import Thread
from datetime import datetime
from time import sleep
from mqttsimdatagenerator import MqttSimDataGenerator
from uuid import uuid4

class MqttSimConfig:
    def __init__(self, path: str):
        self.__config = ConfigHandler(path)

    def put_topic(self, topic_config: dict, uuid: str = uuid4()) -> None:
        self.__config.put(f"topics.{uuid}", topic_config)
        return uuid

    def get_topic_data(self, topic_uuid: str) -> dict | None:
        return self.__config.get(f"topics.{topic_uuid}")

    def put_broker(self, host: str, port: int, username: str | None = None, password: str | None = None) -> None:
        self.__config.put("broker.host", host)
        self.__config.put("broker.port", port)
        if username is not None:
            self.__config.put("broker.username", username)
        if password is not None:
            self.__config.put("broker.password", password)

    def get_broker(self) -> tuple[str, int, str, str]:
        broker_info = self.__config.get("broker")
        if broker_info is None:
            self.__config.put("broker", { "host": "localhost", "port": 1883 })
            return self.get_broker()
        return (
            broker_info.get("host", "localhost"),
            broker_info.get("port", 1883),
            broker_info.get("username", ""),
            broker_info.get("password", "")
        )

    def get_topics(self) -> dict:
        topics = self.__config.get("topics")
        if topics is None:
            self.__config.put("topics", {})
            return self.get_topics()
        return topics

    def remove_topic(self, topic_uuid: str) -> None:
        self.__config.remove(f"topics.{topic_uuid}")


class MqttSim:
    def __init__(self, config: MqttSimConfig, logger: any):
        self.__logger = logger
        self.__config = config
        self.__topic_data_generators = {
            topic_uuid: MqttSimDataGenerator(topic_config.get("data_format"))
            for topic_uuid, topic_config in self.__config.get_topics().items()
        }
        self.__setup_client()
        self.__setup_publishing_thread()

    def __setup_publishing_thread(self) -> None:
        self.__should_stop_publishing_thread = False
        self.__publishing_thread = Thread(target=self.__publishing_thread_fn)

    def __publishing_thread_fn(self) -> None:
        def time_diff_in_seconds(time1, time2) -> int:
            diff_dt = time1 - time2
            return diff_dt.total_seconds()

        topics_data = self.__config.get_topics()
        last_sent = {topic_uuid: datetime.now() for topic_uuid in topics_data.keys()}

        while not self.__should_stop_publishing_thread:
            if not self.is_connected_to_broker():
                sleep(0.5)
                continue
            now = datetime.now()
            for topic_uuid, topic_config in topics_data.items():
                if topic_uuid not in last_sent:
                    last_sent[topic_uuid] = now
                    continue
                if topic_config.get("manual"):
                    continue
                if time_diff_in_seconds(now, last_sent[topic_uuid]) > topic_config.get("interval"):
                    self.send_single_message(topic_uuid)
                    last_sent[topic_uuid] = now
            sleep(0.01)

    def __setup_client(self) -> None:
        def on_message(client, userdata, message) -> None:
            self.__logger.info(f"Received message from broker: '{message}'.")

        def on_connect(client, userdata, flags, rc) -> None:
            if rc == CONNACK_ACCEPTED:
                self.__logger.info("Connected to broker.")
            else:
                self.__logger.error(f"Error when connecting to broker (rc={rc}).")

        def on_disconnect(client, userdata, rc) -> None:
            if rc == 0:
                self.__logger.info(f"Disconnected from broker.")
            else:
                self.__logger.error("Unexpected disconnection from broker.")

        self.__client = Client()
        self.__client.on_message = on_message
        self.__client.on_connect = on_connect
        self.__client.on_disconnect = on_disconnect

    # start publishing thread
    def start(self) -> None:
        self.__publishing_thread.start()

    # disconnect from broker, stop publishing thread and wait for it to join
    def stop(self) -> None:
        self.disconnect_from_broker()
        self.__should_stop_publishing_thread = True
        self.__publishing_thread.join()

    def is_connected_to_broker(self) -> bool:
        return self.__client.is_connected()

    # connects to broker and starts client loop
    def connect_to_broker(self) -> bool:
        host, port, username, password = self.__config.get_broker()
        self.__logger.info(f"Trying to connect to broker {host}:{port}...")
        try:
            self.__client.connect(host, port)
            self.__client.username_pw_set(username, password)
            self.__client.loop_start()
        except ConnectionError:
            self.__logger.error(f"Couldn't connect to broker {host}:{port}.")
            return False
        except Exception:
            self.__logger.error(
                f"Unknown error occured when trying to connect to broker."
            )
            return False
        return True

    def disconnect_from_broker(self) -> None:
        self.__client.disconnect()
        self.__client.loop_stop()

    # Sets broker host and port (and saves it into config file)
    def set_broker(self, host: str, port: int) -> None:
        self.__config.put_broker(host, port)
        self.__logger.info(f"Changed broker to {host}:{port}.")

    # Removes topic from config (and saves it into config file).
    # If publishing thread was already started, it will take the topic into account.
    def remove_topic(self, topic_uuid: str) -> None:
        topic_data = self.__config.get_topic_data(topic_uuid)
        self.__client.unsubscribe(topic_data.get("topic"))
        self.__config.remove_topic(topic_uuid)
        self.__logger.info(f"Removed topic: {topic_data.get("topic")}) [uuid={topic_uuid}].")
        del self.__topic_data_generators[topic_uuid]

    # Adds topic to config (and saves it into config file).
    # If publishing thread was already started, it will take the topic into account.
    def add_topic(self, topic_config: dict) -> str:
        uuid = self.__config.put_topic(topic_config)
        self.__logger.info(f"Added topic: {topic_config.get("topic")} [uuid={uuid}].")
        self.__topic_data_generators[uuid] = MqttSimDataGenerator(
            topic_config.get("data_format")
        )
        return uuid

    def get_logger(self) -> any:
        return self.__logger

    def get_config(self) -> MqttSimConfig:
        return self.__config

    def edit(self, topic_uuid, new_data) -> None:
        self.__config.put_topic(new_data, uuid=topic_uuid)
        self.__topic_data_generators[topic_uuid].reinitalize(
            new_data.get("data_format")
        )

    def send_single_message(self, topic_uuid) -> None:
        if not self.is_connected_to_broker():
            self.__logger.error("Trying to send message when not connected to broker.")
            return
        topic_data = self.__config.get_topic_data(topic_uuid)
        self.__logger.info(f"Publishing data on {topic_data.get("topic")} [uuid={topic_uuid}]...")
        message = self.__topic_data_generators.get(topic_uuid).next_message()
        self.__client.publish(topic_data.get("topic"), message)

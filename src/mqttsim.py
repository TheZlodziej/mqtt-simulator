from confighandler import ConfigHandler
from paho.mqtt.client import Client, CONNACK_ACCEPTED
from threading import Thread
from datetime import datetime
from time import sleep
from mqttsimdatagenerator import MqttSimDataGenerator
from mqttprotogenerator import MqttProtoGenerator


class MqttSimConfig:
    def __init__(self, path: str):
        self.__config = ConfigHandler(path)

    def put_topic(self, topic: str, data_format: str, interval: float = 1.5, manual: bool = False) -> None:
        self.__config.put(f"topics.{topic}.data_format", data_format)
        self.__config.put(f"topics.{topic}.interval", interval)
        self.__config.put(f"topics.{topic}.manual", manual)

    def put_topic(self, topic: str, topic_config: dict[str, str]) -> None:
        self.__config.put(f"topics.{topic}", topic_config)

    def get_topic_data(self, topic: str) -> dict | None:
        return self.__config.get(f"topics.{topic}")

    def put_broker(self, host: str, port: int) -> None:
        self.__config.put("broker.host", host)
        self.__config.put("broker.port", port)

    def get_broker(self) -> tuple[str, int]:
        broker_info = self.__config.get("broker")
        if broker_info is None:
            self.__config.put("broker", {"host": "localhost", "port": 1883})
            return self.get_broker()
        return broker_info.get("host", "localhost"), broker_info.get("port", 1883)

    def get_topics(self) -> dict:
        topics = self.__config.get("topics")
        if topics is None:
            self.__config.put("topics", {})
            return self.get_topics()
        return topics

    def remove_topic(self, topic: str) -> None:
        self.__config.remove(f"topics.{topic}")


class MqttSim:
    def __init__(self, config: MqttSimConfig, logger: any):
        self.__logger = logger
        self.__config = config
        self.__topic_data_generators = {
            topic_name: MqttSimDataGenerator(topic_config.get("data_format")) for topic_name, topic_config in self.__config.get_topics().items() if "data_format" in topic_config
        }
        self.__proto_topic_data_generators = {topic_name: MqttProtoGenerator(topic_config.get(
            "message")) for topic_name, topic_config in self.__config.get_topics().items() if "message" in topic_config}
        self.__setup_client()
        self.__setup_publishing_thread()

    def __setup_publishing_thread(self) -> None:
        self.__should_stop_publishing_thread = False
        self.__publishing_thread = Thread(target=self.__publishing_thread_fn)

    def __publishing_thread_fn(self) -> None:
        def time_diff_in_seconds(time1, time2) -> int:
            diff_dt = time1 - time2
            return diff_dt.total_seconds()

        topics = self.__config.get_topics()
        last_sent = {topic: datetime.now() for topic in topics.keys()}

        while not self.__should_stop_publishing_thread:
            if not self.is_connected_to_broker():
                sleep(0.5)
                continue
            now = datetime.now()
            for topic, config in topics.items():
                if topic not in last_sent:
                    last_sent[topic] = now
                    continue
                if config.get("manual"):
                    continue
                if time_diff_in_seconds(now, last_sent[topic]) > config.get("interval"):
                    self.send_single_message(topic)
                    last_sent[topic] = now
            sleep(0.01)

    def __setup_client(self) -> None:
        def on_message(client, userdata, message) -> None:
            return
            if message.topic in self.__topic_data_generators:
                self.__logger.info(
                    f"Received message from broker {message.topic}: '{message.payload}'.")
            elif message.topic in self.__proto_topic_data_generators:
                message_constructor = self.__proto_topic_data_generators[
                    message.topic].message_constructor
                proto_message = message_constructor()
                proto_message.ParseFromString(message.payload)
                self.__logger.info(
                    f"Received message from broker on topic {message.topic}: '{proto_message}'.")

        def on_connect(client, userdata, flags, rc) -> None:
            for topic_name, _ in self.__config.get_topics().items():
                self.__client.subscribe(topic_name)
            if rc == CONNACK_ACCEPTED:
                self.__logger.info("Connected to broker.")
            else:
                self.__logger.error(
                    f"Error when connecting to broker (rc={rc}).")

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
        host, port = self.__config.get_broker()
        self.__logger.info(f"Trying to connect to broker {host}:{port}...")
        try:
            self.__client.connect(host, port)  # TODO: connect_async ?
            self.__client.loop_start()
        except ConnectionError:
            self.__logger.error(f"Coulnd't connect to broker {host}:{port}.")
            return False
        except Exception:
            self.__logger.error(
                "Unknown error occured when trying to connect to broker.")
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
    def remove_topic(self, topic: str) -> None:
        self.__client.unsubscribe(topic)
        self.__config.remove_topic(topic)
        self.__logger.info(f"Removed topic: {topic}.")
        if topic in self.__topic_data_generators:
            del self.__topic_data_generators[topic]
        else:
            del self.__proto_topic_data_generators[topic]

    # Adds JSON topic to config (and saves it into config file).
    # If publishing thread was already started, it will take the topic into account.
    def add_topic(self, topic: str, topic_config: dict) -> None:
        self.__config.put_topic(topic, topic_config)
        self.__logger.info(f"Added topic: {topic}.")
        self.__topic_data_generators[topic] = MqttSimDataGenerator(
            topic_config.get("data_format"))
        self.__client.subscribe(topic)

    def get_logger(self) -> any:
        return self.__logger

    def get_config(self) -> MqttSimConfig:
        return self.__config

    def edit(self, topic_name, new_data) -> None:
        self.__config.put_topic(topic_name, new_data)
        if "data_format" in new_data.keys():
            self.__topic_data_generators[topic_name].reinitalize(
                new_data.get("data_format"))
        else:
            self.__proto_topic_data_generators[topic_name] = MqttProtoGenerator(
                new_data.get("message"))

    def send_single_message(self, topic_name) -> None:
        if not self.is_connected_to_broker():
            self.__logger.error(
                "Trying to send message when not connected to broker.")
            return
        if topic_name in self.__proto_topic_data_generators:
            self.__logger.info(f"Publishing data on {topic_name}")
            gen = self.__proto_topic_data_generators[topic_name]
            proto_message = gen.get_random_message()
            self.__client.publish(
                topic_name, proto_message.SerializeToString())
        else:
            self.__logger.info(f"Publishing data on {topic_name}...")
            message = self.__topic_data_generators.get(
                topic_name).next_message()
            self.__client.publish(topic_name, message)

    def add_proto_topic(self, topic: str, topic_config: dict) -> None:
        self.__config.put_topic(topic, topic_config)
        self.__logger.info(f"Added topic: {topic}.")
        self.__proto_topic_data_generators[topic] = MqttProtoGenerator(
            topic_config.get("message"))
        self.__client.subscribe(topic)

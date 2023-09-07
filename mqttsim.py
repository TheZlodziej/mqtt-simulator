from confighandler import ConfigHandler
from paho.mqtt.client import Client, CONNACK_ACCEPTED

class MqttSimConfig:
    def __init__(self, path: str):
        self.__config = ConfigHandler(path)

    def put_topic(self, topic: str, data_format: str, interval: float = 1.5) -> None:
        self.__config.put(f"topics.{topic}.data_format", data_format)
        self.__config.put(f"topics.{topic}.interval", interval)

    def put_topic(self, topic: str, topic_config: dict) -> None:
        self.__config.put(f"topics.{topic}", topic_config)

    def get_topic_data(self, topic: str) -> dict | None:
        self.__config.get(topic)

    def put_broker(self, host: str, port: int) -> None:
        self.__config.put("broker.host", host)
        self.__config.put("broker.port", port)

    def get_broker(self) -> (str, int):
        broker_info = self.__config.get("broker")
        return broker_info.get("host", "localhost"), broker_info.get('port', 1883)

    def get_topics(self) -> dict:
        topics = self.__config.get("topics")
        return topics if topics is not None else dict()

    def remove_topic(self, topic: str) -> None:
        self.__config.remove(f"topics.{topic}")


class MqttSim:
    def __init__(self, config: MqttSimConfig, logger):
        self.__logger = logger
        self.__config = config
        self.__setup_client()

    def __setup_client(self) -> None:
        def on_message(client, userdata, message):
            self.__logger.info(f"Received message from broker: '{message}'.")

        def on_connect(client, userdata, flags, rc):
            if rc == CONNACK_ACCEPTED:
                self.__logger.info("Connected to broker.")
            else:
                self.__logger.error(f"Error when connecting to broker (rc={rc}).")

        def on_disconnect(client, userdata, rc):
            if rc == 0:
                self.__logger.info(f"Disconnected from broker.")
            else:
                self.__logger.error("Unexpected disconnection from broker.")

        self.__client = Client()
        self.__client.on_message = on_message
        self.__client.on_connect = on_connect
        self.__client.on_disconnect = on_disconnect

    def is_connected_to_broker(self) -> bool:
        return self.__client.is_connected()

    def connect_to_broker(self) -> bool:
        host, port = self.__config.get_broker()
        self.__logger.info(f"Trying to connect to broker {host}:{port}...")
        try:
            self.__client.connect(host, port)
            self.__client.loop_start()
        except ConnectionError:
            self.__logger.error(f"Coulnd't connect to broker {host}:{port}.")
            return False
        except Exception:
            self.__logger.error(f"Unknown error occured when trying to connect to broker.")
            return False
        return True
    
    def disconnect_from_broker(self) -> None:
        self.__client.disconnect()
        self.__client.loop_stop()

    def set_broker(self, host: str, port: int) -> None:
        curr_host, curr_port = self.__config.get_broker()
        if host == curr_host and port == curr_port:
            return None
        self.__config.put_broker(host, port)
        self.__logger.info(f"Changed broker to {host}:{port}.")

    def remove_topic(self, topic: str) -> None:
        self.__client.unsubscribe(topic)
        self.__config.remove_topic(topic)
        self.__logger.info(f"Removed topic: {topic}.")

    def add_topic(self, topic: str, topic_config: dict) -> None:
        self.__config.put_topic(topic, topic_config)
        self.__logger.info(f"Added topic: {topic}.")

    def get_config(self) -> MqttSimConfig:
        return self.__config

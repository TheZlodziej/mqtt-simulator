from confighandler import ConfigHandler
from paho.mqtt.client import Client


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
    def __init__(self, config: MqttSimConfig):
        self.__config = config
        self.__client = Client()
        self.__setup_client()
        self.logger = None

    def __setup_client(self) -> None:
        self.__client.on_message = lambda a, b, msg: print(f"msg: {msg}")
        self.__client.on_connect = lambda a, b, c, d: print("connected")
        self.__client.on_disconnect = lambda a, b, c: print("disconnected")
        host, port = self.__config.get_broker()
        self.__client.connect(host, port)

    # resubscribes all topics
    # def update_topics(self) -> None:
    #     self.__client.unsubscribe('#')

    def __reinitialize_client(self) -> None:
        self.__client.disconnect()
        self.__client.reinitialise()
        self.__setup_client()

    # def loop(self) -> None:
    #     self.__client.loop()
    #     # self.__client.loop_forever()

    def set_broker(self, host: str, port: int) -> None:
        curr_host, curr_port = self.__config.get_broker()

        if host == curr_host and port == curr_port:
            return None

        self.__config.put_broker(host, port)
        self.__reinitialize_client()

    def remove_topic(self, topic: str) -> None:
        self.__client.unsubscribe(topic)
        self.__config.remove_topic(topic)
        self.logger.info(f"Removed topic: {topic}")

    def add_topic(self, topic: str, topic_config: dict) -> None:
        self.__config.put_topic(topic, topic_config)
        self.logger.info(f"Added topic: {topic}")

    def get_config(self) -> MqttSimConfig:
        return self.__config

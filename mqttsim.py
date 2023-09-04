from confighandler import ConfigHandler
from paho.mqtt.client import Client


class MqttSimConfig:
    def __init__(self, path: str):
        self.__config = ConfigHandler(path)

    def put_topic(self, topic: str, data_format: str) -> None:
        self.__config.put(f"topics.{topic}.data_format", data_format)

    def get_topic_data(self, topic: str) -> dict | None:
        self.__config.get(topic)

    def put_broker(self, host: str, port: int) -> None:
        self.__config.put("broker.host", host)
        self.__config.put("broker.port", port)

    def get_broker(self) -> (str, int):
        broker_info = self.__config.get("broker")
        return broker_info.get('host', 'localhost'), broker_info.get('port', 1883)


class MqttSim:
    def __init__(self, config):
        self.__config = config
        self.__client = Client()
        self.__setup_client()

    def __setup_client(self):

        self.__client.on_message = lambda a, b, msg: print(f"msg: {msg}")
        self.__client.on_connect = lambda a, b, c, d: print("connected")
        self.__client.on_disconnect = lambda a, b, c: print("disconnected")
        host, port = self.__config.get_broker()
        self.__client.connect(host, port)

    # resubscribes all topics
    def update_topics(self) -> None:
        self.__client.unsubscribe('#')

    def update_client(self) -> None:
        self.__client.disconnect()
        self.__client.reinitialise()
        self.__setup_client()

    def loop(self) -> None:
        self.__client.loop()
        # self.__client.loop_forever()

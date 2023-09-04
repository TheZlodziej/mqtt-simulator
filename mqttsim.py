from confighandler import ConfigHandler


class MqttSimConfig:
    def __init__(self, path):
        self.__config = ConfigHandler(path)
        self.__init_default()

    # reads config, if it's missing some crucial data, fills it in with default values
    def __init_default(self):
        if not self.__config.get("broker"):
            self.put_broker("localhost")

    def put_topic(self, topic, data_format):
        self.__config.put(f"topics.{topic}.data_format", data_format)

    def put_broker(self, url):
        self.__config.put("broker", url)


class MqttSim:
    def __init__(self, config):
        self.__config = config

    def add_topic(self, topic, data_format):
        self.__config.put_topic(topic, data_format)

    def set_broker(self, url):
        self.__config.put_broker(url)

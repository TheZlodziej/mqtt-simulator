from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QPushButton, QHBoxLayout, QLabel, QWidget
from gui.generated.mainwindow import Ui_MainWindow
from mqttsim import MqttSim
from functools import partial


class MqttSimMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, sim: MqttSim):
        super(MqttSimMainWindow, self).__init__()
        self.setupUi(self)
        self.__sim = sim
        self.__config = sim.get_config()
        self.__setup_connects()
        self.__set_values_from_config()

    def __setup_connects(self) -> None:
        def on_broker_connect_btn_clicked() -> None:
            self.__sim.set_broker(
                self.broker_hostname.text, self.broker_port.value)

        def on_clear_logs_btn_clicked() -> None:
            self.logs_list.clear()

        self.broker_connect_btn.clicked.connect(on_broker_connect_btn_clicked)
        self.clear_logs_btn.clicked.connect(on_clear_logs_btn_clicked)

    def __set_values_from_config(self):
        def set_values_from_config_broker() -> None:
            hostname, port = self.__config.get_broker()
            self.broker_hostname.text = hostname
            self.broker_port.value = port

        def set_values_from_config_topics() -> None:
            def add_topic_item(topic: str, topic_config: dict) -> QListWidgetItem:
                # layout
                layout = QHBoxLayout()

                # topic name label
                lbl = QLabel(topic)
                layout.addWidget(lbl)

                # remove btn
                def on_remove_btn_clicked(topic):
                    self.__sim.remove_topic(topic)
                    self.topics_list.removeItem(layout)
                    print('finish me -> on_remove_btn_clicked', topic_config)

                remove_btn = QPushButton("Remove")
                remove_btn.clicked.connect(partial(on_remove_btn_clicked, topic))
                layout.addWidget(remove_btn)
                
                # widget
                widget = QWidget(parent=self.topics_list_widget)
                widget.setLayout(layout)
                widget.resize(200, 200)

            topics = self.__config.get_topics()
            for topic, topic_config in topics.items():
                add_topic_item(topic, topic_config)

        set_values_from_config_broker()
        set_values_from_config_topics()

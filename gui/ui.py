from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QPushButton, QHBoxLayout, QDialog, QLabel, QWidget, QMessageBox
from PySide6.QtCore import Qt, QCoreApplication
from gui.generated.mainwindow import Ui_MainWindow
from gui.generated.addtopicdialog import Ui_Dialog
from mqttsim import MqttSim
from functools import partial
from logger import QListWidgetLogHandler

class MqttSimAddTopicWindow(Ui_Dialog, QDialog):
    def __init__(self):
        super(MqttSimAddTopicWindow, self).__init__()
        self.setupUi(self)


class MqttSimMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, sim: MqttSim, logger):
        super(MqttSimMainWindow, self).__init__()
        self.setupUi(self)
        self.__logger = logger
        self.__setup_logger()
        self.__sim = sim
        self.__config = sim.get_config()
        self.__setup_connects()
        self.__set_values_from_config()

    def __setup_logger(self) -> None:
        self.__logger.addHandler(QListWidgetLogHandler(self.logs_list))

    def __setup_connects(self) -> None:
        def on_broker_connect_btn_clicked() -> None:
            if self.__sim.is_connected_to_broker():
                self.__sim.disconnect_from_broker()
                self.broker_connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
                self.broker_connect_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect to broker", None))
            else:
                if self.__sim.connect_to_broker():
                    self.broker_connect_btn.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
                    self.broker_connect_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Disconnect from broker", None))

        def on_clear_logs_btn_clicked() -> None:
            self.logs_list.clear()
            self.__logger.info("Cleared logs.")

        def on_add_topic_btn_clicked() -> None:
            def validate_input(topic_name, topic_config):
                return len(topic_name) > 0 and topic_name not in self.__config.get_topics().keys()
            add_topic_window = MqttSimAddTopicWindow()
            add_topic_window.exec()
            if add_topic_window.accepted:
                topic_name = add_topic_window.name_line_edit.text()
                topic_config = {
                    'data_format': add_topic_window.format_line_edit.text(),
                    'interval': add_topic_window.interval_spin_box.value()
                }
                if validate_input(topic_name, topic_config):
                    self.__sim.add_topic(topic_name, topic_config)
                    self.__add_topic_to_item_list(topic_name, topic_config)
                else:
                    QMessageBox().critical(self, "Error!", "Invalid topic input.")

        def on_broker_info_changed() -> None:
            self.__sim.set_broker(self.broker_hostname.text(), self.broker_port.value())

        self.broker_connect_btn.clicked.connect(on_broker_connect_btn_clicked)
        self.clear_logs_btn.clicked.connect(on_clear_logs_btn_clicked)
        self.add_topic_btn.clicked.connect(on_add_topic_btn_clicked)
        self.broker_hostname.textChanged.connect(on_broker_info_changed)
        self.broker_port.valueChanged.connect(on_broker_info_changed)

    def __add_topic_to_item_list(self, topic: str, topic_config: dict) -> QListWidgetItem:
        # TODO popup with edit values

        # layout
        layout = QHBoxLayout()

        # topic name label
        lbl = QLabel(topic)
        layout.addWidget(lbl)

        # widget
        widget = QWidget()
        widget.setLayout(layout)
        self.topics_list.insertWidget(0, widget)

        # remove btn
        def on_remove_btn_clicked(topic: str) -> None:
            self.__sim.remove_topic(topic)
            widget.deleteLater()

        remove_btn = QPushButton("Remove")
        remove_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        remove_btn.clicked.connect(partial(on_remove_btn_clicked, topic))
        layout.addWidget(remove_btn)

    def __set_values_from_config(self) -> None:
        def set_values_from_config_broker() -> None:
            hostname, port = self.__config.get_broker()
            self.broker_hostname.setText(hostname)
            self.broker_port.setValue(port)

        def set_values_from_config_topics() -> None:
            topics = self.__config.get_topics()
            for topic, topic_config in topics.items():
                self.__add_topic_to_item_list(topic, topic_config)

        set_values_from_config_broker()
        set_values_from_config_topics()

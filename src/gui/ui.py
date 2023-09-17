from PySide6.QtWidgets import (
    QMainWindow,
    QListWidgetItem,
    QToolButton,
    QHBoxLayout,
    QDialog,
    QLabel,
    QWidget,
    QMessageBox,
)
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QIcon
from gui.generated.mainwindow import Ui_MainWindow
from gui.generated.addtopicdialog import Ui_AddTopicDialog
from gui.generated.edittopicdialog import Ui_EditTopicDialog
from mqttsim import MqttSim
from functools import partial
from logger import QListWidgetLogHandler
import icons.generated.icons


class MqttSimTopicToolButton(QToolButton):
    def __init__(self, icon: str, tooltip: str):
        super(MqttSimTopicToolButton, self).__init__()
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setIcon(QIcon(icon))
        self.setToolTip(QCoreApplication.translate("MainWindow", tooltip, None))


class MqttSimAddTopicWindow(Ui_AddTopicDialog, QDialog):
    def __init__(self):
        super(MqttSimAddTopicWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/mqtt.svg"))


class MqttSimEditTopicWindow(Ui_EditTopicDialog, QDialog):
    def __init__(self, topic_name: str, topic_data: dict):
        super(MqttSimEditTopicWindow, self).__init__()
        self.setupUi(self)
        self.__set_topic_values(topic_name, topic_data)
        self.setWindowIcon(QIcon(":/icons/mqtt.svg"))

    def __set_topic_values(self, topic_name, topic_data) -> None:
        self.name_line_edit.setText(topic_name)
        self.format_text_edit.setPlainText(topic_data.get("data_format"))
        self.interval_spin_box.setValue(topic_data.get("interval"))
        self.manual_check_box.setChecked(topic_data.get("manual"))


class MqttSimTopicWidget(QWidget):
    def __init__(self, topic: str):
        super(MqttSimTopicWidget, self).__init__()
        self.topic = topic

        # hlayout
        hlayout = QHBoxLayout()
        self.setLayout(hlayout)

        # topic name label
        lbl = QLabel(topic)
        hlayout.addWidget(lbl)

        # remove btn
        self.remove_btn = MqttSimTopicToolButton(
            ":/icons/remove.svg",
            QCoreApplication.translate("MainWindow", "Remove", None),
        )
        hlayout.addWidget(self.remove_btn)

        # edit btn
        self.edit_btn = MqttSimTopicToolButton(":/icons/edit.svg", QCoreApplication.translate("MainWindow", "Edit", None))
        self.edit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        hlayout.addWidget(self.edit_btn)

        # send now btn
        self.send_now_btn = MqttSimTopicToolButton(
            ":/icons/send.svg",
            QCoreApplication.translate("MainWindow", "Send now", None),
        )
        hlayout.addWidget(self.send_now_btn)


class MqttSimMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, sim: MqttSim):
        super(MqttSimMainWindow, self).__init__()
        self.setupUi(self)
        self.__setup_icons()
        self.__logger = sim.get_logger()
        self.__setup_logger()
        self.__sim = sim
        self.__config = sim.get_config()
        self.__setup_connects()
        self.__set_values_from_config()

    def __setup_icons(self) -> None:
        self.setWindowIcon(QIcon(":/icons/mqtt.svg"))
        self.add_topic_btn.setIcon(QIcon(":/icons/add.svg"))

    def __setup_logger(self) -> None:
        self.__logger.addHandler(QListWidgetLogHandler(self.logs_list))

    def __setup_connects(self) -> None:
        def on_broker_connect_btn_clicked() -> None:
            if self.__sim.is_connected_to_broker():
                self.__sim.disconnect_from_broker()
                self.broker_connect_btn.setText(QCoreApplication.translate("MainWindow", "Connect", None))
                self.broker_connect_btn.setToolTip(QCoreApplication.translate("MainWindow", "Connect to broker", None))
            else:
                if self.__sim.connect_to_broker():
                    self.broker_connect_btn.setText(QCoreApplication.translate("MainWindow", "Disconnect", None))
                    self.broker_connect_btn.setToolTip(QCoreApplication.translate("MainWindow", "Disconnect from broker", None))

        def on_clear_logs_btn_clicked() -> None:
            self.logs_list.clear()
            self.__logger.info("Cleared logs.")

        def on_add_topic_btn_clicked() -> None:
            def validate_input(topic_name, topic_config) -> bool:
                return len(topic_name) > 0 and topic_name not in self.__config.get_topics().keys()

            add_topic_window = MqttSimAddTopicWindow()
            if add_topic_window.exec():
                topic_name = add_topic_window.name_line_edit.text()
                topic_config = {
                    "data_format": add_topic_window.format_text_edit.toPlainText(),
                    "interval": add_topic_window.interval_spin_box.value(),
                    "manual": add_topic_window.manual_check_box.isChecked(),
                }
                if validate_input(topic_name, topic_config):
                    self.__sim.add_topic(topic_name, topic_config)
                    self.__add_topic_to_item_list(topic_name)
                else:
                    QMessageBox().critical(self, "Error!", "Invalid topic input.")

        def on_broker_info_changed() -> None:
            self.__sim.set_broker(self.broker_hostname.text(), self.broker_port.value())

        def on_topic_search_text_changed() -> None:
            for widget in self.topics_list_widget.findChildren(MqttSimTopicWidget):
                if self.topic_search_line_edit.text().lower() in widget.topic.lower():
                    widget.show()
                else:
                    widget.hide()

        self.broker_connect_btn.clicked.connect(on_broker_connect_btn_clicked)
        self.clear_logs_btn.clicked.connect(on_clear_logs_btn_clicked)
        self.add_topic_btn.clicked.connect(on_add_topic_btn_clicked)
        self.broker_hostname.textChanged.connect(on_broker_info_changed)
        self.broker_port.valueChanged.connect(on_broker_info_changed)
        self.topic_search_line_edit.textChanged.connect(on_topic_search_text_changed)

    def __add_topic_to_item_list(self, topic: str) -> None:
        topic_widget = MqttSimTopicWidget(topic)

        def on_remove_btn_clicked(topic: str) -> None:
            self.__sim.remove_topic(topic)
            topic_widget.deleteLater()

        def on_edit_btn_clicked(topic: str) -> None:
            topic_data = self.__config.get_topic_data(topic)
            edit_topic_window = MqttSimEditTopicWindow(topic, topic_data)

            if edit_topic_window.exec():
                edited_topic_data = {
                    "data_format": edit_topic_window.format_text_edit.toPlainText(),
                    "interval": edit_topic_window.interval_spin_box.value(),
                    "manual": edit_topic_window.manual_check_box.isChecked(),
                }
                if edited_topic_data != topic_data:
                    self.__sim.edit(topic, edited_topic_data)
                    self.__logger.info(f"Edited topic {topic} ({topic_data} -> {edited_topic_data}).")

        topic_widget.remove_btn.clicked.connect(partial(on_remove_btn_clicked, topic))
        topic_widget.edit_btn.clicked.connect(partial(on_edit_btn_clicked, topic))
        topic_widget.send_now_btn.clicked.connect(partial(self.__sim.send_single_message, topic))

        self.topics_list.insertWidget(0, topic_widget)

    def __set_values_from_config(self) -> None:
        def set_values_from_config_broker() -> None:
            hostname, port = self.__config.get_broker()
            self.broker_hostname.setText(hostname)
            self.broker_port.setValue(port)

        def set_values_from_config_topics() -> None:
            topics = self.__config.get_topics()
            for topic in topics.keys():
                self.__add_topic_to_item_list(topic)

        set_values_from_config_broker()
        set_values_from_config_topics()

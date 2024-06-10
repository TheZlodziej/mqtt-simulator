from PySide6.QtWidgets import (
    QMainWindow,
    QListWidgetItem,
    QToolButton,
    QHBoxLayout,
    QDialog,
    QLabel,
    QWidget,
    QMessageBox,
    QFileDialog,
    QInputDialog,
)
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QIcon
from gui.generated.mainwindow import Ui_MainWindow
from gui.generated.addtopicdialog import Ui_AddTopicDialog
from mqttsim import MqttSim
from functools import partial
from logger import QListWidgetLogHandler
from os import listdir, path, getcwd
import icons.generated.icons
from gui.generated.addprototopicdialog import Ui_AddProtoTopicDialog
from gui.generated.choosetopicdialog import Ui_ChooseTopicDialog
from protogenerator import ProtoDataGenerator


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
        self.load_from_file_btn.clicked.connect(self.__on_load_from_file_btn_clicked)
        self.__load_patterns()
        self.predefined_pattern_combo_box.currentIndexChanged.connect(
            self.__on_pattern_selected
        )
        self.save_as_pattern_btn.clicked.connect(
            self.__on_save_as_pattern_btn_clicked)

    def __on_load_from_file_btn_clicked(self) -> None:
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select file",
            None,
            "All files (*.*);;Text files (*.txt);;JSON files (*.json)",
        )

        if len(filename) == 0:
            return

        with open(filename, "r") as file:
            self.format_text_edit.setPlainText(file.read())

    def __on_pattern_selected(self, index):
        pattern_name = self.predefined_pattern_combo_box.itemText(index)
        pattern_data = self.predefined_pattern_combo_box.itemData(index)

        response = QMessageBox.question(
            self,
            "Confirm action",
            f"Are you sure you want to load {pattern_name}? This will erase all data in format input.",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if response == QMessageBox.Ok:
            self.format_text_edit.setPlainText(pattern_data)
        else:
            self.predefined_pattern_combo_box.blockSignals(True)
            self.predefined_pattern_combo_box.setCurrentIndex(-1)
            self.predefined_pattern_combo_box.blockSignals(False)

    def __load_patterns(self):
        self.predefined_pattern_combo_box.clear()

        patterns_dir = path.join(getcwd(), "patterns")
        pattern_filenames = [
            path.join(patterns_dir, file)
            for file in listdir(patterns_dir)
            if path.isfile(path.join(patterns_dir, file))
        ]

        for pattern_filename in pattern_filenames:
            with open(pattern_filename, "r") as file:
                pattern_name = path.splitext(
                    path.basename(pattern_filename).replace("_", " ")
                )[0]
                pattern_value = file.read()
                self.predefined_pattern_combo_box.addItem(pattern_name, pattern_value)

    def __on_save_as_pattern_btn_clicked(self):
        pattern_name, accepted = QInputDialog.getText(
            self, "Input dialog", "Pattern name:"
        )
        if not accepted:
            return

        if len(pattern_name) == 0:
            QMessageBox.critical(
                self, "Error", "Pattern name cannot be empty.", QMessageBox.Ok
            )
            return

        pattern_filename = pattern_name.replace(" ", "_") + ".pattern"
        pattern_path = path.join(getcwd(), "patterns", pattern_filename)

        if path.exists(pattern_path):
            result = QMessageBox.warning(
                self,
                "Warning",
                "Pattern with this name already exists. Do you want to overwrite it?",
                QMessageBox.Yes | QMessageBox.No,
            )
            if result == QMessageBox.No:
                return

        with open(pattern_path, "w") as file:
            file.write(self.format_text_edit.toPlainText())
        self.__load_patterns()


class MqttSimEditTopicWindow(MqttSimAddTopicWindow):
    def __init__(self, topic_data: dict):
        super(MqttSimEditTopicWindow, self).__init__()
        self.__set_topic_values(topic_data)
        self.setWindowTitle(
            QCoreApplication.translate("EditTopicDialog", "Edit topic", None)
        )
        self.label.setText(
            QCoreApplication.translate("EditTopicDialog", "Edit topic", None)
        )

    def __set_topic_values(self, topic_data) -> None:
        self.name_line_edit.setText(topic_data.get("topic"))
        self.format_text_edit.setPlainText(topic_data.get("data_format"))
        self.interval_spin_box.setValue(topic_data.get("interval"))
        self.manual_check_box.setChecked(topic_data.get("manual"))


class MqttSimTopicWidget(QWidget):
    def __init__(self, topic_name: str):
        super(MqttSimTopicWidget, self).__init__()

        self.topic = topic_name

        # hlayout
        hlayout = QHBoxLayout()
        self.setLayout(hlayout)

        # topic name label
        self.topic_lbl = QLabel(self.topic)
        # TODO: add on hover uuid
        hlayout.addWidget(self.topic_lbl)

        # remove btn
        self.remove_btn = MqttSimTopicToolButton(
            ":/icons/remove.svg",
            QCoreApplication.translate("MainWindow", "Remove", None),
        )
        hlayout.addWidget(self.remove_btn)

        # edit btn
        self.edit_btn = MqttSimTopicToolButton(
            ":/icons/edit.svg", QCoreApplication.translate("MainWindow", "Edit", None)
        )
        self.edit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        hlayout.addWidget(self.edit_btn)

        # send now btn
        self.send_now_btn = MqttSimTopicToolButton(
            ":/icons/send.svg",
            QCoreApplication.translate("MainWindow", "Send now", None),
        )
        hlayout.addWidget(self.send_now_btn)

    def set_topic_name(self, new_topic_name: str) -> None:
        self.topic = new_topic_name
        self.topic_lbl.setText(new_topic_name)


class MqttSimAddProtoTopicWindow(Ui_AddProtoTopicDialog, QDialog):
    def __init__(self):
        super(MqttSimAddProtoTopicWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/mqtt.svg"))


class MqttSimEditProtoTopicWindow(MqttSimAddProtoTopicWindow, QDialog):
    def __init__(self, topic_name: str, topic_data: dict):
        super(MqttSimEditProtoTopicWindow, self).__init__()
        self.__set_topic_values(topic_name, topic_data)
        self.setWindowIcon(QIcon(":/icons/mqtt.svg"))

    def __set_topic_values(self, topic_name, topic_data) -> None:
        messages = ProtoDataGenerator.get_message_constructors()
        current_item = None
        message_names = sorted(list(messages.keys()), key=lambda s: (not 'Msg' in s, s))
        for message_name in message_names:
            new_item = QListWidgetItem(message_name)
            self.message_list.addItem(new_item)
            if message_name == topic_data["message"]:
                current_item = new_item
        self.message_list.setCurrentItem(current_item)
        self.name_line_edit.setText(topic_name)
        self.file_line_edit.setText(topic_data["file"])
        self.interval_spin_box.setValue(topic_data.get("interval"))
        self.manual_check_box.setChecked(topic_data.get("manual"))


class MqttSimChooseTopicWindow(Ui_ChooseTopicDialog, QDialog):
    def __init__(self):
        super(MqttSimChooseTopicWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/mqtt.svg"))


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
                self.broker_connect_btn.setText(
                    QCoreApplication.translate("MainWindow", "Connect", None)
                )
                self.broker_connect_btn.setToolTip(
                    QCoreApplication.translate("MainWindow", "Connect to broker", None)
                )
            else:
                if self.__sim.connect_to_broker():
                    self.broker_connect_btn.setText(
                        QCoreApplication.translate(
                            "MainWindow", "Disconnect", None)
                    )
                    self.broker_connect_btn.setToolTip(
                        QCoreApplication.translate(
                            "MainWindow", "Disconnect from broker", None)
                    )

        def on_clear_logs_btn_clicked() -> None:
            self.logs_list.clear()
            self.__logger.info("Cleared logs.")

        def on_add_topic_btn_clicked() -> None:
            choose_topic_window = MqttSimChooseTopicWindow()
            choose_topic_window.choose_json_button.clicked.connect(
                choose_topic_window.close)
            choose_topic_window.choose_json_button.clicked.connect(
                on_add_json_btn_clicked)
            choose_topic_window.choose_proto_button.clicked.connect(
                choose_topic_window.close)
            choose_topic_window.choose_proto_button.clicked.connect(
                on_add_proto_btn_clicked)
            choose_topic_window.exec()

        def on_add_json_btn_clicked() -> None:
            def validate_input(topic_config) -> bool:
                return len(topic_config.get("topic")) > 0

            add_topic_window = MqttSimAddTopicWindow()
            while True:
                if add_topic_window.exec() == QDialog.Accepted:
                    topic_config = {
                        "topic": add_topic_window.name_line_edit.text(),
                        "data_format": add_topic_window.format_text_edit.toPlainText(),
                        "interval": add_topic_window.interval_spin_box.value(),
                        "manual": add_topic_window.manual_check_box.isChecked(),
                    }
                    if validate_input(topic_config):
                        uuid = self.__sim.add_topic(topic_config)
                        self.__add_topic_to_item_list(uuid)
                        break  # Break out of the loop if input is valid and accepted
                    else:
                        QMessageBox().critical(self, "Error!", "Invalid topic input.")
                else:
                    break  # Break out of the loop if dialog is cancelled

        def on_add_proto_btn_clicked() -> None:
            def validate_input(topic_name, topic_config) -> bool:
                return (len(topic_name) > 0 and topic_name not in self.__config.get_topics().keys())

            add_topic_window = MqttSimAddProtoTopicWindow()
            messages = ProtoDataGenerator.get_message_constructors()

            message_names = sorted(list(messages.keys()), key=lambda s: (not 'Msg' in s, s))
            for message_name in message_names:
                add_topic_window.message_list.addItem(message_name)
            if add_topic_window.exec():
                if add_topic_window.message_list.currentItem() is None:
                    QMessageBox().critical(self, "Error!", "Invalid topic input.")
                    return
                topic_name = add_topic_window.name_line_edit.text()
                topic_config = {
                    "topic": add_topic_window.name_line_edit.text(),
                    "message": add_topic_window.message_list.currentItem().text(),
                    "interval": add_topic_window.interval_spin_box.value(),
                    "manual": add_topic_window.manual_check_box.isChecked(),
                    "file": add_topic_window.file_line_edit.text()
                }
                if validate_input(topic_name, topic_config):
                    uuid = self.__sim.add_topic(topic_config)
                    self.__add_topic_to_item_list(uuid)
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

    def __add_topic_to_item_list(self, topic_uuid: str) -> None:
        topic_name = self.__config.get_topic_data(topic_uuid).get("topic")
        topic_widget = MqttSimTopicWidget(topic_name)

        def on_remove_btn_clicked() -> None:
            result = QMessageBox.question(
                self,
                "Remove topic?",
                f'Are you sure you want to remove topic {self.__config.get_topic_data(topic_uuid).get("topic")} [uuid={topic_uuid}]?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if result == QMessageBox.StandardButton.Yes:
                self.__sim.remove_topic(topic_uuid)
                topic_widget.deleteLater()

        def on_edit_btn_clicked() -> None:
            data = self.__config.get_topic_data(topic_uuid)
            if "data_format" in data.keys():
                edit_topic_window = MqttSimEditTopicWindow(data)
                if edit_topic_window.exec():
                    edited_data = {
                        "topic": edit_topic_window.name_line_edit.text(),
                        "data_format": edit_topic_window.format_text_edit.toPlainText(),
                        "interval": edit_topic_window.interval_spin_box.value(),
                        "manual": edit_topic_window.manual_check_box.isChecked(),
                    }
                    if edited_data != data:
                        topic_widget.set_topic_name(edited_data.get("topic"))
                        self.__sim.edit(topic_uuid, edited_data)
                        self.__logger.info(
                            f'Edited topic {data.get("topic")} [uuid={topic_uuid}] ({data} -> {edited_data}).'
                        )
            else:
                edit_topic_window = MqttSimEditProtoTopicWindow(
                    topic_name, data)
                if edit_topic_window.exec():
                    edited_topic_data = {
                        "topic": edit_topic_window.name_line_edit.text(),
                        "message": edit_topic_window.message_list.currentItem().text(),
                        "interval": edit_topic_window.interval_spin_box.value(),
                        "manual": edit_topic_window.manual_check_box.isChecked(),
                        "file": edit_topic_window.file_line_edit.text()
                    }
                    if edited_topic_data != data:
                        self.__sim.edit(topic_uuid, edited_topic_data)
                        self.__logger.info(
                            f'Edited topic {data.get("topic")} [uuid={topic_uuid}] ({data} -> {edited_topic_data}).'
                        )

        topic_widget.remove_btn.clicked.connect(on_remove_btn_clicked)
        topic_widget.edit_btn.clicked.connect(on_edit_btn_clicked)
        topic_widget.send_now_btn.clicked.connect(
            partial(self.__sim.send_single_message, topic_uuid)
        )

        self.topics_list.insertWidget(0, topic_widget)

    def __set_values_from_config(self) -> None:
        def set_values_from_config_broker() -> None:
            hostname, port, *_ = self.__config.get_broker()
            self.broker_hostname.setText(hostname)
            self.broker_port.setValue(port)

        def set_values_from_config_topics() -> None:
            topics = self.__config.get_topics()
            for topic_uuid in topics.keys():
                self.__add_topic_to_item_list(topic_uuid)

        set_values_from_config_broker()
        set_values_from_config_topics()

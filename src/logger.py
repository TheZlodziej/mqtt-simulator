from datetime import datetime
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QListWidgetItem
from logging import Handler


class QListWidgetLogHandler(Handler):
    def __init__(self, logs_list):
        super().__init__()
        self.__logs_list = logs_list

    def emit(self, record):
        try:
            current_time = datetime.now().strftime("%H:%M:%S")
            log_message = QCoreApplication.translate("MainWindow", f"[{current_time}] {record.getMessage()}", None)
            log_item = QListWidgetItem(log_message)
            self.__logs_list.insertItem(0, log_item)

            # limit the number of logs displayed in gui
            max_number_of_logs_gui = 50
            while self.__logs_list.count() > max_number_of_logs_gui:
                self.__logs_list.takeItem(self.__logs_list.count() - 1)

        except Exception:
            self.handleError(record)

import datetime
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QListWidgetItem
import logging


class QListWidgetLogHandler(logging.Handler):
    def __init__(self, logs_list):
        super().__init__()
        self.logs_list = logs_list

    def emit(self, record):
        try:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            log_message = QCoreApplication.translate("MainWindow", f"[{current_time}] {record.getMessage()}", None)
            log_item = QListWidgetItem(log_message)
            self.logs_list.addItem(log_item)
        except Exception:
            self.handleError(record)

from PySide6.QtWidgets import QApplication
from gui.ui import MqttSimMainWindow
from mqttsim import MqttSimConfig, MqttSim
from logger import QListWidgetLogHandler
import logging

app = QApplication()
sim = MqttSim(MqttSimConfig("config.json"))
window = MqttSimMainWindow(sim)

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.DEBUG)
log_handler = QListWidgetLogHandler(window.logs_list)
file_handler = logging.FileHandler("logs.txt")
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(log_handler)
logger.addHandler(file_handler)

sim.logger = logger
window.logger = logger
window.show()
app.exec()

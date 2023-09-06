from PySide6.QtWidgets import QApplication
from gui.ui import MqttSimMainWindow
from mqttsim import MqttSimConfig, MqttSim
from logging import getLogger, Formatter, FileHandler, DEBUG

app = QApplication()
logger = getLogger("MyLogger")
sim = MqttSim(MqttSimConfig("config.json"), logger)
window = MqttSimMainWindow(sim, logger)

logger.setLevel(DEBUG)
file_handler = FileHandler("logs.txt")
file_formatter = Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


window.show()
app.exec()

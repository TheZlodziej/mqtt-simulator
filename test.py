from PySide6.QtWidgets import QApplication
from gui.ui import MqttSimMainWindow
from mqttsim import MqttSimConfig, MqttSim

app = QApplication()
sim = MqttSim(MqttSimConfig("config.json"))
window = MqttSimMainWindow(sim)
window.show()
app.exec()

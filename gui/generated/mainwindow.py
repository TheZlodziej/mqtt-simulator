# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_hlayout = QHBoxLayout()
        self.main_hlayout.setObjectName(u"main_hlayout")
        self.main_hlayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.main_hlayout.setContentsMargins(10, 10, 10, 10)
        self.left_vlayout = QVBoxLayout()
        self.left_vlayout.setObjectName(u"left_vlayout")
        self.broker_info_vlayout = QHBoxLayout()
        self.broker_info_vlayout.setObjectName(u"broker_info_vlayout")
        self.broker_lbl = QLabel(self.centralwidget)
        self.broker_lbl.setObjectName(u"broker_lbl")

        self.broker_info_vlayout.addWidget(self.broker_lbl)

        self.broker_hostname = QLineEdit(self.centralwidget)
        self.broker_hostname.setObjectName(u"broker_hostname")

        self.broker_info_vlayout.addWidget(self.broker_hostname)

        self.broker_port = QSpinBox(self.centralwidget)
        self.broker_port.setObjectName(u"broker_port")
        self.broker_port.setMaximum(65535)
        self.broker_port.setValue(1883)

        self.broker_info_vlayout.addWidget(self.broker_port)


        self.left_vlayout.addLayout(self.broker_info_vlayout)

        self.broker_connect_btn = QPushButton(self.centralwidget)
        self.broker_connect_btn.setObjectName(u"broker_connect_btn")
        self.broker_connect_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.left_vlayout.addWidget(self.broker_connect_btn, 0, Qt.AlignRight)

        self.broker_line = QFrame(self.centralwidget)
        self.broker_line.setObjectName(u"broker_line")
        self.broker_line.setFrameShape(QFrame.HLine)
        self.broker_line.setFrameShadow(QFrame.Sunken)

        self.left_vlayout.addWidget(self.broker_line)

        self.topics_vlayout = QVBoxLayout()
        self.topics_vlayout.setObjectName(u"topics_vlayout")
        self.topics_vlayout.setContentsMargins(-1, -1, -1, 1)
        self.topics_hlayout = QHBoxLayout()
        self.topics_hlayout.setObjectName(u"topics_hlayout")
        self.topics_lbl = QLabel(self.centralwidget)
        self.topics_lbl.setObjectName(u"topics_lbl")

        self.topics_hlayout.addWidget(self.topics_lbl)

        self.add_topic_btn = QPushButton(self.centralwidget)
        self.add_topic_btn.setObjectName(u"add_topic_btn")
        self.add_topic_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.topics_hlayout.addWidget(self.add_topic_btn, 0, Qt.AlignRight)

        self.topics_hlayout.setStretch(1, 1)

        self.topics_vlayout.addLayout(self.topics_hlayout)

        self.topics_list_scroll_area = QScrollArea(self.centralwidget)
        self.topics_list_scroll_area.setObjectName(u"topics_list_scroll_area")
        self.topics_list_scroll_area.setWidgetResizable(True)
        self.topics_list_widget = QWidget()
        self.topics_list_widget.setObjectName(u"topics_list_widget")
        self.topics_list_widget.setGeometry(QRect(0, 0, 318, 337))
        self.verticalLayout = QVBoxLayout(self.topics_list_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topics_list = QVBoxLayout()
        self.topics_list.setObjectName(u"topics_list")
        self.topics_list_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.topics_list.addItem(self.topics_list_spacer)


        self.verticalLayout.addLayout(self.topics_list)

        self.topics_list_scroll_area.setWidget(self.topics_list_widget)

        self.topics_vlayout.addWidget(self.topics_list_scroll_area)


        self.left_vlayout.addLayout(self.topics_vlayout)


        self.main_hlayout.addLayout(self.left_vlayout)

        self.center_line = QFrame(self.centralwidget)
        self.center_line.setObjectName(u"center_line")
        self.center_line.setFrameShape(QFrame.VLine)
        self.center_line.setFrameShadow(QFrame.Sunken)

        self.main_hlayout.addWidget(self.center_line)

        self.logs_vlayout = QVBoxLayout()
        self.logs_vlayout.setObjectName(u"logs_vlayout")
        self.logs_lbl = QLabel(self.centralwidget)
        self.logs_lbl.setObjectName(u"logs_lbl")

        self.logs_vlayout.addWidget(self.logs_lbl)

        self.logs_list = QListWidget(self.centralwidget)
        self.logs_list.setObjectName(u"logs_list")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(10)
        self.logs_list.setFont(font1)
        self.logs_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.logs_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.logs_list.setTextElideMode(Qt.ElideNone)
        self.logs_list.setProperty("isWrapping", False)
        self.logs_list.setUniformItemSizes(False)
        self.logs_list.setWordWrap(True)
        self.logs_list.setSortingEnabled(False)

        self.logs_vlayout.addWidget(self.logs_list)

        self.clear_logs_btn = QPushButton(self.centralwidget)
        self.clear_logs_btn.setObjectName(u"clear_logs_btn")
        self.clear_logs_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.logs_vlayout.addWidget(self.clear_logs_btn, 0, Qt.AlignRight)


        self.main_hlayout.addLayout(self.logs_vlayout)

        self.main_hlayout.setStretch(0, 1)
        self.main_hlayout.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.main_hlayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MQTT flow simulator", None))
        self.broker_lbl.setText(QCoreApplication.translate("MainWindow", u"Broker", None))
#if QT_CONFIG(tooltip)
        self.broker_hostname.setToolTip(QCoreApplication.translate("MainWindow", u"Broker hostname", None))
#endif // QT_CONFIG(tooltip)
        self.broker_hostname.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.broker_hostname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"hostname", None))
#if QT_CONFIG(tooltip)
        self.broker_port.setToolTip(QCoreApplication.translate("MainWindow", u"Broker port (1-65535)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.broker_connect_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Connect to broker", None))
#endif // QT_CONFIG(tooltip)
        self.broker_connect_btn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.topics_lbl.setText(QCoreApplication.translate("MainWindow", u"Topics", None))
#if QT_CONFIG(tooltip)
        self.add_topic_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Add topic", None))
#endif // QT_CONFIG(tooltip)
        self.add_topic_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.logs_lbl.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
#if QT_CONFIG(tooltip)
        self.clear_logs_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Clear logs", None))
#endif // QT_CONFIG(tooltip)
        self.clear_logs_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choosetopicdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_ChooseTopicDialog(object):
    def setupUi(self, ChooseTopicDialog):
        if not ChooseTopicDialog.objectName():
            ChooseTopicDialog.setObjectName(u"ChooseTopicDialog")
        ChooseTopicDialog.resize(319, 153)
        self.horizontalLayoutWidget = QWidget(ChooseTopicDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 19, 291, 121))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.choose_proto_button = QPushButton(self.horizontalLayoutWidget)
        self.choose_proto_button.setObjectName(u"choose_proto_button")

        self.horizontalLayout.addWidget(self.choose_proto_button)

        self.choose_json_button = QPushButton(self.horizontalLayoutWidget)
        self.choose_json_button.setObjectName(u"choose_json_button")

        self.horizontalLayout.addWidget(self.choose_json_button)


        self.retranslateUi(ChooseTopicDialog)

        QMetaObject.connectSlotsByName(ChooseTopicDialog)
    # setupUi

    def retranslateUi(self, ChooseTopicDialog):
        ChooseTopicDialog.setWindowTitle(QCoreApplication.translate("ChooseTopicDialog", u"Choose message type", None))
        self.choose_proto_button.setText(QCoreApplication.translate("ChooseTopicDialog", u"Protobuf", None))
        self.choose_json_button.setText(QCoreApplication.translate("ChooseTopicDialog", u"JSON", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addtopicdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QLabel,
    QLineEdit, QPlainTextEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AddTopicDialog(object):
    def setupUi(self, AddTopicDialog):
        if not AddTopicDialog.objectName():
            AddTopicDialog.setObjectName(u"AddTopicDialog")
        AddTopicDialog.resize(399, 224)
        font = QFont()
        font.setPointSize(12)
        AddTopicDialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(AddTopicDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AddTopicDialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.name_lbl = QLabel(AddTopicDialog)
        self.name_lbl.setObjectName(u"name_lbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_lbl)

        self.format_lbl = QLabel(AddTopicDialog)
        self.format_lbl.setObjectName(u"format_lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.format_lbl)

        self.interval_lbl = QLabel(AddTopicDialog)
        self.interval_lbl.setObjectName(u"interval_lbl")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.interval_lbl)

        self.interval_spin_box = QDoubleSpinBox(AddTopicDialog)
        self.interval_spin_box.setObjectName(u"interval_spin_box")
        self.interval_spin_box.setMinimum(0.100000000000000)
        self.interval_spin_box.setMaximum(60.000000000000000)
        self.interval_spin_box.setSingleStep(0.500000000000000)
        self.interval_spin_box.setValue(1.500000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.interval_spin_box)

        self.name_line_edit = QLineEdit(AddTopicDialog)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_line_edit)

        self.manual_check_box = QCheckBox(AddTopicDialog)
        self.manual_check_box.setObjectName(u"manual_check_box")
        self.manual_check_box.setChecked(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.manual_check_box)

        self.manual_lbl = QLabel(AddTopicDialog)
        self.manual_lbl.setObjectName(u"manual_lbl")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.manual_lbl)

        self.format_text_edit = QPlainTextEdit(AddTopicDialog)
        self.format_text_edit.setObjectName(u"format_text_edit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.format_text_edit)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(AddTopicDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(AddTopicDialog)
        self.buttonBox.accepted.connect(AddTopicDialog.accept)
        self.buttonBox.rejected.connect(AddTopicDialog.reject)

        QMetaObject.connectSlotsByName(AddTopicDialog)
    # setupUi

    def retranslateUi(self, AddTopicDialog):
        AddTopicDialog.setWindowTitle(QCoreApplication.translate("AddTopicDialog", u"Add topic", None))
        self.label.setText(QCoreApplication.translate("AddTopicDialog", u"Add topic", None))
        self.name_lbl.setText(QCoreApplication.translate("AddTopicDialog", u"Name", None))
        self.format_lbl.setText(QCoreApplication.translate("AddTopicDialog", u"Format", None))
        self.interval_lbl.setText(QCoreApplication.translate("AddTopicDialog", u"Interval (seconds)", None))
#if QT_CONFIG(tooltip)
        self.interval_spin_box.setToolTip(QCoreApplication.translate("AddTopicDialog", u"Interval of incoming data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.name_line_edit.setToolTip(QCoreApplication.translate("AddTopicDialog", u"Name of topic", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.manual_check_box.setToolTip(QCoreApplication.translate("AddTopicDialog", u"If checked, the data will be automatically send every <interval> seconds", None))
#endif // QT_CONFIG(tooltip)
        self.manual_check_box.setText("")
        self.manual_lbl.setText(QCoreApplication.translate("AddTopicDialog", u"Manual", None))
        self.format_text_edit.setPlainText(QCoreApplication.translate("AddTopicDialog", u"{ 'data': <%randi%> }", None))
    # retranslateUi


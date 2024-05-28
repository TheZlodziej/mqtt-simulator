# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addprototopicdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QLineEdit, QListWidget, QListWidgetItem, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_AddProtoTopicDialog(object):
    def setupUi(self, AddProtoTopicDialog):
        if not AddProtoTopicDialog.objectName():
            AddProtoTopicDialog.setObjectName(u"AddProtoTopicDialog")
        AddProtoTopicDialog.resize(457, 337)
        font = QFont()
        font.setPointSize(12)
        AddProtoTopicDialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(AddProtoTopicDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AddProtoTopicDialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignTop)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.name_lbl = QLabel(AddProtoTopicDialog)
        self.name_lbl.setObjectName(u"name_lbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_lbl)

        self.name_line_edit = QLineEdit(AddProtoTopicDialog)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_line_edit)

        self.format_lbl = QLabel(AddProtoTopicDialog)
        self.format_lbl.setObjectName(u"format_lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.format_lbl)

        self.message_list = QListWidget(AddProtoTopicDialog)
        self.message_list.setObjectName(u"message_list")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.message_list)

        self.interval_lbl = QLabel(AddProtoTopicDialog)
        self.interval_lbl.setObjectName(u"interval_lbl")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.interval_lbl)

        self.interval_spin_box = QDoubleSpinBox(AddProtoTopicDialog)
        self.interval_spin_box.setObjectName(u"interval_spin_box")
        self.interval_spin_box.setMinimum(0.100000000000000)
        self.interval_spin_box.setMaximum(60.000000000000000)
        self.interval_spin_box.setSingleStep(0.500000000000000)
        self.interval_spin_box.setValue(1.500000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.interval_spin_box)

        self.manual_lbl = QLabel(AddProtoTopicDialog)
        self.manual_lbl.setObjectName(u"manual_lbl")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.manual_lbl)

        self.manual_check_box = QCheckBox(AddProtoTopicDialog)
        self.manual_check_box.setObjectName(u"manual_check_box")
        self.manual_check_box.setChecked(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.manual_check_box)

        self.file_line_edit = QLineEdit(AddProtoTopicDialog)
        self.file_line_edit.setObjectName(u"file_line_edit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.file_line_edit)

        self.path_label = QLabel(AddProtoTopicDialog)
        self.path_label.setObjectName(u"path_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.path_label)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(AddProtoTopicDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(AddProtoTopicDialog)
        self.buttonBox.accepted.connect(AddProtoTopicDialog.accept)
        self.buttonBox.rejected.connect(AddProtoTopicDialog.reject)

        QMetaObject.connectSlotsByName(AddProtoTopicDialog)
    # setupUi

    def retranslateUi(self, AddProtoTopicDialog):
        AddProtoTopicDialog.setWindowTitle(QCoreApplication.translate("AddProtoTopicDialog", u"Add topic", None))
        self.label.setText(QCoreApplication.translate("AddProtoTopicDialog", u"Add topic", None))
        self.name_lbl.setText(QCoreApplication.translate("AddProtoTopicDialog", u"Name", None))
#if QT_CONFIG(tooltip)
        self.name_line_edit.setToolTip(QCoreApplication.translate("AddProtoTopicDialog", u"Name of topic", None))
#endif // QT_CONFIG(tooltip)
        self.format_lbl.setText(QCoreApplication.translate("AddProtoTopicDialog", u"Message", None))
        self.interval_lbl.setText(QCoreApplication.translate("AddProtoTopicDialog", u"Interval (seconds)", None))
#if QT_CONFIG(tooltip)
        self.interval_spin_box.setToolTip(QCoreApplication.translate("AddProtoTopicDialog", u"Interval of incoming data", None))
#endif // QT_CONFIG(tooltip)
        self.manual_lbl.setText(QCoreApplication.translate("AddProtoTopicDialog", u"Manual", None))
#if QT_CONFIG(tooltip)
        self.manual_check_box.setToolTip(QCoreApplication.translate("AddProtoTopicDialog", u"If checked, the data will be automatically send every <interval> seconds", None))
#endif // QT_CONFIG(tooltip)
        self.manual_check_box.setText("")
        self.path_label.setText(QCoreApplication.translate("AddProtoTopicDialog", u"File (optional)", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editprototopicdialog.ui'
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
    QLineEdit, QListWidget, QListWidgetItem, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_EditProtoTopicDialog(object):
    def setupUi(self, EditProtoTopicDialog):
        if not EditProtoTopicDialog.objectName():
            EditProtoTopicDialog.setObjectName(u"EditProtoTopicDialog")
        EditProtoTopicDialog.resize(399, 261)
        font = QFont()
        font.setPointSize(12)
        EditProtoTopicDialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(EditProtoTopicDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(EditProtoTopicDialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.name_lbl = QLabel(EditProtoTopicDialog)
        self.name_lbl.setObjectName(u"name_lbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_lbl)

        self.format_lbl = QLabel(EditProtoTopicDialog)
        self.format_lbl.setObjectName(u"format_lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.format_lbl)

        self.interval_lbl = QLabel(EditProtoTopicDialog)
        self.interval_lbl.setObjectName(u"interval_lbl")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.interval_lbl)

        self.interval_spin_box = QDoubleSpinBox(EditProtoTopicDialog)
        self.interval_spin_box.setObjectName(u"interval_spin_box")
        self.interval_spin_box.setMinimum(0.100000000000000)
        self.interval_spin_box.setMaximum(60.000000000000000)
        self.interval_spin_box.setSingleStep(0.500000000000000)
        self.interval_spin_box.setValue(1.500000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.interval_spin_box)

        self.name_line_edit = QLineEdit(EditProtoTopicDialog)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_line_edit)

        self.manual_check_box = QCheckBox(EditProtoTopicDialog)
        self.manual_check_box.setObjectName(u"manual_check_box")
        self.manual_check_box.setChecked(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.manual_check_box)

        self.manual_lbl = QLabel(EditProtoTopicDialog)
        self.manual_lbl.setObjectName(u"manual_lbl")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.manual_lbl)

        self.message_list = QListWidget(EditProtoTopicDialog)
        self.message_list.setObjectName(u"message_list")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.message_list)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(EditProtoTopicDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(EditProtoTopicDialog)
        self.buttonBox.accepted.connect(EditProtoTopicDialog.accept)
        self.buttonBox.rejected.connect(EditProtoTopicDialog.reject)

        QMetaObject.connectSlotsByName(EditProtoTopicDialog)
    # setupUi

    def retranslateUi(self, EditProtoTopicDialog):
        EditProtoTopicDialog.setWindowTitle(QCoreApplication.translate("EditProtoTopicDialog", u"Add topic", None))
        self.label.setText(QCoreApplication.translate("EditProtoTopicDialog", u"Edit topic", None))
        self.name_lbl.setText(QCoreApplication.translate("EditProtoTopicDialog", u"Name", None))
        self.format_lbl.setText(QCoreApplication.translate("EditProtoTopicDialog", u"Message", None))
        self.interval_lbl.setText(QCoreApplication.translate("EditProtoTopicDialog", u"Interval (seconds)", None))
#if QT_CONFIG(tooltip)
        self.interval_spin_box.setToolTip(QCoreApplication.translate("EditProtoTopicDialog", u"Interval of incoming data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.name_line_edit.setToolTip(QCoreApplication.translate("EditProtoTopicDialog", u"Name of topic", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.manual_check_box.setToolTip(QCoreApplication.translate("EditProtoTopicDialog", u"If checked, the data will be automatically send every <interval> seconds", None))
#endif // QT_CONFIG(tooltip)
        self.manual_check_box.setText("")
        self.manual_lbl.setText(QCoreApplication.translate("EditProtoTopicDialog", u"Manual", None))
    # retranslateUi


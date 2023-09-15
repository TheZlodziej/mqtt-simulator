# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edittopicdialog.ui'
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

class Ui_EditTopicDialog(object):
    def setupUi(self, EditTopicDialog):
        if not EditTopicDialog.objectName():
            EditTopicDialog.setObjectName(u"EditTopicDialog")
        EditTopicDialog.resize(399, 216)
        font = QFont()
        font.setPointSize(12)
        EditTopicDialog.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(EditTopicDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(EditTopicDialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.name_lbl = QLabel(EditTopicDialog)
        self.name_lbl.setObjectName(u"name_lbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_lbl)

        self.format_lbl = QLabel(EditTopicDialog)
        self.format_lbl.setObjectName(u"format_lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.format_lbl)

        self.interval_lbl = QLabel(EditTopicDialog)
        self.interval_lbl.setObjectName(u"interval_lbl")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.interval_lbl)

        self.interval_spin_box = QDoubleSpinBox(EditTopicDialog)
        self.interval_spin_box.setObjectName(u"interval_spin_box")
        self.interval_spin_box.setMinimum(0.100000000000000)
        self.interval_spin_box.setMaximum(60.000000000000000)
        self.interval_spin_box.setSingleStep(0.500000000000000)
        self.interval_spin_box.setValue(0.100000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.interval_spin_box)

        self.name_line_edit = QLineEdit(EditTopicDialog)
        self.name_line_edit.setObjectName(u"name_line_edit")
        self.name_line_edit.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_line_edit)

        self.manual_check_box = QCheckBox(EditTopicDialog)
        self.manual_check_box.setObjectName(u"manual_check_box")
        self.manual_check_box.setChecked(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.manual_check_box)

        self.manual_lbl = QLabel(EditTopicDialog)
        self.manual_lbl.setObjectName(u"manual_lbl")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.manual_lbl)

        self.format_text_edit = QPlainTextEdit(EditTopicDialog)
        self.format_text_edit.setObjectName(u"format_text_edit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.format_text_edit)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(EditTopicDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(EditTopicDialog)
        self.buttonBox.accepted.connect(EditTopicDialog.accept)
        self.buttonBox.rejected.connect(EditTopicDialog.reject)

        QMetaObject.connectSlotsByName(EditTopicDialog)
    # setupUi

    def retranslateUi(self, EditTopicDialog):
        EditTopicDialog.setWindowTitle(QCoreApplication.translate("EditTopicDialog", u"Edit topic", None))
        self.label.setText(QCoreApplication.translate("EditTopicDialog", u"Edit topic", None))
        self.name_lbl.setText(QCoreApplication.translate("EditTopicDialog", u"Name", None))
        self.format_lbl.setText(QCoreApplication.translate("EditTopicDialog", u"Format", None))
        self.interval_lbl.setText(QCoreApplication.translate("EditTopicDialog", u"Interval (seconds)", None))
#if QT_CONFIG(tooltip)
        self.interval_spin_box.setToolTip(QCoreApplication.translate("EditTopicDialog", u"Interval of incoming data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.name_line_edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.name_line_edit.setText(QCoreApplication.translate("EditTopicDialog", u"-", None))
#if QT_CONFIG(tooltip)
        self.manual_check_box.setToolTip(QCoreApplication.translate("EditTopicDialog", u"If checked, the data will be automatically send every <interval> seconds", None))
#endif // QT_CONFIG(tooltip)
        self.manual_check_box.setText("")
        self.manual_lbl.setText(QCoreApplication.translate("EditTopicDialog", u"Manual", None))
        self.format_text_edit.setPlainText(QCoreApplication.translate("EditTopicDialog", u"-", None))
    # retranslateUi


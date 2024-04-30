# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addtopicdialog.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AddTopicDialog(object):
    def setupUi(self, AddTopicDialog):
        if not AddTopicDialog.objectName():
            AddTopicDialog.setObjectName(u"AddTopicDialog")
        AddTopicDialog.resize(399, 280)
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

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignTop)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setVerticalSpacing(5)
        self.name_lbl = QLabel(AddTopicDialog)
        self.name_lbl.setObjectName(u"name_lbl")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_lbl)

        self.name_line_edit = QLineEdit(AddTopicDialog)
        self.name_line_edit.setObjectName(u"name_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_line_edit.sizePolicy().hasHeightForWidth())
        self.name_line_edit.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_line_edit)

        self.format_lbl = QLabel(AddTopicDialog)
        self.format_lbl.setObjectName(u"format_lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.format_lbl)

        self.format_vlayout = QVBoxLayout()
        self.format_vlayout.setSpacing(0)
        self.format_vlayout.setObjectName(u"format_vlayout")
        self.format_text_edit = QPlainTextEdit(AddTopicDialog)
        self.format_text_edit.setObjectName(u"format_text_edit")

        self.format_vlayout.addWidget(self.format_text_edit)

        self.format_hlayout = QHBoxLayout()
        self.format_hlayout.setObjectName(u"format_hlayout")
        self.format_hlayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.load_from_file_hspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.format_hlayout.addItem(self.load_from_file_hspacer)

        self.load_from_file_btn = QPushButton(AddTopicDialog)
        self.load_from_file_btn.setObjectName(u"load_from_file_btn")
        self.load_from_file_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.format_hlayout.addWidget(self.load_from_file_btn)


        self.format_vlayout.addLayout(self.format_hlayout)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.format_vlayout)

        self.interval_lbl = QLabel(AddTopicDialog)
        self.interval_lbl.setObjectName(u"interval_lbl")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.interval_lbl)

        self.interval_spin_box = QDoubleSpinBox(AddTopicDialog)
        self.interval_spin_box.setObjectName(u"interval_spin_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.interval_spin_box.sizePolicy().hasHeightForWidth())
        self.interval_spin_box.setSizePolicy(sizePolicy1)
        self.interval_spin_box.setMinimum(0.100000000000000)
        self.interval_spin_box.setMaximum(60.000000000000000)
        self.interval_spin_box.setSingleStep(0.500000000000000)
        self.interval_spin_box.setValue(1.500000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.interval_spin_box)

        self.manual_lbl = QLabel(AddTopicDialog)
        self.manual_lbl.setObjectName(u"manual_lbl")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.manual_lbl)

        self.manual_check_box = QCheckBox(AddTopicDialog)
        self.manual_check_box.setObjectName(u"manual_check_box")
        self.manual_check_box.setChecked(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.manual_check_box)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(AddTopicDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

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
#if QT_CONFIG(tooltip)
        self.name_line_edit.setToolTip(QCoreApplication.translate("AddTopicDialog", u"Name of topic", None))
#endif // QT_CONFIG(tooltip)
        self.format_lbl.setText(QCoreApplication.translate("AddTopicDialog", u"Format", None))
        self.format_text_edit.setPlainText(QCoreApplication.translate("AddTopicDialog", u"{ \"data\": <%randi%> }", None))
        self.load_from_file_btn.setText(QCoreApplication.translate("AddTopicDialog", u"Load from file", None))
        self.interval_lbl.setText(QCoreApplication.translate("AddTopicDialog", u"Interval (seconds)", None))
#if QT_CONFIG(tooltip)
        self.interval_spin_box.setToolTip(QCoreApplication.translate("AddTopicDialog", u"Interval of incoming data", None))
#endif // QT_CONFIG(tooltip)
        self.manual_lbl.setText(QCoreApplication.translate("AddTopicDialog", u"Manual", None))
#if QT_CONFIG(tooltip)
        self.manual_check_box.setToolTip(QCoreApplication.translate("AddTopicDialog", u"If checked, the data will be automatically send every <interval> seconds", None))
#endif // QT_CONFIG(tooltip)
        self.manual_check_box.setText("")
    # retranslateUi


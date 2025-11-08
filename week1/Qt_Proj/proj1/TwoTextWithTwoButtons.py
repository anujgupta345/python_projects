# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TwoTextWithButtons.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(911, 829)
        self.inputLayoutParentWidget = QWidget(Form)
        self.inputLayoutParentWidget.setObjectName(u"horizontalLayoutWidget")
        self.inputLayoutParentWidget.setGeometry(QRect(170, 140, 531, 80))
        self.inputHLayout = QHBoxLayout(self.inputLayoutParentWidget)
        self.inputHLayout.setObjectName(u"horizontalLayout")
        self.inputHLayout.setContentsMargins(0, 0, 0, 0)
        self.inpulLabel = QLabel(self.inputLayoutParentWidget)
        self.inpulLabel.setObjectName(u"label")

        self.inputHLayout.addWidget(self.inpulLabel)

        self.inputSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.inputHLayout.addItem(self.inputSpacer1)

        self.inputTextEdit = QTextEdit(self.inputLayoutParentWidget)
        self.inputTextEdit.setObjectName(u"inputTextEdit")
        self.inputTextEdit.setMinimumWidth(450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTextEdit.sizePolicy().hasHeightForWidth())
        self.inputTextEdit.setSizePolicy(sizePolicy)

        self.inputHLayout.addWidget(self.inputTextEdit)

        self.responseLayoutParentWidget = QWidget(Form)
        self.responseLayoutParentWidget.setObjectName(u"horizontalLayoutWidget_2")
        self.responseLayoutParentWidget.setGeometry(QRect(170, 260, 531, 80))
        self.responsetHLayout = QHBoxLayout(self.responseLayoutParentWidget)
        self.responsetHLayout.setObjectName(u"horizontalLayout_2")
        self.responsetHLayout.setContentsMargins(0, 0, 0, 0)
        self.responseLabel = QLabel(self.responseLayoutParentWidget)
        self.responseLabel.setObjectName(u"responseLabel")

        self.responsetHLayout.addWidget(self.responseLabel)

        self.responseSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.responsetHLayout.addItem(self.responseSpacer1)

        self.responseTextEdit = QTextEdit(self.responseLayoutParentWidget)
        self.responseTextEdit.setObjectName(u"responseTextEdit")
        self.responseTextEdit.setMinimumWidth(450)
        sizePolicy.setHeightForWidth(self.responseTextEdit.sizePolicy().hasHeightForWidth())
        self.responseTextEdit.setSizePolicy(sizePolicy)
        self.responseTextEdit.setReadOnly(True)

        self.responsetHLayout.addWidget(self.responseTextEdit)

        self.pushButtonsHParentWidget = QWidget(Form)
        self.pushButtonsHParentWidget.setObjectName(u"horizontalLayoutWidget_3")
        self.pushButtonsHParentWidget.setGeometry(QRect(170, 400, 241, 80))
        self.pushButtonsHLayout = QHBoxLayout(self.pushButtonsHParentWidget)
        self.pushButtonsHLayout.setObjectName(u"horizontalLayout_3")
        self.pushButtonsHLayout.setContentsMargins(0, 0, 0, 0)
        self.resetPushButton = QPushButton(self.pushButtonsHParentWidget)
        self.resetPushButton.setObjectName(u"resetPushButton")

        self.pushButtonsHLayout.addWidget(self.resetPushButton)

        self.pushButtonsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.pushButtonsHLayout.addItem(self.pushButtonsSpacer)

        self.okPushButton = QPushButton(self.pushButtonsHParentWidget)
        self.okPushButton.setObjectName(u"okPushButton")

        self.pushButtonsHLayout.addWidget(self.okPushButton)

        self.rolesHLayoutParentWidget = QWidget(Form)
        self.rolesHLayoutParentWidget.setObjectName(u"horizontalLayoutWidget_4")
        self.rolesHLayoutParentWidget.setGeometry(QRect(170, 50, 160, 80))
        self.rolesHLayout = QHBoxLayout(self.rolesHLayoutParentWidget)
        self.rolesHLayout.setObjectName(u"horizontalLayout_4")
        self.rolesHLayout.setContentsMargins(0, 0, 0, 0)
        self.roleLabel = QLabel(self.rolesHLayoutParentWidget)
        self.roleLabel.setObjectName(u"roleLabel")

        self.rolesHLayout.addWidget(self.roleLabel)

        self.rolesSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rolesHLayout.addItem(self.rolesSpacer)

        self.roleComboBox = QComboBox(self.rolesHLayoutParentWidget)
        self.roleComboBox.setObjectName(u"roleComboBox")

        self.rolesHLayout.addWidget(self.roleComboBox)


        self.retranslateUi(Form)

        self.roleComboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.inpulLabel.setText(QCoreApplication.translate("Form", u"Input:", None))
        self.inputTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Input:", None))
        self.responseLabel.setText(QCoreApplication.translate("Form", u"Response", None))
        self.resetPushButton.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.okPushButton.setText(QCoreApplication.translate("Form", u"Ok", None))
        self.roleLabel.setText(QCoreApplication.translate("Form", u"Role: ", None))
        self.roleComboBox.setCurrentText("")
        self.roleComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"Role", None))
    # retranslateUi


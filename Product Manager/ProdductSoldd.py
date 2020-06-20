# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductSold.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class SoldProductWindow(QWidget):
    def setupUi(self, ProductSold):
        ProductSold.setObjectName("ProductSold")
        ProductSold.resize(378, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProductSold.setWindowIcon(icon)
        ProductSold.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ProductSold)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Udemy/icons/shop.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(255, 71,25);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.ConfirmBtn = QtWidgets.QPushButton(self.frame_2)
        self.ConfirmBtn.setMaximumSize(QtCore.QSize(142, 24))
        self.ConfirmBtn.setStyleSheet("background-color: rgb(255, 187, 14);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.ConfirmBtn.setObjectName("ConfirmBtn")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.ConfirmBtn)
        self.ProductText = QtWidgets.QLabel(self.frame_2)
        self.ProductText.setText("")
        self.ProductText.setObjectName("ProductText")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ProductText)
        self.MemberText = QtWidgets.QLabel(self.frame_2)
        self.MemberText.setText("")
        self.MemberText.setObjectName("MemberText")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.MemberText)
        self.AmountText = QtWidgets.QLabel(self.frame_2)
        self.AmountText.setText("")
        self.AmountText.setObjectName("AmountText")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.AmountText)
        self.verticalLayout.addWidget(self.frame_2)
        ProductSold.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProductSold)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 21))
        self.menubar.setObjectName("menubar")
        ProductSold.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProductSold)
        self.statusbar.setObjectName("statusbar")
        ProductSold.setStatusBar(self.statusbar)

        self.retranslateUi(ProductSold)
        QtCore.QMetaObject.connectSlotsByName(ProductSold)

    def retranslateUi(self, ProductSold):
        _translate = QtCore.QCoreApplication.translate
        ProductSold.setWindowTitle(_translate("ProductSold", "Sell Product"))
        self.label.setText(_translate("ProductSold", "SELL PRODUCT"))
        self.label_3.setText(_translate("ProductSold", "Product"))
        self.label_4.setText(_translate("ProductSold", "Member"))
        self.label_5.setText(_translate("ProductSold", "Amount"))
        self.ConfirmBtn.setText(_translate("ProductSold", "Confirm"))


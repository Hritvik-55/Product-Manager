# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddMember.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import os



################SQL#############################
con=sqlite3.connect('Products.db')
cur=con.cursor()
################################################




class Add_Member(QWidget):
    def setupUi(self, AddMemberWindow):
        AddMemberWindow.setObjectName("AddMemberWindow")
        AddMemberWindow.resize(327, 469)
        AddMemberWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddMemberWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Udemy/icons/addmember.png"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(300, 150))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_2.setStyleSheet("background-color: rgb(255, 71,25);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("background-color: rgb(255, 71,25);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("background-color: rgb(255, 71,25);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet("background-color: rgb(255, 71,25);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.Name = QtWidgets.QLineEdit(self.frame_2)
        self.Name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Mistral\";")
        self.Name.setText("")
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.Surname = QtWidgets.QLineEdit(self.frame_2)
        self.Surname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Mistral\";")
        self.Surname.setText("")
        self.Surname.setObjectName("Surname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Surname)
        self.Phone = QtWidgets.QLineEdit(self.frame_2)
        self.Phone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Mistral\";")
        self.Phone.setText("")
        self.Phone.setObjectName("Phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Phone)
        self.Submit = QtWidgets.QPushButton(self.frame_2)
        self.Submit.setStyleSheet("background-color: rgb(255, 187, 14);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.Submit.setObjectName("Submit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Submit)
        self.verticalLayout.addWidget(self.frame_2)
        AddMemberWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddMemberWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 327, 21))
        self.menubar.setObjectName("menubar")
        AddMemberWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddMemberWindow)
        self.statusbar.setObjectName("statusbar")
        AddMemberWindow.setStatusBar(self.statusbar)
        ############################################################
        self.Submit.clicked.connect(self.AddNewMember)
        ############################################################

        self.retranslateUi(AddMemberWindow)
        QtCore.QMetaObject.connectSlotsByName(AddMemberWindow)

    def AddNewMember(self):
        query="INSERT INTO Members (Member_Name,Member_Surname,Member_Phone) VALUES (?,?,?)"
        Name=self.Name.text()
        Surname=self.Surname.text()
        Phone=self.Phone.text()
        if (Name and Surname and Phone !=""):
            try:
                cur.execute(query,(Name,Surname,Phone))
                con.commit()
                QMessageBox.information(self,"Successful","New Member Added")
            except:
                QMessageBox.information(self,"Warning","Something Went Wrong \n Member Can't Be Added")
        else:
            QMessageBox.information(self,"Warning","Fill All The Fields")

    def retranslateUi(self, AddMemberWindow):
        _translate = QtCore.QCoreApplication.translate
        AddMemberWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "ADD MEMBER"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Surname"))
        self.label_3.setText(_translate("MainWindow", "Phone"))
        self.Submit.setText(_translate("MainWindow", "Submit"))



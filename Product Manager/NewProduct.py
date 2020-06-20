# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddProduct.ui'
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

from PIL import Image
defaultimg="Images/image-not-available.jpg"




################SQL#############################
con=sqlite3.connect('Products.db')
cur=con.cursor()
################################################




class Add_Product(QWidget):
    def setupUi(self, addproductwindow):
        addproductwindow.setObjectName("addproductwindow")
        addproductwindow.resize(344, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/add_product.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addproductwindow.setWindowIcon(icon)
        addproductwindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(addproductwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/addproduct.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(255, 241, 37);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Name = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.Manufacturer = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Manufacturer.setFont(font)
        self.Manufacturer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Manufacturer.setObjectName("Manufacturer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Manufacturer)
        self.Price = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Price.setFont(font)
        self.Price.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Price.setObjectName("Price")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Price)
        self.Quota = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Quota.setFont(font)
        self.Quota.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Quota.setObjectName("Quota")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Quota)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.UploadBtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UploadBtn.sizePolicy().hasHeightForWidth())
        self.UploadBtn.setSizePolicy(sizePolicy)
        self.UploadBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.UploadBtn.setFont(font)
        self.UploadBtn.setStyleSheet("background-color: rgb(255, 146, 57);\n"
"background-color: rgb(255, 133, 34);")
        self.UploadBtn.setObjectName("UploadBtn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.UploadBtn)
        self.SubmitBtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubmitBtn.sizePolicy().hasHeightForWidth())
        self.SubmitBtn.setSizePolicy(sizePolicy)
        self.SubmitBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SubmitBtn.setFont(font)
        self.SubmitBtn.setStyleSheet("background-color: rgb(255, 151, 33);")
        self.SubmitBtn.setObjectName("SubmitBtn")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.SubmitBtn)
        self.verticalLayout.addWidget(self.frame_2)
        addproductwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addproductwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 344, 21))
        self.menubar.setObjectName("menubar")
        addproductwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addproductwindow)
        self.statusbar.setObjectName("statusbar")
        addproductwindow.setStatusBar(self.statusbar)
        addproductwindow.setWindowIcon(QIcon("Icons/icon"))
        #####################################################################
        self.UploadBtn.clicked.connect(self.UploadImg)
        self.SubmitBtn.clicked.connect(self.saveRecord)
        #####################################################################


        self.retranslateUi(addproductwindow)
        QtCore.QMetaObject.connectSlotsByName(addproductwindow)

    def UploadImg(self):
        global defaultimg
        size = (300, 200)
        self.filename, ok = QFileDialog.getOpenFileName(self, 'Upload Image', ' ', 'Image Files (*.jpg *.png)')
        if ok:
            print(self.filename)
            defaultimg = os.path.basename(self.filename)
            print(defaultimg)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("Images/{0}".format(defaultimg))

    def saveRecord(self):
        global defaultimg
        query="INSERT INTO Products (Product_Name,Product_Manufacturer,Product_Price,Product_Quota,Product_Image) VALUES (?,?,?,?,?)"
        Name=self.Name.text()
        Manufacturer=self.Manufacturer.text()
        Price=self.Price.text()
        Quota=self.Quota.text()
        Image=defaultimg
        if (Name and Manufacturer and Price !=" "):
            try:
                cur.execute(query,(Name,Manufacturer,Price,Quota,Image))
                con.commit()
                QMessageBox.information(self,"Successful","Product Successfully Added")
                self.close()



            except:
                QMessageBox.information(self,"Warning","Something Went Wrong")
        else:
            QMessageBox.information(self,"Warning","Fields Can't Be Empty")




    def retranslateUi(self, addproductwindow):
        _translate = QtCore.QCoreApplication.translate
        addproductwindow.setWindowTitle(_translate("MainWindow", "Add Product"))
        self.label_3.setText(_translate("MainWindow", "ADD Product"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "Manufacturer:"))
        self.label_6.setText(_translate("MainWindow", "Price:"))
        self.label_7.setText(_translate("MainWindow", "Quota:"))
        self.label_5.setText(_translate("MainWindow", "Image"))
        self.UploadBtn.setText(_translate("MainWindow", "Upload"))
        self.SubmitBtn.setText(_translate("MainWindow", "Submit"))




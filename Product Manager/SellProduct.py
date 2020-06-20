# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SellProduct.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

con=sqlite3.connect('Products.db')
cur=con.cursor()
productName=()
productid=()
membername=()
memberid=()
quantity=0



class SellProductWindow(QWidget):
    def setupUi(self, SellProduct):
        SellProduct.setObjectName("SellProduct")
        SellProduct.resize(378, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SellProduct.setWindowIcon(icon)
        SellProduct.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(SellProduct)
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
        self.ProductCombo = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProductCombo.sizePolicy().hasHeightForWidth())
        self.ProductCombo.setSizePolicy(sizePolicy)
        self.ProductCombo.setMaximumSize(QtCore.QSize(142, 24))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ProductCombo.setFont(font)
        self.ProductCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ProductCombo.setObjectName("ProductCombo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ProductCombo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.MemberCombo = QtWidgets.QComboBox(self.frame_2)
        self.MemberCombo.setMaximumSize(QtCore.QSize(142, 24))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.MemberCombo.setFont(font)
        self.MemberCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MemberCombo.setObjectName("MemberCombo")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.MemberCombo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.QuantityCombo = QtWidgets.QComboBox(self.frame_2)
        self.QuantityCombo.setMaximumSize(QtCore.QSize(142, 24))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic Fixed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.QuantityCombo.setFont(font)
        self.QuantityCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.QuantityCombo.setObjectName("QuantityCombo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.QuantityCombo)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.SellBtn = QtWidgets.QPushButton(self.frame_2)
        self.SellBtn.setMaximumSize(QtCore.QSize(142, 24))
        self.SellBtn.setStyleSheet("background-color: rgb(255, 187, 14);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.SellBtn.setObjectName("SellBtn")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.SellBtn)
        self.verticalLayout.addWidget(self.frame_2)
        SellProduct.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SellProduct)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 21))
        self.menubar.setObjectName("menubar")
        SellProduct.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SellProduct)
        self.statusbar.setObjectName("statusbar")
        SellProduct.setStatusBar(self.statusbar)


        ####################################################################
        self.ProductCombo.currentIndexChanged.connect(self.ChangeQuantity)
        self.SellBtn.clicked.connect(self.ProductSold)
        self.closeWindow=SellProduct
        query1="SELECT * FROM Products WHERE Product_Availability='Available'"
        products=cur.execute(query1).fetchall()

        query2="SELECT Member_ID,Member_Name FROM Members"
        members=cur.execute(query2).fetchall()
        quantity = products[0][4]

        for product in products:
            self.ProductCombo.addItem(product[1],product[0])
        for member in members:
            self.MemberCombo.addItem(member[1],member[0])
        for i in range(1,quantity+1):
            self.QuantityCombo.addItem(str(i))

        ####################################################################

        self.retranslateUi(SellProduct)
        QtCore.QMetaObject.connectSlotsByName(SellProduct)

    def ProductSold(self):
        global productName,productid,membername,memberid,quantity
        productName=self.ProductCombo.currentText()
        productid=self.ProductCombo.currentData()
        membername=self.MemberCombo.currentText()
        memberid=self.MemberCombo.currentData()
        quantity=int(self.QuantityCombo.currentText())
        self.closeWindow.close()






        self.ProductSold = QtWidgets.QMainWindow()
        self.ui = SoldProductWindow()
        self.ui.setupUi(self.ProductSold)
        self.ProductSold.show()



    def ChangeQuantity(self):
        self.QuantityCombo.clear()
        productid=self.ProductCombo.currentData()
        query="SELECT Product_Quota FROM Products WHERE Product_ID=?"
        quota=cur.execute(query,(productid,)).fetchone()
        for i in range(1,quota[0]+1):
            self.QuantityCombo.addItem(str(i))

    def retranslateUi(self, SellProduct):
        _translate = QtCore.QCoreApplication.translate
        SellProduct.setWindowTitle(_translate("SellProduct", "Sell Product"))
        self.label.setText(_translate("SellProduct", "SELL PRODUCT"))
        self.label_3.setText(_translate("SellProduct", "Product"))
        self.label_4.setText(_translate("SellProduct", "Member"))
        self.label_5.setText(_translate("SellProduct", "Quantity"))
        self.SellBtn.setText(_translate("SellProduct", "Sell"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductSold.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys


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
        #####################################################################
        global  productName,productid,membername,memberid,quantity
        self.ProductText.setText(productName)
        self.MemberText.setText(membername)
        query="SELECT Product_Price FROM Products WHERE Product_ID=?"
        price=cur.execute(query,(productid,)).fetchone()
        price=price[0]
        self.amount=price*quantity

        self.AmountText.setText(str(price) + "x" + str(quantity) + "=" + str(self.amount))
        self.ConfirmBtn.clicked.connect(self.ConfirmSell)
        #####################################################################

    def ConfirmSell(self):
        global productid,productName,membername,memberid,quantity
        try:
            query = "INSERT INTO 'Selling_Product' (Selling_Product_ID,Selling_Member_ID,Selling_Quantity,Selling_Amount) VALUES (?,?,?,?)"
            cur.execute(query, (productid, memberid, quantity, self.amount))
            query1 = "SELECT Product_Quota FROM Products WHERE Product_ID=?"
            self.quota = cur.execute(query1, (productid,)).fetchone()
            print(self.quota[0])
            con.commit()

            if (quantity == self.quota[0]):
                query2 = "UPDATE Products SET Product_Quota=?,Product_Availability=? WHERE Product_ID=?"
                cur.execute(query2, (0, "Unavialable", productid))
                con.commit()
            else:
                availablequota = self.quota[0] - quantity
                print(availablequota)
                query3 = "UPDATE Products SET Product_Quota=? WHERE Product_ID=?"
                cur.execute(query3, (availablequota, productid))
                con.commit()
            QMessageBox.information(self, "Product Manager", "Product Sold")
        except:
            QMessageBox.warning(self, "Product Manager", "Something Went Wrong")
















    def retranslateUi(self, ProductSold):
        _translate = QtCore.QCoreApplication.translate
        ProductSold.setWindowTitle(_translate("ProductSold", "Sell Product"))
        self.label.setText(_translate("ProductSold", "SELL PRODUCT"))
        self.label_3.setText(_translate("ProductSold", "Product"))
        self.label_4.setText(_translate("ProductSold", "Member"))
        self.label_5.setText(_translate("ProductSold", "Amount"))
        self.ConfirmBtn.setText(_translate("ProductSold", "Confirm"))





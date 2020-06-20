# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
import NewProduct
import AddMember
import SellProduct
productid=0
memberid=0

from PIL import Image








con=sqlite3.connect('Products.db')
cur=con.cursor()





class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 521)
        MainWindow.setMinimumSize(QtCore.QSize(900, 400))
        MainWindow.setMaximumSize(QtCore.QSize(900, 521))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/product.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 840, 450))
        self.tabWidget.setMinimumSize(QtCore.QSize(900, 400))
        self.tabWidget.setMaximumSize(QtCore.QSize(900, 521))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.blockSignals(True)
        self.tabWidget.currentChanged.connect(self.UpdateTab)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMinimumSize(QtCore.QSize(500,400))
        self.frame_2.setMaximumSize(QtCore.QSize(500,400))

        self.table1 = QtWidgets.QTableWidget(self.frame_2)
        self.table1.setGeometry(QtCore.QRect(-5, 1, 411, 401))
        self.table1.setObjectName("table1")
        self.table1.setColumnCount(0)
        self.table1.setRowCount(0)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QtCore.QSize(400,400))
        self.frame.setMaximumSize(QtCore.QSize(400,400))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SearchBox = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SearchBox.setFont(font)
        self.SearchBox.setObjectName("SearchBox")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SearchBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.SearchBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.SearchBoxText = QtWidgets.QLineEdit(self.SearchBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchBoxText.sizePolicy().hasHeightForWidth())
        self.SearchBoxText.setSizePolicy(sizePolicy)
        self.SearchBoxText.setObjectName("SearchBoxText")
        self.horizontalLayout_2.addWidget(self.SearchBoxText)
        self.SearchBoxGo = QtWidgets.QPushButton(self.SearchBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchBoxGo.sizePolicy().hasHeightForWidth())
        self.SearchBoxGo.setSizePolicy(sizePolicy)
        self.SearchBoxGo.setObjectName("SearchBoxGo")
        self.horizontalLayout_2.addWidget(self.SearchBoxGo)
        self.verticalLayout.addWidget(self.SearchBox)
        self.ListBox = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ListBox.setFont(font)
        self.ListBox.setObjectName("ListBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ListBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.AllProductsRadio = QtWidgets.QRadioButton(self.ListBox)
        self.AllProductsRadio.setObjectName("AllProductsRadio")
        self.horizontalLayout_3.addWidget(self.AllProductsRadio)
        self.AvailableRadio = QtWidgets.QRadioButton(self.ListBox)
        self.AvailableRadio.setObjectName("AvailableRadio")
        self.horizontalLayout_3.addWidget(self.AvailableRadio)
        self.OutOfStockRadio = QtWidgets.QRadioButton(self.ListBox)
        self.OutOfStockRadio.setObjectName("OutOfStockRadio")
        self.horizontalLayout_3.addWidget(self.OutOfStockRadio)
        self.ListBtn = QtWidgets.QPushButton(self.ListBox)
        self.ListBtn.setObjectName("ListBtn")
        self.horizontalLayout_3.addWidget(self.ListBtn)
        self.verticalLayout.addWidget(self.ListBox)
        self.EmptyFrame = QtWidgets.QFrame(self.frame)
        self.EmptyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EmptyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EmptyFrame.setObjectName("EmptyFrame")
        self.verticalLayout.addWidget(self.EmptyFrame)
        self.horizontalLayout.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.tab_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.table2 = QtWidgets.QTableWidget(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table2.sizePolicy().hasHeightForWidth())
        self.table2.setSizePolicy(sizePolicy)
        self.table2.setObjectName("table2")
        self.table2.setColumnCount(0)
        self.table2.setRowCount(0)
        self.horizontalLayout_5.addWidget(self.table2)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.SearcMembersBox = QtWidgets.QGroupBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SearcMembersBox.setFont(font)
        self.SearcMembersBox.setObjectName("SearcMembersBox")
        self.gridLayout = QtWidgets.QGridLayout(self.SearcMembersBox)
        self.gridLayout.setObjectName("gridLayout")
        self.SearchBtn = QtWidgets.QPushButton(self.SearcMembersBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SearchBtn.setFont(font)
        self.SearchBtn.setObjectName("SearchBtn")
        self.gridLayout.addWidget(self.SearchBtn, 0, 2, 1, 1)
        self.SearchMemberText = QtWidgets.QLineEdit(self.SearcMembersBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchMemberText.sizePolicy().hasHeightForWidth())
        self.SearchMemberText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SearchMemberText.setFont(font)
        self.SearchMemberText.setObjectName("SearchMemberText")
        self.gridLayout.addWidget(self.SearchMemberText, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.SearcMembersBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 2, 1)
        self.horizontalLayout_6.addWidget(self.SearcMembersBox)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.StatsBox = QtWidgets.QGroupBox(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.StatsBox.setFont(font)
        self.StatsBox.setObjectName("StatsBox")
        self.formLayout = QtWidgets.QFormLayout(self.StatsBox)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.StatsBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.TotalProducts = QtWidgets.QLabel(self.StatsBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalProducts.setFont(font)
        self.TotalProducts.setText("")
        self.TotalProducts.setObjectName("TotalProducts")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.TotalProducts)
        self.label_5 = QtWidgets.QLabel(self.StatsBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.TotalMembers = QtWidgets.QLabel(self.StatsBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalMembers.setFont(font)
        self.TotalMembers.setText("")
        self.TotalMembers.setObjectName("TotalMembers")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TotalMembers)
        self.label_7 = QtWidgets.QLabel(self.StatsBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.SoldProducts = QtWidgets.QLabel(self.StatsBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SoldProducts.setFont(font)
        self.SoldProducts.setText("")
        self.SoldProducts.setObjectName("SoldProducts")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SoldProducts)
        self.label_9 = QtWidgets.QLabel(self.StatsBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.TotalAmount = QtWidgets.QLabel(self.StatsBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalAmount.setFont(font)
        self.TotalAmount.setText("")
        self.TotalAmount.setObjectName("TotalAmount")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.TotalAmount)
        self.horizontalLayout_7.addWidget(self.StatsBox)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        ######################################################################
        #####################ToolBar Widgets #################################
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.AddProduct = QAction(QIcon("Icons/add-product.png"), "Add Product", self)
        self.toolBar.addAction(self.AddProduct)
        self.AddProduct.triggered.connect(self.AddProductWindow)
        self.toolBar.addSeparator()

        self.AddMembers = QAction(QIcon("Icons/add-user.png"), "Add Member", self)
        self.toolBar.addAction(self.AddMembers)
        self.AddMembers.triggered.connect(self.AddNewMember)

        self.toolBar.addSeparator()

        self.SellProduct = QAction(QIcon("Icons/sell-product.png"), "Sell Product", self)
        self.toolBar.addAction(self.SellProduct)
        self.SellProduct.triggered.connect(self.SellProducts)
        self.toolBar.addSeparator()
        self.tabWidget.blockSignals(False)

        #########################################################################
        #################Table Widget For Products Tab###########################
        self.table1.setColumnCount(6)

        self.table1.setColumnHidden(0, True)
        self.table1.setHorizontalHeaderItem(0, QTableWidgetItem("Product ID"))
        self.table1.setHorizontalHeaderItem(1, QTableWidgetItem("Product Name"))
        self.table1.setHorizontalHeaderItem(2, QTableWidgetItem("Manufacturer"))
        self.table1.setHorizontalHeaderItem(3, QTableWidgetItem("Price"))
        self.table1.setHorizontalHeaderItem(4, QTableWidgetItem("Quota"))
        self.table1.setHorizontalHeaderItem(5, QTableWidgetItem("Availability"))
        self.table1.doubleClicked.connect(self.UpdateProducts)


        ################Table Widget For Member Tab#####################

        self.table2.setColumnCount(4)
        self.table2.setHorizontalHeaderItem(0, QTableWidgetItem("Member ID"))
        self.table2.setHorizontalHeaderItem(1, QTableWidgetItem("Member Name"))
        self.table2.setHorizontalHeaderItem(2, QTableWidgetItem("Member Surname"))
        self.table2.setHorizontalHeaderItem(3, QTableWidgetItem("Member Phone Number"))
        self.table2.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.table2.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.table2.doubleClicked.connect(self.UpdateMember)


        ################################################################
        self.DisplayProducts()
        self.DisplayMembers()
        self.getStats()
        self.SearchBoxGo.clicked.connect(self.SearchProduct)
        self.SearchBtn.clicked.connect(self.SearchMembers)
        self.ListBtn.clicked.connect(self.ListProducts)

        ######################################################################


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def AddProductWindow(self):

        self.addproductwindow = QtWidgets.QMainWindow()
        self.NewWindow=NewProduct.Add_Product()
        self.NewWindow.setupUi(self.addproductwindow)
        self.addproductwindow.show()


    def AddNewMember(self):

        self.AddMemberWindow = QtWidgets.QMainWindow()
        self.AddMemberUi=AddMember.Add_Member()
        self.AddMemberUi.setupUi(self.AddMemberWindow)
        self.AddMemberWindow.show()

    def DisplayProducts(self):
        self.table1.setFont(QFont("Times",14))
        for i in reversed(range(self.table1.rowCount())):
            self.table1.removeRow(i)
        query="SELECT Product_ID,Product_Name,Product_Manufacturer,Product_Price,Product_Quota,Product_Availability FROM Products"
        queryans=cur.execute(query)
        for row_data in queryans:
            row_number=self.table1.rowCount()
            self.table1.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table1.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        self.table1.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def DisplayMembers(self):
        self.table2.setFont(QFont("Times",14))
        for i in reversed(range(self.table2.rowCount())):
            self.table2.removeRow(i)
        query="SELECT Member_ID,Member_Name,Member_Surname,Member_Phone FROM Members"
        queryans=cur.execute(query)
        for row_data in queryans:
            row_number=self.table2.rowCount()
            self.table2.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table2.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        self.table2.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def UpdateProducts(self):
        global productid
        listproducct=[]
        for i in range(0,6):
            listproducct.append(self.table1.item(self.table1.currentRow(),i).text())
        productid=listproducct[0]
        self.display=QtWidgets.QMainWindow()
        self.ui=UpdateProductWindow()
        self.ui.setupUi(self.display)

        self.display.show()

    def UpdateMember(self):
        global memberid
        listmember=[]
        for i in range(0,4):
            listmember.append(self.table2.item(self.table2.currentRow(),i).text())
        memberid=listmember[0]

        self.demo = QtWidgets.QMainWindow()
        self.ui = Update_Member()
        self.ui.setupUi(self.demo)
        self.demo.show()

    def SearchProduct(self):
        value=self.SearchBoxText.text()
        if value==" ":
            QMessageBox.information(self,"Product Manager","Enter Something To Search For")
        else:
            self.SearchBoxText.setText(" ")
            query=("SELECT Product_ID,Product_Name,Product_Manufacturer,Product_Price,Product_Quota,Product_Availability FROM Products WHERE Product_Name LIKE ? OR Product_Manufacturer LIKE ?")
            result=cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()
            print(result)
            if result==[]:
                QMessageBox.information(self,"Product Manager","There Is No Product Or Manufacturer With That Name ")
            else:
                for i in reversed(range(self.table1.rowCount())):
                    self.table1.removeRow(i)

                for row_data in result:
                    row_number=self.table1.rowCount()
                    self.table1.insertRow(row_number)
                    for column_number ,data in enumerate(row_data):
                        self.table1.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def SearchMembers(self):
        value=self.SearchMemberText.text()
        if value == "":
            QMessageBox.information(self,"Product Manager","Type In The Members Name Or Surname To search For")
        else:
            self.SearchMemberText.setText(" ")
            query=("SELECT Member_ID,Member_Name,Member_Surname,Member_Phone FROM Members WHERE Member_Name LIKE ? OR Member_Surname LIKE ? ")
            result=cur.execute(query,('%' + value + '%' , '%' + value + '%')).fetchall()
            print(result)
            if result==[]:
               QMessageBox.information(self,"Product Manager","No Member With This Surname OR Name")
            else:
                for i in reversed(range(self.table2.rowCount())):
                    self.table2.removeRow(i)
                for row_data in result:
                        row_number=self.table2.rowCount()
                        self.table2.insertRow(row_number)
                        for column_number ,     data in enumerate(row_data):
                            self.table2.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def ListProducts(self):
        if self.AllProductsRadio.isChecked():
            self.DisplayProducts()
        elif self.AvailableRadio.isChecked():
            query="SELECT Product_ID,Product_Name,Product_Manufacturer,Product_Price,Product_Quota,Product_Availability FROM Products WHERE Product_Availability='Available'"
            products=cur.execute(query).fetchall()
            print(products)
            for i in reversed(range (self.table1.rowCount())):
                self.table1.removeRow(i)
            for row_data in products:
                row_number=self.table1.rowCount()
                self.table1.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.table1.setItem(row_number,column_number,QTableWidgetItem(str(data)))

        elif self.OutOfStockRadio.isChecked():
            query="SELECT Product_ID,Product_Name,Product_Manufacturer,Product_Price,Product_Quota,Product_Availability FROM Products WHERE Product_Availability='Unavailable'"
            products1=cur.execute(query)
            for i in reversed(range(self.table1.rowCount())):
                self.table1.removeRow(i)
            for rows_data in products1:
                rows_number=self.table1.rowCount()
                self.table1.insertRow(rows_number)
                for colums_number,datas in enumerate(rows_data):
                    self.table1.setItem(rows_number,colums_number,QTableWidgetItem(str(datas)))

    def SellProducts(self):

        self.demo1 = QtWidgets.QMainWindow()
        self.ui = SellProduct.SellProductWindow()
        self.ui.setupUi(self.demo1)
        self.demo1.show()

    def getStats(self):
        productcount=cur.execute("SELECT COUNT(Product_ID) FROM Products").fetchall()
        productcount=productcount[0][0]
        print(productcount)
        membercount=cur.execute("SELECT COUNT(Member_ID) FROM Members").fetchall()
        soldcount=cur.execute("SELECT COUNT(Selling_ID) FROM Selling_Product").fetchall()
        totalamount=cur.execute("SELECT SUM(Selling_Amount) FROM Selling_Product").fetchall()
        totalamount=totalamount[0][0]
        print(totalamount)
        soldcount=soldcount[0][0]
        print(soldcount)
        membercount=membercount[0][0]
        print(membercount)
        self.TotalProducts.setText(str(productcount))
        self.TotalMembers.setText(str(membercount))
        self.SoldProducts.setText(str(soldcount))
        self.TotalAmount.setText(str(totalamount) + "/-" )

    def UpdateTab(self):
        self.getStats()
        self.DisplayProducts()
        self.DisplayMembers()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Product Manager"))
        self.SearchBox.setTitle(_translate("MainWindow", "Search Box"))
        self.label.setText(_translate("MainWindow", "Search Box"))
        self.SearchBoxGo.setText(_translate("MainWindow", "GO"))
        self.ListBox.setTitle(_translate("MainWindow", "List Box"))
        self.AllProductsRadio.setText(_translate("MainWindow", "All Products"))
        self.AvailableRadio.setText(_translate("MainWindow", "Available"))
        self.OutOfStockRadio.setText(_translate("MainWindow", "Out Of Stock"))
        self.ListBtn.setText(_translate("MainWindow", "List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Products"))
        self.SearcMembersBox.setTitle(_translate("MainWindow", "Search For Members"))
        self.SearchBtn.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Search Member"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Member"))
        self.StatsBox.setTitle(_translate("MainWindow", "Statistics"))
        self.label_3.setText(_translate("MainWindow", "Total Products:"))
        self.label_5.setText(_translate("MainWindow", "Total Members:"))
        self.label_7.setText(_translate("MainWindow", "Sold Products:"))
        self.label_9.setText(_translate("MainWindow", "Total Amount:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Statistics"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

#######################Update Product Class ####################################################################
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateProduct.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!



class UpdateProductWindow(QWidget):
    def setupUi(self, Update ):
        Update .setObjectName("Update")
        Update .resize(318, 501)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/product.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Update .setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Update )
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
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
        self.verticalLayout.addWidget(self.frame)
        self.ImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ImageLabel.setText("")
        self.ImageLabel.setObjectName("ImageLabel")
        self.verticalLayout.addWidget(self.ImageLabel)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(300, 150))
        self.frame_2.setMaximumSize(QtCore.QSize(300, 250))
        self.frame_2.setStyleSheet("background-color: rgb(255, 71,25);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Name = QtWidgets.QLineEdit(self.frame_2)
        self.Name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.Manufacturer = QtWidgets.QLineEdit(self.frame_2)
        self.Manufacturer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Manufacturer.setObjectName("Manufacturer")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Manufacturer)
        self.Price = QtWidgets.QLineEdit(self.frame_2)
        self.Price.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Price.setObjectName("Price")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Price)
        self.Quota = QtWidgets.QLineEdit(self.frame_2)
        self.Quota.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Quota.setObjectName("Quota")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Quota)
        self.Availabillity = QtWidgets.QComboBox(self.frame_2)
        self.Availabillity.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Availabillity.setObjectName("Availabillity")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Availabillity)
        self.Upload = QtWidgets.QPushButton(self.frame_2)
        self.Upload.setStyleSheet("background-color: rgb(255, 187, 14);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.Upload.setObjectName("Upload")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Upload)
        self.Submit = QtWidgets.QPushButton(self.frame_2)
        self.Submit.setStyleSheet("background-color: rgb(255, 187, 14);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.Submit.setObjectName("Submit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Submit)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setStyleSheet("background-color: rgb(255, 187, 14);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.verticalLayout.addWidget(self.frame_2)
        Update .setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Update )
        self.menubar.setGeometry(QtCore.QRect(0, 0, 318, 21))
        self.menubar.setObjectName("menubar")
        Update .setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Update )
        self.statusbar.setObjectName("statusbar")
        Update .setStatusBar(self.statusbar)

        ##############################################################################
        self.ProductDetails()
        self.Upload.clicked.connect(self.UploadImage)
        self.Submit.clicked.connect(self.UpdateProduct)
        self.pushButton.clicked.connect(self.DeleteProduct)


        ##############################################################################

        self.retranslateUi(Update )
        QtCore.QMetaObject.connectSlotsByName(Update )


    def ProductDetails(self):
        global productid
        size=(280,280)
        query = "SELECT * FROM Products WHERE Product_ID=?"
        product = cur.execute(query, (productid,)).fetchone()
        print(product)
        self.ProductName = product[1]
        self.ProductManufacturer = product[2]
        self.ProductPrice = product[3]
        self.ProductQuota = product[4]
        self.ProductImage = product[5]

        self.ProductStatus = product[6]
        self.Name.setText(self.ProductName)
        self.Manufacturer.setText(self.ProductManufacturer)
        self.Price.setText(str(self.ProductPrice))

        self.Quota.setText(str(self.ProductQuota))
        self.Availabillity.addItems(["Available","Unavailable"])

        self.ImageLabel.setPixmap(QPixmap("Images/{}".format(self.ProductImage)))

    def UploadImage(self):
        import os

        size=(250,200)
        self.filename,ok=QFileDialog.getOpenFileName(self,"Update Image","","Image Files (*.jpg *.png)")
        if ok:
            try:
                self.ProductImg=os.path.basename(self.filename)
                img=Image.open(self.filename)
                img=img.resize(size)
                img.save("Images/{}".format(self.ProductImg))
                QMessageBox.information(self,"Successful","Image Updated Successfully")

            except:
                QMessageBox.warning(self,"Warning","Image Can't Be Updated")
        else:
            QMessageBox.warning(self,"Warning","Image Can't Be Uploaded")


    def UpdateProduct(self):
        global productid
        productName=self.Name.text()
        productmanufacturer=self.Manufacturer.text()
        productPrice=int(self.Price.text())
        productQuota=int(self.Quota.text())
        productStatus=self.Availabillity.currentText()
        productImage= self.ProductImg
        if (productName and productmanufacturer and productPrice and productImage !=" "):
            try:
                query="UPDATE Products SET Product_Name=?,Product_Manufacturer=?,Product_Price=?,Product_Quota=?,Product_Image=?,Product_Availability=? WHERE Product_ID=?"
                cur.execute(query,(productName,productmanufacturer,productPrice,productQuota,productImage,productStatus,productid))
                con.commit()

                QMessageBox.information(self,"Successful","Product Updated Successfully")


            except:
                QMessageBox.warning(self,"Warning","Something Went Wrong")
        else:
            QMessageBox.warning(self,"Warning","Field Can't Be Empty")

    def DeleteProduct(self):
        global productid
        mbox=QMessageBox.question(self,"Delete Product","Are You Sure You Want To Delete Seleted Product",QMessageBox.Yes | QMessageBox.No , QMessageBox.No)
        if mbox==QMessageBox.Yes:
            try:
                query="DELETE FROM Products WHERE Product_ID=?"
                cur.execute(query,(productid,))
                con.commit()
                QMessageBox.information(self,"Product Manager","Selected Product Has Been Deleted")
                self.close()


            except:
                QMessageBox.warning(self,"Product Manager","Something Went Wrong")

        else:
            QMessageBox.information(self,"Product Manager","Product Not Deleted")












    def retranslateUi(self, Update ):
        _translate = QtCore.QCoreApplication.translate
        Update .setWindowTitle(_translate("MainWindow", "Product Information"))
        self.label.setText(_translate("MainWindow", "UPDATE PRODUCT"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Manufacturer"))
        self.label_5.setText(_translate("MainWindow", "Price"))
        self.label_6.setText(_translate("MainWindow", "Image"))
        self.label_7.setText(_translate("MainWindow", "Quota"))
        self.label_8.setText(_translate("MainWindow", "Availability"))
        self.Upload.setText(_translate("MainWindow", "Upload"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.pushButton.setText(_translate("MainWindow", "Delete"))




################################################################################################################
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateMember.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Update_Member(QWidget):
    def setupUi(self, UpdateMemberWindow):
        UpdateMemberWindow.setObjectName("UpdateMemberWindow")
        UpdateMemberWindow.resize(300, 530)
        UpdateMemberWindow.setMinimumSize(QtCore.QSize(0, 0))
        UpdateMemberWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        UpdateMemberWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(UpdateMemberWindow)
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
        self.label_2.setPixmap(QtGui.QPixmap("Udemy/icons/members.png"))
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
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Name = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Name.sizePolicy().hasHeightForWidth())
        self.Name.setSizePolicy(sizePolicy)
        self.Name.setMaximumSize(QtCore.QSize(200, 25))
        self.Name.setToolTip("")
        self.Name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: italic 20pt \"Monotype Corsiva\";\n"
"")
        self.Name.setText("")
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.Surname = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Surname.sizePolicy().hasHeightForWidth())
        self.Surname.setSizePolicy(sizePolicy)
        self.Surname.setMaximumSize(QtCore.QSize(200, 25))
        self.Surname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: italic 20pt \"Monotype Corsiva\";\n"
"")
        self.Surname.setText("")
        self.Surname.setObjectName("Surname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Surname)
        self.Phone = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Phone.sizePolicy().hasHeightForWidth())
        self.Phone.setSizePolicy(sizePolicy)
        self.Phone.setMaximumSize(QtCore.QSize(200, 25))
        self.Phone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: italic 20pt \"Monotype Corsiva\";\n"
"")
        self.Phone.setText("")
        self.Phone.setObjectName("Phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Phone)
        self.Delete = QtWidgets.QPushButton(self.frame_2)
        self.Delete.setStyleSheet("background-color: rgb(255, 187, 14);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.Delete.setObjectName("Delete")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Delete)
        self.Update = QtWidgets.QPushButton(self.frame_2)
        self.Update.setStyleSheet("background-color: rgb(255, 187, 14);\n"
"font: 14pt \"Simplified Arabic Fixed\";")
        self.Update.setObjectName("Update")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Update)
        self.verticalLayout.addWidget(self.frame_2)
        UpdateMemberWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UpdateMemberWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        UpdateMemberWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UpdateMemberWindow)
        self.statusbar.setObjectName("statusbar")
        UpdateMemberWindow.setStatusBar(self.statusbar)

        ###################################################################
        self.MemberDetails()
        self.Name.setText(self.MemberName)
        self.Surname.setText(self.MemberSurname)
        self.Phone.setText(self.MemberPhone)
        self.Delete.clicked.connect(self.DeleteMember)
        self.Update.clicked.connect(self.UpdateMembers)
        ###################################################################

        self.retranslateUi(UpdateMemberWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateMemberWindow)

    def MemberDetails(self):
        global memberid
        query="SELECT * FROM Members WHERE Member_ID=?"
        member=cur.execute(query,(memberid,)).fetchone()
        self.MemberName=member[1]
        self.MemberSurname=member[2]
        self.MemberPhone=member[3]

    def DeleteMember(self):
        global memberid
        mbox=QMessageBox.question(self,"Product Manager","Are You Sure You Want to Delete Selected Member",QMessageBox.Yes | QMessageBox.No , QMessageBox.No)
        if mbox==QMessageBox.Yes:
            try:
                query = "DELETE  FROM Members WHERE Member_ID=?"

                cur.execute(query, (memberid,))
                con.commit()
                QMessageBox.information(self,"Product Manager","Selected Member Deleted")
                self.close()
            except:
                QMessageBox.information(self,"Product Manager","Something Went Wrong")


    def UpdateMembers(self):
        global memberid
        Name=self.Name.text()
        Surname=self.Surname.text()
        Phone=self.Phone.text()
        if (Name and Surname and Phone !=" "):
            try:
                query="UPDATE Members SET Member_Name=?,Member_Surname=?,Member_Phone=?"
                cur.execute(query,(Name,Surname,str(Phone)))
                con.commit()
                QMessageBox.information(self,"Product Manager","Selected Member Updated")
            except:
                QMessageBox.information(self,"Product Manager","Something Went Wrong")


        else:
            QMessageBox.information(self,"Product Manager","Fields Can't Be Empty")



    def retranslateUi(self, UpdateMemberWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateMemberWindow.setWindowTitle(_translate("UpdateMemberWindow", "Update Member"))
        self.label.setText(_translate("UpdateMemberWindow", "UPDATE USER"))
        self.label_3.setText(_translate("UpdateMemberWindow", "Name"))
        self.label_4.setText(_translate("UpdateMemberWindow", "Surname"))
        self.label_5.setText(_translate("UpdateMemberWindow", "Phone Number"))
        self.Delete.setText(_translate("UpdateMemberWindow", "Delete"))
        self.Update.setText(_translate("UpdateMemberWindow", "Update"))






#################################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

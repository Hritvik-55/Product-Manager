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

        self.retranslateUi(UpdateMemberWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateMemberWindow)

    def retranslateUi(self, UpdateMemberWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateMemberWindow.setWindowTitle(_translate("UpdateMemberWindow", "Update Member"))
        self.label.setText(_translate("UpdateMemberWindow", "UPDATE USER"))
        self.label_3.setText(_translate("UpdateMemberWindow", "Name"))
        self.label_4.setText(_translate("UpdateMemberWindow", "Surname"))
        self.label_5.setText(_translate("UpdateMemberWindow", "Phone Number"))
        self.Delete.setText(_translate("UpdateMemberWindow", "Delete"))
        self.Update.setText(_translate("UpdateMemberWindow", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateMemberWindow = QtWidgets.QMainWindow()
    ui = Update_Member()
    ui.setupUi(UpdateMemberWindow)
    UpdateMemberWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import menu,first,head,forgetpassword,changepassword,dialogdelforacc
from first import *
forecho=1
class Ui_admin(object):
    def inchange(self):
        self.invalid.setText("")
    def iconcheck(self):
        global forecho
        if forecho==1:
            self.showpd.setStyleSheet("background-image: url(:/newPrefix/kisspng-computer-icons-cross-eye-5adf65cad344d8.0427956315245900268654 (1).png);")
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            forecho=2
        else:
            self.showpd.setStyleSheet("background-image: url(:/newPrefix/show-password-64 (1).png);")
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            forecho=1
    def back(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=first.Ui_first()
        self.ui.setupUi(self.window)
        self.window.show()
        self.admin1.hide()
    def enterclick(self): 
        user=self.username.text
        passw=self.password.text
        head.checkforfirst()
        if len(self.username.text())!=0 and len(self.password.text())!=0:
            if self.username.text()==head.forfirst[0] and self.password.text()==head.forfirstt[0]:
                self.invalid.setText("")
                self.openwindow()
                self.username.setText("")
                self.password.setText("")
                self.invalid.setText("") 
            else:
                self.invalid.setText("Invalid username and password")
        else:
            self.invalid.setText("All fields are mandatory")
    def openwindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=dialogdelforacc.Ui_dialogdel()
        self.ui.setupUi(self.window)
        self.window.show()
        self.admin1.hide()
    def setupUi(self, admin):
        self.admin1=admin
        admin.setObjectName("admin")
        admin.resize(719, 522)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(admin.sizePolicy().hasHeightForWidth())
        admin.setSizePolicy(sizePolicy)
        admin.setMinimumSize(QtCore.QSize(719, 522))
        admin.setMaximumSize(QtCore.QSize(719, 522))
        self.centralwidget = QtWidgets.QWidget(admin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -30, 731, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/White-Lock-Wallpaper-1080x2340-.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 270, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPixelSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 310, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPixelSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(150, 270, 151, 21))
        self.username.setObjectName("username")
        self.username.setStyleSheet("background-color:transparent;")
        
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(150, 310, 151, 21))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password.setStyleSheet("background-color: transparent;")
        self.invalid = QtWidgets.QLabel(self.centralwidget)
        self.invalid.setGeometry(QtCore.QRect(150, 330, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPixelSize(13)
        self.invalid.setFont(font)
        self.invalid.setStyleSheet("color: rgb(255, 3, 3);")
        self.invalid.setText("")
        self.invalid.setObjectName("invalid")
        self.showpd = QtWidgets.QPushButton(self.centralwidget)
        self.showpd.setGeometry(QtCore.QRect(305, 312, 22, 16))
        self.showpd.setStyleSheet("background-image: url(:/newPrefix/show-password-64 (1).png);")
        self.showpd.setText("")
        self.showpd.setFlat(True)
        self.showpd.setDefault(False)
        self.showpd.setAcceptDrops(False)
        self.showpd.setObjectName("showpd")
        self.showpd.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(150, 360, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPixelSize(13)
        self.ok.setFont(font)
        self.ok.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ok.setDefault(True)
        self.ok.setFlat(True)
        self.ok.setObjectName("ok")
        self.ok_ = QtWidgets.QPushButton(self.centralwidget)
        self.ok_.setGeometry(QtCore.QRect(150, 400, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPixelSize(13)
        self.ok_.setFont(font)
        self.ok_.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ok_.setDefault(True)
        self.ok_.setFlat(True)
        self.ok_.setObjectName("ok_")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(70, 200, 250, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPixelSize(15)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_4")
        self.label_41.setText("To continue, first verify that it's you")
        admin.setCentralWidget(self.centralwidget)
        admin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(admin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 21))
        self.menubar.setObjectName("menubar")
        admin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(admin)
        self.statusbar.setObjectName("statusbar")
        admin.setStatusBar(self.statusbar)
        self.showpd.clicked.connect(self.iconcheck)
        self.ok.clicked.connect(self.enterclick)
        self.ok_.clicked.connect(self.back)
        self.username.textChanged.connect(self.inchange)
        self.password.textChanged.connect(self.inchange)
        self.retranslateUi(admin)
        QtCore.QMetaObject.connectSlotsByName(admin)

    def retranslateUi(self, admin):
        _translate = QtCore.QCoreApplication.translate
        admin.setWindowTitle(_translate("admin", "Remove account"))
        self.label_2.setText(_translate("admin", "Username "))
        self.label_3.setText(_translate("admin", "Password "))
        self.ok.setText(_translate("admin", "Submit"))
        self.ok_.setText(_translate("admin", "Back"))

import pic


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    admin = QtWidgets.QMainWindow()
    ui = Ui_admin()
    ui.setupUi(admin)
    admin.show()
    sys.exit(app.exec_())

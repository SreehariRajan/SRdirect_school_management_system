# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mod01.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import head,mod001,dialogmodteacher
from mod001 import *
class Ui_mod01(object):
    def inchange(self):
        self.invalid_3.setText("")
    def ctrchange(self):
        cteach=self.cteach.text()
        cteach=cteach.strip()
        cteach=cteach.split(' ')
        cteach2=''
        for i in cteach:
                cteach2+=i
        if len(self.cteach.text())!=0:
            if cteach2.isalpha()==True:
                head.cupdate(retrieve.amod,retrieve.bmod,self.cteach.text().lower())
                self.window = QtWidgets.QMainWindow()
                self.ui=dialogmodteacher.Ui_dialogmod()
                self.ui.setupUi(self.window)
                self.window.show()
                self.mod01.hide()
                
            else:
                self.invalid_3.setText("Invalid Entry")
        else:
            self.invalid_3.setText("The field is mandatory")
    def cancel1(self): 
        self.window = QtWidgets.QMainWindow()
        self.ui=mod001.Ui_mod001()
        self.ui.setupUi(self.window)
        self.window.show()
        self.mod01.hide()
    def setupUi(self, mod01):
        self.mod01=mod01
        mod01.setObjectName("mod01")
        mod01.resize(510, 313)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mod01.sizePolicy().hasHeightForWidth())
        mod01.setSizePolicy(sizePolicy)
        mod01.setMinimumSize(QtCore.QSize(510, 313))
        mod01.setMaximumSize(QtCore.QSize(510, 313))
        self.centralwidget = QtWidgets.QWidget(mod01)
        self.centralwidget.setObjectName("centralwidget")
        self.invalid = QtWidgets.QLabel(self.centralwidget)
        self.invalid.setGeometry(QtCore.QRect(150, 350, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.invalid.setFont(font)
        self.invalid.setStyleSheet("color: rgb(255, 3, 3);")
        self.invalid.setText("")
        self.invalid.setObjectName("invalid")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, -20, 751, 541))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/ttt.jpg"))
        self.label.setObjectName("label")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setAcceptDrops(False)
        self.add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add.setCheckable(False)
        self.add.setDefault(True)
        self.add.setFlat(True)
        self.add.setObjectName("add")
        self.add.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 20, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.invalid_2 = QtWidgets.QLabel(self.centralwidget)
        self.invalid_2.setGeometry(QtCore.QRect(240, 280, 151, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.invalid_2.setFont(font)
        self.invalid_2.setStyleSheet("color:rgb(238, 0, 0)")
        self.invalid_2.setText("")
        self.invalid_2.setObjectName("invalid_2")
        self.cteach = QtWidgets.QLineEdit(self.centralwidget)
        self.cteach.setGeometry(QtCore.QRect(220, 130, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPixelSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.cteach.setFont(font)
        self.cteach.setStyleSheet("background-color:transparent;")
        self.cteach.setText("")
        self.cteach.setObjectName("cteach")

        
        self.cteach.setText((head.ctr).upper())
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(220, 220, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setAcceptDrops(False)
        self.back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.back.setCheckable(False)
        self.back.setDefault(True)
        self.back.setFlat(True)
        self.back.setObjectName("back")
        self.classwise = QtWidgets.QPushButton(self.centralwidget)
        self.classwise.setGeometry(QtCore.QRect(220, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.classwise.setFont(font)
        self.classwise.setAcceptDrops(False)
        self.classwise.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.classwise.setCheckable(False)
        self.classwise.setDefault(True)
        self.classwise.setFlat(True)
        self.classwise.setObjectName("classwise")
        self.classd = QtWidgets.QLabel(self.centralwidget)
        self.classd.setGeometry(QtCore.QRect(450, 50, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.classd.setFont(font)
        self.classd.setText("")
        self.classd.setObjectName("classd")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 50, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        

        
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(110, 130, 111, 21))
        font = QtGui.QFont()        
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setTextFormat(QtCore.Qt.RichText)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_18.setObjectName("label_18")
        self.invalid_3 = QtWidgets.QLabel(self.centralwidget)
        self.invalid_3.setGeometry(QtCore.QRect(220, 150, 151, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPixelSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.invalid_3.setFont(font)
        self.invalid_3.setStyleSheet("color:rgb(238, 0, 0)\n"
"")
        self.invalid_3.setText("")
        self.invalid_3.setObjectName("invalid_3")
        mod01.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mod01)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        mod01.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mod01)
        self.statusbar.setObjectName("statusbar")
        mod01.setStatusBar(self.statusbar)
        self.add.setFocusPolicy(QtCore.Qt.NoFocus)
        self.classwise.clicked.connect(self.ctrchange)
        self.back.clicked.connect(self.cancel1)

        self.retranslateUi(mod01)
        QtCore.QMetaObject.connectSlotsByName(mod01)
        mod01.setTabOrder(self.cteach, self.classwise)
        mod01.setTabOrder(self.classwise, self.back)
        self.cteach.textChanged.connect(self.inchange)
    def retranslateUi(self, mod01):
        _translate = QtCore.QCoreApplication.translate
        mod01.setWindowTitle(_translate("mod01", "Update"))
        self.add.setText(_translate("mod01", "UPDATE"))
        self.label_3.setText(_translate("mod01", "admin"))
        self.back.setText(_translate("mod01", "CANCEL"))
        self.classwise.setText(_translate("mod01", "OK"))
        self.label_4.setText(_translate("mod01", "CLASS :"))
        self.label_18.setText(_translate("mod01", "CLASS TEACHER"))
import pic


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mod01 = QtWidgets.QMainWindow()
    ui = Ui_mod01()
    ui.setupUi(mod01)
    mod01.show()
    sys.exit(app.exec_())

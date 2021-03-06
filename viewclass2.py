# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewclass.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
import roman,sys
import retrieve,view02option
class Ui_viewclass(object):
    def backing(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=view02option.Ui_view0()
        self.ui.setupUi(self.window)
        self.window.show()
        self.viewclass2.hide()
    def classviewing(self):
        retrieve.view0333()
        for row_number,row_data in enumerate(retrieve.result500):
            self.tableView.insertRow(row_number)
            for column_number,column_data in enumerate(row_data):
                if column_number!=1:
                    item1=str(column_data).upper()
                    #making readonly...................
                    item=QtWidgets.QTableWidgetItem(item1)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    #....................................
                    self.tableView.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(item))
                else:
                    global imagelabel
                    imagelabel=QtWidgets.QLabel(self.centralwidget)
                    imagelabel.setText("")
                    font = QtGui.QFont()
                    font.setFamily("Myriad Pro")
                    font.setPixelSize(18)
                    font.setBold(True)
                    font.setWeight(75)
                    imagelabel.setFont(font)
                    if column_data==b'PHOTO NOT AVAILABLE':
                        imagelabel.setStyleSheet("border: 2px solid black;")
                        pic="         PHOTO \n           NOT \n     AVAILABLE"
                        imagelabel.setText(pic)
                        item=imagelabel
                    else:
                        item=self.getimage(column_data)
                    self.tableView.setCellWidget(row_number,column_number,item)
        self.tableView.verticalHeader().setDefaultSectionSize(175)
        self.tableView.horizontalHeader().setDefaultSectionSize(145)
        countc=self.tableView.columnCount
    def getimage(self,image):
        imagelabel.setScaledContents(True)
        pixmap=QtGui.QPixmap()
        picformatcheck=['png','jpg','jpeg']
        for i in range (0,len(picformatcheck)):
            pixmap.loadFromData(image,picformatcheck[i])
            imagelabel.setPixmap(pixmap)
            if pixmap.loadFromData(image,picformatcheck[i])==True:
                break
            i+=1
        return imagelabel
    def namesorting(self):
        self.tableView.clearContents()
        self.tableView.setRowCount(0)
        a=self.searching.text
        b=str(self.searching.text())
        b=b+'%'
        l=[]
        for i in b:
            l.append(i)
        l.append('"')
        l.insert(0,'"')
        c=""
        for i in l:
            c+=i     
        retrieve.namesorting11(c.lower())
        for row_number,row_data in enumerate(retrieve.result1500):
            self.tableView.insertRow(row_number)
            for column_number,column_data in enumerate(row_data):
                if column_number!=1:
                    item=str(column_data).upper()
                    self.tableView.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(item))
                else:
                    global imagelabel
                    imagelabel=QtWidgets.QLabel(self.centralwidget)
                    imagelabel.setText("")
                    font = QtGui.QFont()
                    font.setFamily("Myriad Pro")
                    font.setPixelSize(18)
                    font.setBold(True)
                    font.setWeight(75)
                    imagelabel.setFont(font)
                    if column_data==b'PHOTO NOT AVAILABLE':
                        imagelabel.setStyleSheet("border: 2px solid black;")
                        pic="         PHOTO \n           NOT \n     AVAILABLE"
                        imagelabel.setText(pic)
                        item=imagelabel
                    else:
                        item=self.getimage(column_data)
                    
                    self.tableView.setCellWidget(row_number,column_number,item)
        self.tableView.verticalHeader().setDefaultSectionSize(200)
    def setupUi(self, viewclass):
        self.viewclass2=viewclass
        viewclass.setObjectName("viewclass")
        viewclass.resize(1339, 729)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(viewclass.sizePolicy().hasHeightForWidth())
        viewclass.setSizePolicy(sizePolicy)
        viewclass.setMinimumSize(QtCore.QSize(1339, 729))
        viewclass.setMaximumSize(QtCore.QSize(1339, 729))
        self.centralwidget = QtWidgets.QWidget(viewclass)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 160, 1301, 450))
        self.tableView.setStyleSheet("background:transparent;")
        self.tableView.setObjectName("tableView")
        self.tableView.setColumnCount(11)
        self.tableView.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView.setHorizontalHeaderItem(10, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1341, 711))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/ttt - Copy.jpg"))
        self.label.setObjectName("label")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(20, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(15)
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
        self.label_2.setGeometry(QtCore.QRect(1160, 60, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.classd = QtWidgets.QLabel(self.centralwidget)
        self.classd.setGeometry(QtCore.QRect(1230, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.classd.setFont(font)
        self.classd.setText("")
        self.classd.setObjectName("classd")
        self.searching = QtWidgets.QLineEdit(self.centralwidget)
        self.searching.setGeometry(QtCore.QRect(20, 110, 341, 31))
        self.searching.setStyleSheet("background:transparent;\n"
"\n"
"")
        self.searching.setObjectName("searching")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 110, 47, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/sse.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1270, 20, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1240, 10, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.tableView.raise_()
        self.add.raise_()
        self.label_2.raise_()
        self.classd.raise_()
        self.searching.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        viewclass.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(viewclass)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1339, 21))
        self.menubar.setObjectName("menubar")
        viewclass.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(viewclass)
        self.statusbar.setObjectName("statusbar")
        viewclass.setStatusBar(self.statusbar)
        self.classviewing()
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(1191, 630, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exit.setDefault(True)
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.retranslateUi(viewclass)
        viewclass.setTabOrder(self.searching, self.exit)
        self.exit.clicked.connect(self.backing)
        QtCore.QMetaObject.connectSlotsByName(viewclass)
        self.searching.textChanged.connect(self.namesorting)

        
    def retranslateUi(self, viewclass):
        _translate = QtCore.QCoreApplication.translate
        viewclass.setWindowTitle(_translate("viewclass", "View details"))
        item = self.tableView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ADMN ID"))
        item = self.tableView.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PHOTO"))
        item = self.tableView.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableView.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D.O.B"))
        item = self.tableView.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CLASS"))
        item = self.tableView.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CLASS TEACHER"))
        item = self.tableView.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "DIVISION"))
        item = self.tableView.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ROLL NO."))
        item = self.tableView.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "PHONE NO."))
        item = self.tableView.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "EMAIL ID"))
        item = self.tableView.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "ADDRESS"))
        self.exit.setText(_translate("viewclass", "BACK"))
        self.add.setText(_translate("viewclass", "SEARCH"))
        self.label_2.setText(_translate("viewclass", "  CLASS :"))
        self.label_4.setText(_translate("viewclass", "admin"))
import pic


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewclass = QtWidgets.QMainWindow()
    ui = Ui_viewclass()
    ui.setupUi(viewclass)
    viewclass.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ecc(object):
    def setupUi(self, ecc):
        ecc.setObjectName("ecc")
        ecc.resize(544, 397)
        self.centralwidget = QtWidgets.QWidget(ecc)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 30, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(110, 80, 371, 87))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 300, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(110, 190, 371, 87))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 300, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 30, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        ecc.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ecc)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 26))
        self.menubar.setObjectName("menubar")
        ecc.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ecc)
        self.statusbar.setObjectName("statusbar")
        ecc.setStatusBar(self.statusbar)

        self.retranslateUi(ecc)
        QtCore.QMetaObject.connectSlotsByName(ecc)

    def retranslateUi(self, ecc):
        _translate = QtCore.QCoreApplication.translate
        ecc.setWindowTitle(_translate("ecc", "ECC Cipher"))
        self.label_5.setText(_translate("ecc", "Signature:"))
        self.label_3.setText(_translate("ecc", "Information:"))
        self.label.setText(_translate("ecc", "ECC CIPHER"))
        self.pushButton_5.setText(_translate("ecc", "Sign"))
        self.pushButton_4.setText(_translate("ecc", "Verify"))
        self.pushButton_3.setText(_translate("ecc", "Generate Keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ecc = QtWidgets.QMainWindow()
    ui = Ui_ecc()
    ui.setupUi(ecc)
    ecc.show()
    sys.exit(app.exec_())

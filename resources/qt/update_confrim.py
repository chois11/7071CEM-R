# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_confrim.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.settings = QtWidgets.QTextBrowser(Form)
        self.settings.setEnabled(False)
        self.settings.setGeometry(QtCore.QRect(150, 10, 101, 31))
        self.settings.setMouseTracking(False)
        self.settings.setAcceptDrops(False)
        self.settings.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settings.setObjectName("settings")
        self.settings_2 = QtWidgets.QTextBrowser(Form)
        self.settings_2.setEnabled(False)
        self.settings_2.setGeometry(QtCore.QRect(50, 70, 311, 51))
        self.settings_2.setMouseTracking(False)
        self.settings_2.setAcceptDrops(False)
        self.settings_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settings_2.setObjectName("settings_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.settings.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Confrim</span></p></body></html>"))
        self.settings_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">The update takes at least one hour. Do you wish to continue?</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Continue"))
        self.pushButton_2.setText(_translate("Form", "Back"))

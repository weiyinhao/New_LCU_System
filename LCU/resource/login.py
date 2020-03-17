# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(912, 571)
        self.lab_background = QtWidgets.QLabel(Form)
        self.lab_background.setGeometry(QtCore.QRect(10, 20, 611, 481))
        self.lab_background.setText("")
        self.lab_background.setObjectName("lab_background")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(630, 10, 271, 491))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.user_Edit = QtWidgets.QLineEdit(self.groupBox)
        self.user_Edit.setGeometry(QtCore.QRect(60, 80, 201, 31))
        self.user_Edit.setObjectName("user_Edit")
        self.psw_Edit = QtWidgets.QLineEdit(self.groupBox)
        self.psw_Edit.setGeometry(QtCore.QRect(60, 140, 201, 31))
        self.psw_Edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.psw_Edit.setObjectName("psw_Edit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 41, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_ForgetPaw = QtWidgets.QPushButton(self.groupBox)
        self.btn_ForgetPaw.setGeometry(QtCore.QRect(152, 200, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(9)
        self.btn_ForgetPaw.setFont(font)
        self.btn_ForgetPaw.setStyleSheet("")
        self.btn_ForgetPaw.setFlat(False)
        self.btn_ForgetPaw.setObjectName("btn_ForgetPaw")
        self.btn_login = QtWidgets.QPushButton(self.groupBox)
        self.btn_login.setEnabled(False)
        self.btn_login.setGeometry(QtCore.QRect(10, 250, 251, 41))
        self.btn_login.setStyleSheet("\n"
"QPushButton#pButtonOk\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border: 1px solid rgb(11 , 137 , 234);\n"
"}\n"
"\n"
"QPushButton#pButtonOk:hover\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"    border: 1px solid rgb(11 , 137 , 234);\n"
"}\n"
"\n"
"QPushButton#pButtonOk:pressed\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    border: 1px solid rgb(12 , 138 , 235);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"\n"
"QPushButton#pButtonCancel\n"
"{\n"
"    color:black;\n"
"    background-color:rgb(238 , 238 , 238);\n"
"    border: 1px solid rgb(183 , 183 , 183);\n"
"}\n"
"\n"
"QPushButton#pButtonCancel:hover\n"
"{\n"
"    color:black;\n"
"    background-color:rgb(228 , 240 , 250);\n"
"    border: 1px solid rgb(15 , 150 , 255);\n"
"}\n"
"\n"
"QPushButton#pButtonCancel:pressed\n"
"{\n"
"    color:black;\n"
"    background-color:rgb(204 , 228 , 247);\n"
"    border: 1px solid rgb(1 , 84 , 153);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.btn_Authentication = QtWidgets.QPushButton(self.groupBox)
        self.btn_Authentication.setGeometry(QtCore.QRect(120, 320, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(9)
        self.btn_Authentication.setFont(font)
        self.btn_Authentication.setStyleSheet("")
        self.btn_Authentication.setFlat(False)
        self.btn_Authentication.setObjectName("btn_Authentication")
        self.lab_code = QtWidgets.QLabel(self.groupBox)
        self.lab_code.setGeometry(QtCore.QRect(20, 370, 91, 101))
        self.lab_code.setText("")
        self.lab_code.setObjectName("lab_code")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(130, 370, 121, 101))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 520, 851, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.btn_login.clicked.connect(Form.check_login)
        self.psw_Edit.textChanged['QString'].connect(Form.Led_is_text)
        self.user_Edit.textChanged['QString'].connect(Form.Led_is_text)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "聊城大学教务系统"))
        self.label_2.setText(_translate("Form", "用户登录"))
        self.label_3.setText(_translate("Form", "学号:"))
        self.label_4.setText(_translate("Form", "密码:"))
        self.btn_ForgetPaw.setText(_translate("Form", "忘记密码了？"))
        self.btn_login.setText(_translate("Form", "登录"))
        self.btn_Authentication.setText(_translate("Form", "统一身份认证登录"))
        self.label_6.setText(_translate("Form", "用手机扫一扫,\n"
"安全、便捷登录"))
        self.label.setText(_translate("Form", "版权所有© Copyright 1999-2019 正方软件股份有限公司　　中国·杭州西湖区紫霞街176号 互联网创新创业园2号301"))


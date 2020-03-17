# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stu_info_maintain.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1242, 818)
        self.btn_return_home = QtWidgets.QPushButton(Form)
        self.btn_return_home.setGeometry(QtCore.QRect(1140, 20, 93, 28))
        self.btn_return_home.setObjectName("btn_return_home")
        self.lab_title_info = QtWidgets.QLabel(Form)
        self.lab_title_info.setGeometry(QtCore.QRect(40, 10, 1091, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.lab_title_info.setFont(font)
        self.lab_title_info.setStyleSheet("color: rgb(0, 170, 255);")
        self.lab_title_info.setObjectName("lab_title_info")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 1221, 691))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(1020, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(1120, 20, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 60, 271, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(10, 100, 1201, 581))
        self.tableView.setStyleSheet("QTableView QTableCornerButton::section {\n"
"    color: white;/*文字颜色*/\n"
"    background-color: rgb(41, 139, 201);/*背景色*/\n"
"    border: 5px solid #418bc9;/*边框*/\n"
"    border-radius:0px;/*边框圆角*/\n"
"    border-color: rgb(41, 139, 201);/*边框颜色*/\n"
"    font: 10px;/*字体大小*/\n"
"    padding:0px 0 0 0px;/*内边距*/\n"
" }\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(41, 139, 201);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color:rgb(41, 139, 201);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color:rgb(41, 139, 201);\n"
"}")
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 780, 1221, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.btn_return_home.clicked.connect(Form.return_home)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "聊城大学教务系统"))
        self.btn_return_home.setText(_translate("Form", "返回主页"))
        self.lab_title_info.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "申请"))
        self.pushButton_2.setText(_translate("Form", "撤销申请"))
        self.label.setText(_translate("Form", "历史修改记录"))
        self.label_2.setText(_translate("Form", "版权所有© Copyright 1999-2019 正方软件股份有限公司　　中国·杭州西湖区紫霞街176号 互联网创新创业园2号301"))


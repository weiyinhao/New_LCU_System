# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_course_page.ui'
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
        self.btn_return_home.setGeometry(QtCore.QRect(1140, 30, 93, 28))
        self.btn_return_home.setObjectName("btn_return_home")
        self.lab_title_info = QtWidgets.QLabel(Form)
        self.lab_title_info.setGeometry(QtCore.QRect(40, 20, 1091, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.lab_title_info.setFont(font)
        self.lab_title_info.setStyleSheet("color: rgb(0, 170, 255);")
        self.lab_title_info.setObjectName("lab_title_info")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 90, 1221, 671))
        self.stackedWidget.setObjectName("stackedWidget")
        self.stu_course_query_page = QtWidgets.QWidget()
        self.stu_course_query_page.setObjectName("stu_course_query_page")
        self.groupBox = QtWidgets.QGroupBox(self.stu_course_query_page)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1201, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.cob_school_year_2 = QtWidgets.QComboBox(self.groupBox)
        self.cob_school_year_2.setGeometry(QtCore.QRect(110, 30, 331, 31))
        self.cob_school_year_2.setObjectName("cob_school_year_2")
        self.label_84 = QtWidgets.QLabel(self.groupBox)
        self.label_84.setGeometry(QtCore.QRect(30, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.cob_school_year_3 = QtWidgets.QComboBox(self.groupBox)
        self.cob_school_year_3.setGeometry(QtCore.QRect(580, 30, 331, 31))
        self.cob_school_year_3.setObjectName("cob_school_year_3")
        self.label_85 = QtWidgets.QLabel(self.groupBox)
        self.label_85.setGeometry(QtCore.QRect(500, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(1050, 30, 71, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(1130, 30, 71, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.stu_course_query_page)
        self.tableView.setGeometry(QtCore.QRect(10, 100, 1201, 531))
        self.tableView.setObjectName("tableView")
        self.line_11 = QtWidgets.QFrame(self.stu_course_query_page)
        self.line_11.setGeometry(QtCore.QRect(640, 630, 16, 51))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.btn_select_course_first_2 = QtWidgets.QPushButton(self.stu_course_query_page)
        self.btn_select_course_first_2.setEnabled(False)
        self.btn_select_course_first_2.setGeometry(QtCore.QRect(460, 640, 31, 21))
        self.btn_select_course_first_2.setObjectName("btn_select_course_first_2")
        self.led_btn_select_course_current_page_2 = QtWidgets.QLineEdit(self.stu_course_query_page)
        self.led_btn_select_course_current_page_2.setEnabled(False)
        self.led_btn_select_course_current_page_2.setGeometry(QtCore.QRect(540, 640, 31, 21))
        self.led_btn_select_course_current_page_2.setObjectName("led_btn_select_course_current_page_2")
        self.line_12 = QtWidgets.QFrame(self.stu_course_query_page)
        self.line_12.setGeometry(QtCore.QRect(524, 630, 16, 51))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.btn_select_course_front_2 = QtWidgets.QPushButton(self.stu_course_query_page)
        self.btn_select_course_front_2.setEnabled(False)
        self.btn_select_course_front_2.setGeometry(QtCore.QRect(490, 640, 31, 21))
        self.btn_select_course_front_2.setObjectName("btn_select_course_front_2")
        self.btn_select_course_end_2 = QtWidgets.QPushButton(self.stu_course_query_page)
        self.btn_select_course_end_2.setGeometry(QtCore.QRect(690, 640, 31, 21))
        self.btn_select_course_end_2.setObjectName("btn_select_course_end_2")
        self.combox_select_course_show_page_2 = QtWidgets.QComboBox(self.stu_course_query_page)
        self.combox_select_course_show_page_2.setGeometry(QtCore.QRect(730, 640, 71, 22))
        self.combox_select_course_show_page_2.setObjectName("combox_select_course_show_page_2")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.combox_select_course_show_page_2.addItem("")
        self.btn_select_course_next_2 = QtWidgets.QPushButton(self.stu_course_query_page)
        self.btn_select_course_next_2.setGeometry(QtCore.QRect(660, 640, 31, 21))
        self.btn_select_course_next_2.setObjectName("btn_select_course_next_2")
        self.lab_select_course_total_page_2 = QtWidgets.QLabel(self.stu_course_query_page)
        self.lab_select_course_total_page_2.setGeometry(QtCore.QRect(580, 644, 71, 16))
        self.lab_select_course_total_page_2.setObjectName("lab_select_course_total_page_2")
        self.stackedWidget.addWidget(self.stu_course_query_page)
        self.course_primary_page = QtWidgets.QWidget()
        self.course_primary_page.setObjectName("course_primary_page")
        self.label_3 = QtWidgets.QLabel(self.course_primary_page)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 1201, 51))
        self.label_3.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.course_primary_page)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 1201, 421))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.course_primary_page)
        self.Autonomy_course_selct_page = QtWidgets.QWidget()
        self.Autonomy_course_selct_page.setObjectName("Autonomy_course_selct_page")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Autonomy_course_selct_page)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 1201, 81))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 671, 31))
        self.lineEdit.setText("")
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 30, 93, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(970, 30, 93, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Autonomy_course_selct_page)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 120, 1201, 441))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 1181, 351))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.Autonomy_course_selct_page)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 770, 1221, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(2)
        self.btn_return_home.clicked.connect(Form.return_home)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_return_home.setText(_translate("Form", "返回主页"))
        self.lab_title_info.setText(_translate("Form", "TextLabel"))
        self.label_84.setText(_translate("Form", "*学年"))
        self.label_85.setText(_translate("Form", "*学年"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "导出"))
        self.btn_select_course_first_2.setText(_translate("Form", "◀"))
        self.led_btn_select_course_current_page_2.setText(_translate("Form", "1"))
        self.btn_select_course_front_2.setText(_translate("Form", "<"))
        self.btn_select_course_end_2.setText(_translate("Form", "▶"))
        self.combox_select_course_show_page_2.setItemText(0, _translate("Form", "15"))
        self.combox_select_course_show_page_2.setItemText(1, _translate("Form", "20"))
        self.combox_select_course_show_page_2.setItemText(2, _translate("Form", "30"))
        self.combox_select_course_show_page_2.setItemText(3, _translate("Form", "50"))
        self.combox_select_course_show_page_2.setItemText(4, _translate("Form", "70"))
        self.combox_select_course_show_page_2.setItemText(5, _translate("Form", "90"))
        self.combox_select_course_show_page_2.setItemText(6, _translate("Form", "100"))
        self.combox_select_course_show_page_2.setItemText(7, _translate("Form", "150"))
        self.combox_select_course_show_page_2.setItemText(8, _translate("Form", "300"))
        self.combox_select_course_show_page_2.setItemText(9, _translate("Form", "500"))
        self.combox_select_course_show_page_2.setItemText(10, _translate("Form", "800"))
        self.combox_select_course_show_page_2.setItemText(11, _translate("Form", "1000"))
        self.combox_select_course_show_page_2.setItemText(12, _translate("Form", "1500"))
        self.combox_select_course_show_page_2.setItemText(13, _translate("Form", "2000"))
        self.combox_select_course_show_page_2.setItemText(14, _translate("Form", "2500"))
        self.combox_select_course_show_page_2.setItemText(15, _translate("Form", "5000"))
        self.btn_select_course_next_2.setText(_translate("Form", ">"))
        self.lab_select_course_total_page_2.setText(_translate("Form", "共 0 页"))
        self.label_4.setText(_translate("Form", "对不起，当前时间不可报名，如有需要，请与管理员联系！"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入课程号或课程名称或教学班名查询!"))
        self.pushButton_3.setText(_translate("Form", "查询"))
        self.pushButton_4.setText(_translate("Form", "重置"))
        self.label_5.setText(_translate("Form", "对不起，当前不属于选课阶段，如有需要，请与管理员联系！"))
        self.label_2.setText(_translate("Form", "版权所有© Copyright 1999-2019 正方软件股份有限公司　　中国·杭州西湖区紫霞街176号 互联网创新创业园2号301"))


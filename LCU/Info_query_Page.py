from PyQt5.Qt import *
from resource.info_inquiry_page import Ui_Form
from API.API_Tool import APITool
from API.API_Tool import Config
from API.API_Tool import Cache
class InfoQuery(QWidget,Ui_Form):
    success_return = pyqtSignal()#返回主页信号
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

        self.Init()
        self.current_grade_page=0
        self.current_grade_time=0
        self.current_stu_sroce_page=0
        self.current_plan_page=0
    #初始化页面
    def Init(self):
        pass
    #显示页面槽函数
    def showEvent(self, QShowEvent):
        if Cache.current_title_info=='查询个人信息':
            self.stackedWidget.setCurrentIndex(0)
            # 设置个人信息
            self.Set_My_Info()
            # 设置奖罚信息
            self.Set_Bonus_Info()
            # 设置学籍异动
            self.Set_school_roll_status()
            # 设置页面所处位置
            if self.tabWidget.currentIndex() != 0:
                self.tabWidget.setCurrentIndex(0)
        elif Cache.current_title_info=='推荐课表打印':
            self.stackedWidget.setCurrentIndex(1)
            #设置课表打印页面
            self.Set_curriculum_print_page()
            #初始化其余三个下拉框
            self.cob_zhuanye.clear()
            self.cob_zhuanye.addItem("全部")
            self.cob_zhuanyefangxiang.clear()
            self.cob_zhuanyefangxiang.addItem("全部")
            self.cob_class.clear()
            self.cob_class.addItem("全部")
        elif Cache.current_title_info == '学生课表查询':
            self.stackedWidget.setCurrentIndex(2)
            self.lab_title_info.setText("学生课表查询")#设置标题
            self.label_89.setText("学号:"+Cache.current_user)
            self.clear_tableview(self.tableView_4)
        elif Cache.current_title_info == '查询空闲教室':
            self.stackedWidget.setCurrentIndex(3)
            self.lab_title_info.setText("查询空闲教室")  # 设置标题
            self.Get_storied_building_num("东校区")
        elif Cache.current_title_info == '选课名单查询':
            self.stackedWidget.setCurrentIndex(4)
            self.cob_colleg.clear()
            self.cob_colleg.addItems(Cache.current_college)
            self.lab_title_info.setText("选课名单查询")  # 设置标题
            self.clear_tableview(self.tableView_7)  # 清空表格
            # 按钮回归初始化
            self.pushButton_29.setEnabled(False)
            self.pushButton_27.setEnabled(False)
            self.pushButton_26.setEnabled(True)
            self.pushButton_28.setEnabled(True)
            self.lineEdit_8.setText("1")
            self.label_115.setText("共 0 页")
            self.label_87.setText("")
        elif Cache.current_title_info == '重修课程查询':
            self.stackedWidget.setCurrentIndex(5)
            self.cob_Rebuild_course_College.clear()
            self.cob_Rebuild_course_College.addItems(Cache.current_college)
            self.lab_title_info.setText("重修课程查询")  # 设置标题
            self.clear_tableview(self.tableView_8)#清空表格
            # 按钮回归初始化
            self.pushButton_32.setEnabled(False)
            self.pushButton_31.setEnabled(False)
            self.pushButton_33.setEnabled(True)
            self.pushButton_30.setEnabled(True)
            self.lineEdit_9.setText("1")
            self.label_128.setText("共 0 页")
        elif Cache.current_title_info == '学生成绩查询':
            self.stackedWidget.setCurrentIndex(6)
            self.lab_title_info.setText("学生成绩查询")  # 设置标题
            self.clear_tableview(self.tableView_9)#清空表格
            #按钮回归初始化
            self.pushButton_37.setEnabled(False)
            self.pushButton_38.setEnabled(False)
            self.pushButton_39.setEnabled(True)
            self.pushButton_40.setEnabled(True)
            self.lineEdit_10.setText("1")
            self.label_129.setText("共 0 页")
            self.label_160.setText("")
        elif Cache.current_title_info == '学生学业情况查询':
            self.stackedWidget.setCurrentIndex(7)
            self.lab_title_info.setText("学生学业情况查询")  # 设置标题
            self.Get_Stu_jd()#获取绩点
            self.Set_kz_info()#设置课组信息
        elif Cache.current_title_info == '学生成绩总表打印':
            self.stackedWidget.setCurrentIndex(8)
            self.lab_title_info.setText("学生成绩总表打印")  # 设置标题
        elif Cache.current_title_info == '教学执行计划查看':
            self.stackedWidget.setCurrentIndex(9)
            self.lab_title_info.setText("教学执行计划查看")  # 设置标题
            self.cob_school_year_31.clear()
            self.cob_school_year_31.addItems(Cache.current_college)
    #清空表格
    def clear_tableview(self,tableView):
        model = QStandardItemModel(tableView)
        model.clear()
        tableView.setModel(model)
    #设置推荐课表打印页面
    def Set_curriculum_print_page(self):
        self.lab_title_info.setText("推荐课表打印")
        school_year_list, semester_list, Campus_list, grade_list, College_list,College_code_list=APITool.Get_curriculum_print_info()
        #设置下拉列表(先清空在添加 防止重复)
        self.cob_school_year.clear()
        self.cob_semester.clear()
        self.cob_Campus.clear()
        self.cob_grade.clear()
        self.cob_College.clear()
        self.cob_school_year.addItems(school_year_list)
        self.cob_school_year.setCurrentIndex(2)
        self.cob_semester.addItems(semester_list)
        self.cob_Campus.addItems(Campus_list)
        self.cob_Campus.setCurrentIndex(2)
        self.cob_grade.addItems(grade_list)
        self.cob_College.addItems(College_list)
        #设置相关表头
        headers = ['课表名称', '学院', '年级', '专业', '班级']
        model = QStandardItemModel(self.tableView_3)
        model.setColumnCount(len(headers))
        for idx, title in enumerate(headers):  # 设置退课视图的数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        self.tableView_3.setModel(model)
    #获取课表打印页面的相关专业和班级
    def Get_Curriculum_class_and_profession(self,string):
        #if self.cob_grade.#未完待续。。。。。。。
        school_year_list, semester_list, Campus_list, grade_list, College_list, College_dict = APITool.Get_curriculum_print_info()
        res_list=APITool.Get_detailed_curriculum_print_info(College_dict[self.cob_College.currentText()],self.cob_grade.currentText())
        self.cob_class.clear()
        self.cob_class.addItems(res_list)
    #当前tabWidget点击的页面
    def Current_page_info(self,index):
        #点击成绩页面
        if index==5:
            self.current_grade_page = 1
            self.current_grade_time = 0
            self.Set_Grade_Page()
        #点击选课信息页面
        elif index==6:
            self.Set_Course_Page()
        else:
            self.tableView_Grade_info.clearSpans()
            self.tableView_select_course.clearSpans()
    #设置成绩页面
    def Set_Grade_Page(self):
        self.btn_course_info_first.setEnabled(False)
        self.btn_course_info_front.setEnabled(False)
        self.btn_course_info_next.setEnabled(True)
        self.btn_course_info_end.setEnabled(True)
        res_list, total_page_res, total_Numberofpieces = APITool.Get_MY_GRADE_INFO('15', '1', '0')  # 内容信息
        self.current_grade_page=1
        headers = ['学年', '学期', '课程代码', '课程名称', '学分', '成绩', '考试性质', '绩点', '课程性质', '成绩备注']  # 表头信息
        width_list = [133, 81, 117, 157, 100, 110, 126, 102, 101, 160]  # 表格宽度
        self.Set_table_view(headers, self.tableView_Grade_info, res_list, width_list)
        self.lab_course_info_total_page.setText("共 "+str(total_page_res)+" 页")
        self.label_70.setText("共 "+str(total_Numberofpieces)+" 条")
        self.led_current_page.setText("1")
        if str(total_page_res)=='1':
            self.btn_course_info_next.setEnabled(False)
            self.btn_course_info_end.setEnabled(False)
    #设置课程页面
    def Set_Course_Page(self):
        self.btn_select_course_next.setEnabled(True)
        self.btn_select_course_end.setEnabled(True)
        res_list, total_page_res, total_Numberofpieces = APITool.Get_MY_CROUSE_INFO('15','1','0')
        headers = ['学年', '学期', '课程名称', '开课院系', '课程类别', '学分', '教学班名称', '教师', '上课时间', '上课地点']  # 表头信息
        width_list = [133, 81, 117, 157, 100, 110, 126, 102, 101, 160]  # 表格宽度
        self.Set_table_view_no_width(headers, self.tableView_select_course, res_list)
        self.lab_select_course_total_page.setText("共 " + str(total_page_res) + " 页")
        self.label_74.setText("共 " + str(total_Numberofpieces) + " 条")
        self.led_btn_select_course_current_page.setText("1")
        #判断页数
        if str(total_page_res)=="1":
            self.btn_select_course_first.setEnabled(False)
            self.btn_select_course_front.setEnabled(False)
            self.btn_select_course_next.setEnabled(False)
            self.btn_select_course_end.setEnabled(False)
        #设置显示列宽
        self.tableView_select_course.setColumnWidth(0,120)
        self.tableView_select_course.setColumnWidth(1, 83)
        self.tableView_select_course.setColumnWidth(2, 233)
        self.tableView_select_course.setColumnWidth(3, 123)
        self.tableView_select_course.setColumnWidth(4, 103)
        self.tableView_select_course.setColumnWidth(5, 73)
        self.tableView_select_course.setColumnWidth(6, 142)
        self.tableView_select_course.setColumnWidth(7, 72)
        self.tableView_select_course.setColumnWidth(8, 132)
        self.tableView_select_course.setColumnWidth(9, 127)
    #设置个人信息
    def Set_My_Info(self):
        res_dict = APITool.Get_detailed_My_Info()
        #print(res_dict)
        res_value=[]#进行转化
        for each in res_dict.values():
            if each=='None':
                res_value.append('')
            else:
                res_value.append(each)
        #设置基本信息
        self.lab_student_number.setText(res_value[0])
        self.lab_stu_name.setText(res_value[1])
        self.lab_stu_name_pinyin.setText(res_value[2])
        self.lab_stu_old_name.setText(res_value[3])
        self.lab_stu_english_name.setText(res_value[4])
        self.lab_stu_sex.setText(res_value[5])
        self.lab_stu_ID_type.setText(res_value[6])
        self.lab_stu_ID.setText(res_value[7])
        self.lab_date_of_birth.setText(res_value[8])
        self.lab_nation.setText(res_value[9])
        self.lab_stu_political_face.setText(res_value[10])
        self.lab_Entry_date.setText(res_value[11])
        self.lab_Birthplace.setText(res_value[12])
        self.lab_Account.setText(' ')#res_value[13]
        self.lab_stu_type.setText(' ')#res_velue[14]
        self.lab_grade.setText(res_value[13])#res_velue[15]
        self.lab_xueyuan_name.setText(res_value[14])
        self.lab_dept_name.setText(' ')
        self.lab_profession_name.setText(res_value[15])
        self.lab_Professional_direction.setText(res_value[16])
        self.lab_class_name.setText(res_value[17])
        self.lab_School_system.setText(res_value[18])
        self.lab_school_roll_st.setText(res_value[19])
        '''self.lab_is_school.setText(res_value[23])
self.lab_Registration_status.setText(res_value[24])
self.lab_Registration_note.setText(res_value[25])
self.lab_close_Registration_note.setText(res_value[26])
self.lab_baodao_time.setText(res_value[27])
self.lab_Registration_time.setText(res_value[28])
self.lab_Not_register_reason.setText(res_value[29])
self.lab_Unregistered_reason.setText(res_value[30])
self.lab_Education_level.setText(res_value[31])
self.lab_Training_method.setText(res_value[32])'''
        self.lab_Training_level.setText(res_value[20])
        #self.lab_student_type.setText(res_value[34])
        self.lab_Admissions_quarter.setText(res_value[21])
        #self.lab_depth.setText(res_value[36])
        self.lab_Admissions_profession.setText(res_value[22])
        self.lab_Admission_year.setText(res_value[23])
        self.lab_Candidate_number.setText(res_value[24])
        #self.lab_Candidate_type.setText(res_value[40])
        self.lab_Graduation_school.setText(res_value[25])
        '''self.lab_stu_id.setText(res_value[42])
        self.lab_Specialty.setText(res_value[43])
        self.lab_physical_condition.setText(res_value[44])
        self.lab_Admission_method.setText(res_value[45])'''
        self.lab_Total_enrollment.setText(res_value[26])
        #self.lab_test_id.setText(res_value[47])
        self.lab_train_Interval.setText(res_value[27])
        '''self.lab_Length_of_study.setText(res_value[49])
        self.lab_mark.setText(res_value[50])
        self.lab_email.setText(res_value[51])
        self.lab_iphone.setText(res_value[52])
        self.lab_kuding_iphone.setText(res_value[53])
        self.lab_family_dizhi.setText(res_value[54])
        self.lab_mailing_address.setText(res_value[55])
        self.lab_QQ_num.setText(res_value[56])
        self.lab_family_iphone.setText(res_value[57])
        self.lab_Postal_code.setText(res_value[58])'''

        #个人照片
        pixmap = QPixmap(Config.Get_img_file_path())
        self.lab_my_img.setPixmap(pixmap)

        #设置头部信息
        self.lab_sno.setText("学号：  "+res_value[0])
        self.lab_sname.setText("姓名：  "+res_value[1])

        #设置导向信息
        self.lab_title_info.setText(Cache.current_title_info)
    #设置奖罚信息
    def Set_Bonus_Info(self):
        headers=['学年','学期','奖励项目','奖励级别','奖励等级','奖励方式','获奖类别','获奖类型','奖励金额']
        model = QStandardItemModel(self.tableView)
        model.setColumnCount(len(headers))
        for idx, title in enumerate(headers):  # 设置退课视图的数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        headers2 = ['学年', '学期', '处分名称', '处分日期', '违纪类别', '违纪日期', '处分撤销时间', '处分撤销文号', '处分撤销原因']
        model2 = QStandardItemModel(self.tableView)
        model2.setColumnCount(len(headers2))
        for idx, title in enumerate(headers2):  # 设置退课视图的数据头
            model2.setHeaderData(idx, Qt.Horizontal, title)
        self.tableView.setModel(model)
        self.tableView_2.setModel(model2)
    #设置学籍异动
    def Set_school_roll_status(self):
        headers = ['学年', '学期', '奖励项目', '奖励级别', '奖励等级', '奖励方式', '获奖类别', '获奖类型', '奖励金额']
        model = QStandardItemModel(self.tableView)
        model.setColumnCount(len(headers))
        for idx, title in enumerate(headers):  # 设置退课视图的数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        self.tableView_5.setModel(model)
    #设置表格视图
    def Set_table_view(self,headrs,tableview,res_list,width_list):
        model = QStandardItemModel(tableview)
        model.setColumnCount(len(headrs))  # 设置列数
        for idx, title in enumerate(headrs):  # 添加数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        for row in range(len(res_list) // len(headrs)):  # 设置成绩的详细数据
            for col in range(len(headrs)):
                model.setItem(row, col, QStandardItem(res_list[row * len(headrs) + col]))
        tableview.setModel(model)
        tableview.setColumnWidth(0, width_list[0])
        tableview.setColumnWidth(1, width_list[1])
        tableview.setColumnWidth(2, width_list[2])
        tableview.setColumnWidth(3, width_list[3])
        tableview.setColumnWidth(4, width_list[4])
        tableview.setColumnWidth(5, width_list[5])
        tableview.setColumnWidth(6, width_list[6])
        tableview.setColumnWidth(7, width_list[7])
        tableview.setColumnWidth(8, width_list[8])
        tableview.setColumnWidth(9, width_list[9])
    # 设置表格视图五宽度
    def Set_table_view_no_width(self, headrs, tableview, res_list):
        model = QStandardItemModel(tableview)
        model.setColumnCount(len(headrs))  # 设置列数
        for idx, title in enumerate(headrs):  # 添加数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        for row in range(len(res_list) // len(headrs)):  # 设置成绩的详细数据
            for col in range(len(headrs)):
                model.setItem(row, col, QStandardItem(res_list[row * len(headrs) + col]))
        tableview.setModel(model)
    # 返回主页
    def return_home(self):
        self.close()
        self.success_return.emit()  # 发送成功信号
    #返回首页(成绩信息)
    def Get_First_Grade_info(self):
        self.btn_course_info_first.setEnabled(False)
        self.btn_course_info_front.setEnabled(False)
        self.btn_course_info_next.setEnabled(True)
        self.btn_course_info_end.setEnabled(True)
        #res_list, total_page_res_temp, total_Numberofpieces_temp = APITool.Get_MY_GRADE_INFO('15', '1', '0')  # 内容信息

        self.current_grade_page = 1
        self.current_grade_time = 0
        self.led_current_page.setText("1")
        res_list, total_page_res, total_Numberofpieces = APITool.Get_MY_GRADE_INFO(
            str(self.combox_current_page.currentText()), str(self.current_grade_page),
            str(self.current_grade_time))  # 内容信息

        headers = ['学年', '学期', '课程代码', '课程名称', '学分', '成绩', '考试性质', '绩点', '课程性质', '成绩备注']  # 表头信息
        width_list = [133, 81, 117, 157, 100, 110, 126, 102, 101, 160]  # 表格宽度
        self.Set_table_view(headers, self.tableView_Grade_info, res_list, width_list)
        self.lab_course_info_total_page.setText("共 " + str(total_page_res) + " 页")
        self.label_70.setText("共 " + str(total_Numberofpieces) + " 条")
    #上一页(成绩信息)
    def Get_Front_Grade_info(self):
        self.btn_course_info_next.setEnabled(True)
        self.btn_course_info_end.setEnabled(True)
        print(self.current_grade_page,self.current_grade_time)
        self.current_grade_page -= 1
        self.current_grade_time -= 1
        self.led_current_page.setText(str(self.current_grade_page))
        res_list, total_page_res, total_Numberofpieces = APITool.Get_MY_GRADE_INFO(
            str(self.combox_current_page.currentText()), str(self.current_grade_page),
            str(self.current_grade_time))  # 内容信息
        headers = ['学年', '学期', '课程代码', '课程名称', '学分', '成绩', '考试性质', '绩点', '课程性质', '成绩备注']  # 表头信息
        width_list = [133, 81, 117, 157, 100, 110, 126, 102, 101, 160]  # 表格宽度
        self.Set_table_view(headers, self.tableView_Grade_info, res_list, width_list)
        self.lab_course_info_total_page.setText("共 " + str(total_page_res) + " 页")
        self.label_70.setText("共 " + str(total_Numberofpieces) + " 条")
        if (str(self.current_grade_page) == "1"):
            self.btn_course_info_first.setEnabled(False)
            self.btn_course_info_front.setEnabled(False)
            self.btn_course_info_next.setEnabled(True)
            self.btn_course_info_end.setEnabled(True)
    #下一页(成绩信息)
    def Get_Next_Grade_info(self):
        self.btn_course_info_first.setEnabled(True)
        self.btn_course_info_front.setEnabled(True)
        self.current_grade_page+=1
        self.current_grade_time+=1
        self.led_current_page.setText(str(self.current_grade_page))
        res_list, total_page_res, total_Numberofpieces = APITool.Get_MY_GRADE_INFO(str(self.combox_current_page.currentText()), str(self.current_grade_page), str(self.current_grade_time))  # 内容信息
        headers = ['学年', '学期', '课程代码', '课程名称', '学分', '成绩', '考试性质', '绩点', '课程性质', '成绩备注']  # 表头信息
        width_list = [133, 81, 117, 157, 100, 110, 126, 102, 101, 160]  # 表格宽度
        self.Set_table_view(headers, self.tableView_Grade_info, res_list, width_list)
        self.lab_course_info_total_page.setText("共 " + str(total_page_res) + " 页")
        self.label_70.setText("共 " + str(total_Numberofpieces) + " 条")
        if(str(self.current_grade_page)==str(total_page_res)):
            self.btn_course_info_first.setEnabled(True)
            self.btn_course_info_front.setEnabled(True)
            self.btn_course_info_next.setEnabled(False)
            self.btn_course_info_end.setEnabled(False)
    #返回尾页(成绩信息)
    def Get_End_Grade_info(self):
        self.btn_course_info_first.setEnabled(True)
        self.btn_course_info_front.setEnabled(True)
        self.btn_course_info_next.setEnabled(False)
        self.btn_course_info_end.setEnabled(False)
        res_list, total_page_res_temp, total_Numberofpieces_temp = APITool.Get_MY_GRADE_INFO(str(self.combox_current_page.currentText()), '1', '0')  # 内容信息

        self.current_grade_page = int(total_page_res_temp)
        self.current_grade_time = int(int(total_page_res_temp)-1)
        self.led_current_page.setText(str(self.current_grade_page))
        res_list, total_page_res, total_Numberofpieces = APITool.Get_MY_GRADE_INFO(
            str(self.combox_current_page.currentText()), str(self.current_grade_page),
            str(self.current_grade_time))  # 内容信息

        headers = ['学年', '学期', '课程代码', '课程名称', '学分', '成绩', '考试性质', '绩点', '课程性质', '成绩备注']  # 表头信息
        width_list = [133, 81, 117, 157, 100, 110, 126, 102, 101, 160]  # 表格宽度
        self.Set_table_view(headers, self.tableView_Grade_info, res_list, width_list)
        self.lab_course_info_total_page.setText("共 " + str(total_page_res) + " 页")
        self.label_70.setText("共 " + str(total_Numberofpieces) + " 条")
    #获取显示页数(成绩信息)
    def Get_Grade_info_page(self,string):
        self.led_current_page.setText(str(1))
        res_list, total_page_res, total_Numberofpieces = APITool.Get_MY_GRADE_INFO(
            str(self.combox_current_page.currentText()), "1",
            "0")  # 内容信息
        headers = ['学年', '学期', '课程代码', '课程名称', '学分', '成绩', '考试性质', '绩点', '课程性质', '成绩备注']  # 表头信息
        width_list = [133, 81, 117, 157, 100, 110, 126, 102, 101, 160]  # 表格宽度
        self.Set_table_view(headers, self.tableView_Grade_info, res_list, width_list)
        self.lab_course_info_total_page.setText("共 " + str(total_page_res) + " 页")
        self.label_70.setText("共 " + str(total_Numberofpieces) + " 条")
        if str(total_page_res)=="1":
            self.btn_course_info_first.setEnabled(False)
            self.btn_course_info_front.setEnabled(False)
            self.btn_course_info_next.setEnabled(False)
            self.btn_course_info_end.setEnabled(False)
        else:
            self.btn_course_info_first.setEnabled(False)
            self.btn_course_info_front.setEnabled(False)
            self.btn_course_info_next.setEnabled(True)
            self.btn_course_info_end.setEnabled(True)
    # 返回首页(课程信息)
    def Get_First_Course_info(self):
        pass

    # 上一页(课程信息)
    def Get_Front_Course_info(self):
        pass

    # 下一页(课程信息)
    def Get_Next_Course_info(self):
        pass

    # 返回尾页(课程信息)
    def Get_End_Course_info(self):
        pass

    # 获取显示页数(课程信息)
    def Get_Course_Current_page_info(self,string):
        pass

    #查询课表打印
    def Query_course_print_info(self):
        QMessageBox.question(self, '提示', '当前无信息可查询', QMessageBox.Ok)

    #导出课表打印
    def Exoprt_couser_print_info(self):
        QMessageBox.question(self, '警告提示', '请选择至少一条记录', QMessageBox.Ok)

    #查询课表
    def query_course(self):
        headrs=['节次','星期一','星期二','星期三','星期四','星期五','星期六','星期天']
        model = QStandardItemModel(self.tableView_4)
        model.setColumnCount(len(headrs))  # 设置列数
        model.setRowCount(10)#设置行数
        for idx, title in enumerate(headrs):  # 添加数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        res_list, kb_jc_list,xq_list=APITool.Get_Query_Course_Info(self.cob_stu_course_school_year.currentText()[:4],self.cob_stu_course_semester.currentText())
        #进行课表填充
        #print(res_list)
        for i in range(len(xq_list)):
            if kb_jc_list[i]=='1-2节' and xq_list[i]=='星期一':
                model.setItem(0, 1, QStandardItem(res_list[i]))
                model.setItem(1, 1, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='3-4节' and xq_list[i]=='星期一':
                model.setItem(2, 1, QStandardItem(res_list[i]))
                model.setItem(3, 1, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='5-6节' and xq_list[i]=='星期一':
                model.setItem(4, 1, QStandardItem(res_list[i]))
                model.setItem(5, 1, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='7-8节' and xq_list[i]=='星期一':
                model.setItem(6, 1, QStandardItem(res_list[i]))
                model.setItem(7, 1, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='9-10节' and xq_list[i]=='星期一':
                model.setItem(8, 1, QStandardItem(res_list[i]))
                model.setItem(9, 1, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='1-2节' and xq_list[i]=='星期二':
                model.setItem(0, 2, QStandardItem(res_list[i]))
                model.setItem(1, 2, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='3-4节' and xq_list[i]=='星期二':
                model.setItem(2, 2, QStandardItem(res_list[i]))
                model.setItem(3, 2, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='5-6节' and xq_list[i]=='星期二':
                model.setItem(4, 2, QStandardItem(res_list[i]))
                model.setItem(5, 2, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='7-8节' and xq_list[i]=='星期二':
                model.setItem(6, 2, QStandardItem(res_list[i]))
                model.setItem(7, 2, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='9-10节' and xq_list[i]=='星期二':
                model.setItem(8, 2, QStandardItem(res_list[i]))
                model.setItem(9, 2, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='1-2节' and xq_list[i]=='星期三':
                model.setItem(0, 3, QStandardItem(res_list[i]))
                model.setItem(1, 3, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='3-4节' and xq_list[i]=='星期三':
                model.setItem(2, 3, QStandardItem(res_list[i]))
                model.setItem(3, 3, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='5-6节' and xq_list[i]=='星期三':
                model.setItem(4, 3, QStandardItem(res_list[i]))
                model.setItem(5, 3, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='7-8节' and xq_list[i]=='星期三':
                model.setItem(6, 3, QStandardItem(res_list[i]))
                model.setItem(7, 3, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='9-10节' and xq_list[i]=='星期三':
                model.setItem(8, 3, QStandardItem(res_list[i]))
                model.setItem(9, 3, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='1-2节' and xq_list[i]=='星期四':
                model.setItem(0, 4, QStandardItem(res_list[i]))
                model.setItem(1, 4, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='3-4节' and xq_list[i]=='星期四':
                model.setItem(2, 4, QStandardItem(res_list[i]))
                model.setItem(3, 4, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='5-6节' and xq_list[i]=='星期四':
                model.setItem(4, 4, QStandardItem(res_list[i]))
                model.setItem(5, 4, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='7-8节' and xq_list[i]=='星期四':
                model.setItem(6, 4, QStandardItem(res_list[i]))
                model.setItem(7, 4, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='9-10节' and xq_list[i]=='星期四':
                model.setItem(8, 4, QStandardItem(res_list[i]))
                model.setItem(9, 4, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='1-2节' and xq_list[i]=='星期五':
                model.setItem(0, 5, QStandardItem(res_list[i]))
                model.setItem(1, 5, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='3-4节' and xq_list[i]=='星期五':
                model.setItem(2, 5, QStandardItem(res_list[i]))
                model.setItem(3, 5, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='5-6节' and xq_list[i]=='星期五':
                model.setItem(4, 5, QStandardItem(res_list[i]))
                model.setItem(5, 5, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='7-8节' and xq_list[i]=='星期五':
                model.setItem(6, 5, QStandardItem(res_list[i]))
                model.setItem(7, 5, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='9-10节' and xq_list[i]=='星期五':
                model.setItem(8, 5, QStandardItem(res_list[i]))
                model.setItem(9, 5, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='1-2节' and xq_list[i]=='星期六':
                model.setItem(0, 6, QStandardItem(res_list[i]))
                model.setItem(1, 6, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='3-4节' and xq_list[i]=='星期六':
                model.setItem(2, 6, QStandardItem(res_list[i]))
                model.setItem(3, 6, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='5-6节' and xq_list[i]=='星期六':
                model.setItem(4, 6, QStandardItem(res_list[i]))
                model.setItem(5, 6, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='7-8节' and xq_list[i]=='星期六':
                model.setItem(6, 6, QStandardItem(res_list[i]))
                model.setItem(7, 6, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='9-10节' and xq_list[i]=='星期六':
                model.setItem(8, 6, QStandardItem(res_list[i]))
                model.setItem(9, 6, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='1-2节' and xq_list[i]=='星期天':
                model.setItem(0, 7, QStandardItem(res_list[i]))
                model.setItem(1, 7, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='3-4节' and xq_list[i]=='星期天':
                model.setItem(2, 7, QStandardItem(res_list[i]))
                model.setItem(3, 7, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='5-6节' and xq_list[i]=='星期天':
                model.setItem(4, 7, QStandardItem(res_list[i]))
                model.setItem(5, 7, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='7-8节' and xq_list[i]=='星期天':
                model.setItem(6, 7, QStandardItem(res_list[i]))
                model.setItem(7, 7, QStandardItem(res_list[i]))
            elif kb_jc_list[i]=='9-10节' and xq_list[i]=='星期天':
                model.setItem(8, 7, QStandardItem(res_list[i]))
                model.setItem(9, 7, QStandardItem(res_list[i]))
        #设置节次
        model.setItem(0, 0, QStandardItem("第一节(8:00-8:50)"))
        model.setItem(1, 0, QStandardItem("第二节(9:00-9:50)"))
        model.setItem(2, 0, QStandardItem("第三节(10:00-10:50)"))
        model.setItem(3, 0, QStandardItem("第四节(11:00-11:50)"))
        model.setItem(4, 0, QStandardItem("第五节(14:00-14:50)"))
        model.setItem(5, 0, QStandardItem("第六节(15:00-15:50)"))
        model.setItem(6, 0, QStandardItem("第七节(16:00-16:50)"))
        model.setItem(7, 0, QStandardItem("第八节(17:00-17:50)"))
        model.setItem(8, 0, QStandardItem("第九节(19:00-19:50)"))
        model.setItem(9, 0, QStandardItem("第十节(20:00-20:50)"))
        self.tableView_4.setModel(model)

        #设置表格行高和行宽
        self.tableView_4.verticalHeader().setDefaultSectionSize(120)
        self.tableView_4.horizontalHeader().setDefaultSectionSize(149)

    #查询空闲教室
    def query_empty_classroom(self):
        QMessageBox.warning(self, "提示", "该学年学期场地预约尚未\n开放申请,请联系相关\n管理人员")
    #获取空闲教室的楼号
    def Get_storied_building_num(self,string):
        self.cob_storied_building_num.clear()
        if string=="东校区":
            res_list=['东1号教学楼','东2号教学楼','东3号教学楼','东4号教学楼','东5号教学楼','东6号教学楼','东校体育场馆','东校逸夫图书馆','无楼号']
            self.cob_storied_building_num.addItems(res_list)
        elif string=="西校区":
            res_list = ['西10号教学楼', '西11号教学楼', '西1号教学楼', '西2号教学楼', '西3号教学楼', '西4号教学楼', '西5号教学楼', '西6号教学楼', '西7号教学楼', '西8号教学楼', '西9号教学楼','西校体育场馆', '西校图书馆','西校综合实验楼','无楼号']
            self.cob_storied_building_num.addItems(res_list)
    #选课名单查询
    def Query_select_course_list(self):
        headrs = ['选课来源','学年','学期','课程代码','课程名称','课程归属','开课学院','学分','学号','姓名','身份证号码','选修类型','开课状态	','任课教师','上课时间','上课地点','起始结束周','教学项目报名项','校区','课程类别','课程性质','开课类型','教学班','选课时间', '性别', '学院', '年级', '专业', '班级']
        res_list, total_page_res, total_Numberofpieces=APITool.Get_select_course_list(self.cob_select_course_school_year.currentText()[:4],self.cob_select_course_semester.currentText())
        self.label_115.setText("共 "+str(total_page_res)+" 页")
        self.label_87.setText("共"+str(total_Numberofpieces)+"条")
        self.Set_table_view_no_width(headrs,self.tableView_7,res_list)#设置表格内容
        self.tableView_7.verticalHeader().setDefaultSectionSize(50)#设置整体表格行高
    #查询重修课程
    def Query_Rebuild_course(self):
        headrs = ['重修学年	','重修学期	','课程代码	','课程名称	','学分	','开课学院','课程类别	','重修状态']

    #查询学生成绩
    def Query_Stu_score_info(self):
        self.pushButton_37.setEnabled(False)
        self.pushButton_38.setEnabled(False)
        self.pushButton_39.setEnabled(True)
        self.pushButton_40.setEnabled(True)
        self.current_stu_sroce_page = 1
        res_list, total_page_res, total_Numberofpieces=APITool.Get_Stu_score_info(self.cob_stu_score_school_year.currentText()[:4],self.cob_stu_score_semester.currentText(),'15','1')
        headrs = [ '学年','学期', '课程代码',	'课程名称', '课程性质', '学分', '成绩','成绩备注',	'绩点', '成绩性质',	 '是否成绩作废','是否学位课程', '开课学院', '课程标记', '课程类别','课程归属', '教学班','任课教师','学号','姓名', '性别', '学生类别',	 '学院', '专业', '年级', '班级']
        self.label_129.setText("共 " + str(total_page_res) + " 页")
        self.label_160.setText("共" + str(total_Numberofpieces) + "条")
        self.Set_table_view_no_width(headrs, self.tableView_9, res_list)  # 设置表格内容
        self.tableView_9.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高
        if str(total_page_res)=="1":
            self.pushButton_37.setEnabled(False)
            self.pushButton_38.setEnabled(False)
            self.pushButton_39.setEnabled(False)
            self.pushButton_40.setEnabled(False)
    #查询学生成绩更多页
    def Stu_score_more_page(self,string):
        self.pushButton_37.setEnabled(False)
        self.pushButton_38.setEnabled(False)
        self.pushButton_39.setEnabled(True)
        self.pushButton_40.setEnabled(True)
        self.current_stu_sroce_page = 1
        self.lineEdit_10.setText("1")
        res_list, total_page_res, total_Numberofpieces = APITool.Get_Stu_score_info(
            self.cob_stu_score_school_year.currentText()[:4], self.cob_stu_score_semester.currentText(), string,'1')
        headrs = ['学年', '学期', '课程代码', '课程名称', '课程性质', '学分', '成绩', '成绩备注', '绩点', '成绩性质', '是否成绩作废', '是否学位课程', '开课学院',
                  '课程标记', '课程类别', '课程归属', '教学班', '任课教师', '学号', '姓名', '性别', '学生类别', '学院', '专业', '年级', '班级']
        self.label_129.setText("共 " + str(total_page_res) + " 页")
        self.label_160.setText("共" + str(total_Numberofpieces) + "条")
        self.Set_table_view_no_width(headrs, self.tableView_9, res_list)  # 设置表格内容
        self.tableView_9.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高
        if str(total_page_res)=="1":
            self.pushButton_37.setEnabled(False)
            self.pushButton_38.setEnabled(False)
            self.pushButton_39.setEnabled(False)
            self.pushButton_40.setEnabled(False)
    #学生成绩下一页
    def Get_Next_Stu_Score(self):
        self.pushButton_37.setEnabled(True)
        self.pushButton_38.setEnabled(True)
        self.current_stu_sroce_page+=1
        res_list, total_page_res, total_Numberofpieces = APITool.Get_Stu_score_info(
            self.cob_stu_score_school_year.currentText()[:4], self.cob_stu_score_semester.currentText(), self.comboBox_13.currentText(),str(self.current_stu_sroce_page))
        headrs = ['学年', '学期', '课程代码', '课程名称', '课程性质', '学分', '成绩', '成绩备注', '绩点', '成绩性质', '是否成绩作废', '是否学位课程', '开课学院',
                  '课程标记', '课程类别', '课程归属', '教学班', '任课教师', '学号', '姓名', '性别', '学生类别', '学院', '专业', '年级', '班级']
        self.label_129.setText("共 " + str(total_page_res) + " 页")
        self.label_160.setText("共" + str(total_Numberofpieces) + "条")
        self.lineEdit_10.setText(str(self.current_stu_sroce_page))
        self.Set_table_view_no_width(headrs, self.tableView_9, res_list)  # 设置表格内容
        self.tableView_9.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高
        if str(self.current_stu_sroce_page)==str(total_page_res):
            self.pushButton_37.setEnabled(True)
            self.pushButton_38.setEnabled(True)
            self.pushButton_39.setEnabled(False)
            self.pushButton_40.setEnabled(False)
    #学生成绩尾页
    def Get_End_Stu_Score(self):
        self.pushButton_37.setEnabled(True)
        self.pushButton_38.setEnabled(True)
        self.pushButton_39.setEnabled(False)
        self.pushButton_40.setEnabled(False)
        res_list, total_page_res, total_Numberofpieces = APITool.Get_Stu_score_info(
            self.cob_stu_score_school_year.currentText()[:4], self.cob_stu_score_semester.currentText(),
            self.comboBox_13.currentText(), str("1"))
        self.current_stu_sroce_page=int(total_page_res)
        res_list, total_page_res, total_Numberofpieces = APITool.Get_Stu_score_info(
            self.cob_stu_score_school_year.currentText()[:4], self.cob_stu_score_semester.currentText(),
            self.comboBox_13.currentText(), str(self.current_stu_sroce_page))
        headrs = ['学年', '学期', '课程代码', '课程名称', '课程性质', '学分', '成绩', '成绩备注', '绩点', '成绩性质', '是否成绩作废', '是否学位课程', '开课学院',
                  '课程标记', '课程类别', '课程归属', '教学班', '任课教师', '学号', '姓名', '性别', '学生类别', '学院', '专业', '年级', '班级']
        self.label_129.setText("共 " + str(total_page_res) + " 页")
        self.label_160.setText("共" + str(total_Numberofpieces) + "条")
        self.lineEdit_10.setText(str(self.current_stu_sroce_page))
        self.Set_table_view_no_width(headrs, self.tableView_9, res_list)  # 设置表格内容
        self.tableView_9.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高
    #学生成绩上一页
    def Get_Front_Stu_Score(self):
        self.pushButton_39.setEnabled(True)
        self.pushButton_40.setEnabled(True)
        self.current_stu_sroce_page -= 1
        res_list, total_page_res, total_Numberofpieces = APITool.Get_Stu_score_info(
            self.cob_stu_score_school_year.currentText()[:4], self.cob_stu_score_semester.currentText(),
            self.comboBox_13.currentText(), str(self.current_stu_sroce_page))
        headrs = ['学年', '学期', '课程代码', '课程名称', '课程性质', '学分', '成绩', '成绩备注', '绩点', '成绩性质', '是否成绩作废', '是否学位课程', '开课学院',
                  '课程标记', '课程类别', '课程归属', '教学班', '任课教师', '学号', '姓名', '性别', '学生类别', '学院', '专业', '年级', '班级']
        self.label_129.setText("共 " + str(total_page_res) + " 页")
        self.label_160.setText("共" + str(total_Numberofpieces) + "条")
        self.lineEdit_10.setText(str(self.current_stu_sroce_page))
        self.Set_table_view_no_width(headrs, self.tableView_9, res_list)  # 设置表格内容
        self.tableView_9.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高
        if self.lineEdit_10.text()=="1":
            self.pushButton_37.setEnabled(False)
            self.pushButton_38.setEnabled(False)
            self.pushButton_39.setEnabled(True)
            self.pushButton_40.setEnabled(True)
    #学生成绩首页
    def Get_Frist_Stu_Score(self):
        self.pushButton_37.setEnabled(False)
        self.pushButton_38.setEnabled(False)
        self.pushButton_39.setEnabled(True)
        self.pushButton_40.setEnabled(True)
        self.current_stu_sroce_page = 1
        self.lineEdit_10.setText(str(self.current_stu_sroce_page))
        res_list, total_page_res, total_Numberofpieces = APITool.Get_Stu_score_info(
            self.cob_stu_score_school_year.currentText()[:4], self.cob_stu_score_semester.currentText(),self.comboBox_13.currentText() , '1')
        headrs = ['学年', '学期', '课程代码', '课程名称', '课程性质', '学分', '成绩', '成绩备注', '绩点', '成绩性质', '是否成绩作废', '是否学位课程', '开课学院',
                  '课程标记', '课程类别', '课程归属', '教学班', '任课教师', '学号', '姓名', '性别', '学生类别', '学院', '专业', '年级', '班级']
        self.label_129.setText("共 " + str(total_page_res) + " 页")
        self.label_160.setText("共" + str(total_Numberofpieces) + "条")
        self.Set_table_view_no_width(headrs, self.tableView_9, res_list)  # 设置表格内容
        self.tableView_9.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高
    #获取学生绩点
    def Get_Stu_jd(self):
        res=APITool.Get_Stu_Jd()
        self.lab_jd.setText(res)
    #设置课组信息
    def Set_kz_info(self):
        # 设置treewidget控件全部展开
        self.treeWidget.expandAll()
        #设置宽度
        self.treeWidget.setColumnWidth(0,790)

    #教学计划信息查询
    def Query_teaching_paln_info(self):
        self.pushButton_50.setEnabled(False)
        self.pushButton_49.setEnabled(False)
        self.pushButton_51.setEnabled(True)
        self.pushButton_48.setEnabled(True)

        res_list, total_page_res, total_Numberofpieces=APITool.Get_teaching_plan_info(self.cob_school_year_31.currentText(),self.cob_school_year_27.currentText(),self.cob_school_year_24.currentText(),self.cob_school_year_32.currentText(),"15","1")
        headrs = ['年级','专业号','专业','大类标识','任务标记','计划人数','校区','课程数','专业方向个数','班级个数','最低毕业学分','不收费学分','第二课堂学分','辅修学分',
                    '二专业学分','二学位学分','学制','授予学位','学科专业类别','依托主干学科','培养目标','培养要求','核心课程','教学特色课程','说明','学科专业类别(英)','依托主干学科(英)','培养目标(英)','培养要求(英)','核心课程(英)','教学特色课程(英)','说明(英)]']
        self.current_plan_page = 1
        self.label_150.setText("共 " + str(total_page_res) + " 页")
        self.label_120.setText("共" + str(total_Numberofpieces) + "条")
        self.lineEdit_12.setText("1")
        self.Set_table_view_no_width(headrs, self.tableView_11, res_list)  # 设置表格内容
        self.tableView_11.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高
        if str(total_page_res)=="1":
            self.pushButton_50.setEnabled(False)
            self.pushButton_49.setEnabled(False)
            self.pushButton_51.setEnabled(False)
            self.pushButton_48.setEnabled(False)
    #学院转到专业
    def Get_depth_zy(self,string):
        res_list=APITool.Get_depth_to_profession(string)
        self.cob_school_year_32.clear()
        self.cob_school_year_32.addItems(res_list)
        if res_list==[]:
            self.cob_school_year_32.clear()
            self.cob_school_year_32.addItems(["全部"])

    #教学计划信息 首页
    def Get_First_plan_info(self):
        self.pushButton_50.setEnabled(False)
        self.pushButton_49.setEnabled(False)
        self.pushButton_51.setEnabled(True)
        self.pushButton_48.setEnabled(True)
        self.current_plan_page = 1
        res_list, total_page_res, total_Numberofpieces = APITool.Get_teaching_plan_info(
            self.cob_school_year_31.currentText(), self.cob_school_year_27.currentText(),
            self.cob_school_year_24.currentText(), self.cob_school_year_32.currentText(), self.comboBox_14.currentText(), "1")
        headrs = ['年级', '专业号', '专业', '大类标识', '任务标记', '计划人数', '校区', '课程数', '专业方向个数', '班级个数', '最低毕业学分', '不收费学分', '第二课堂学分',
                  '辅修学分','二专业学分', '二学位学分', '学制', '授予学位', '学科专业类别', '依托主干学科', '培养目标', '培养要求', '核心课程', '教学特色课程', '说明',
                  '学科专业类别(英)', '依托主干学科(英)', '培养目标(英)', '培养要求(英)', '核心课程(英)', '教学特色课程(英)', '说明(英)]']
        self.current_plan_page = 1
        self.label_150.setText("共 " + str(total_page_res) + " 页")
        self.label_120.setText("共" + str(total_Numberofpieces) + "条")
        self.lineEdit_12.setText("1")
        self.Set_table_view_no_width(headrs, self.tableView_11, res_list)  # 设置表格内容
        self.tableView_11.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高
        if str(total_page_res) == "1":
            self.pushButton_50.setEnabled(False)
            self.pushButton_49.setEnabled(False)
            self.pushButton_51.setEnabled(False)
            self.pushButton_48.setEnabled(False)
    # 教学计划信息 上一页
    def Get_Front_plan_info(self):
        self.pushButton_50.setEnabled(True)
        self.pushButton_49.setEnabled(True)
        self.pushButton_51.setEnabled(True)
        self.pushButton_48.setEnabled(True)
        self.current_plan_page -= 1
        res_list, total_page_res, total_Numberofpieces = APITool.Get_teaching_plan_info(
            self.cob_school_year_31.currentText(), self.cob_school_year_27.currentText(),
            self.cob_school_year_24.currentText(), self.cob_school_year_32.currentText(),
            self.comboBox_14.currentText(), str(self.current_plan_page))
        headrs = ['年级', '专业号', '专业', '大类标识', '任务标记', '计划人数', '校区', '课程数', '专业方向个数', '班级个数', '最低毕业学分', '不收费学分', '第二课堂学分',
                  '辅修学分', '二专业学分', '二学位学分', '学制', '授予学位', '学科专业类别', '依托主干学科', '培养目标', '培养要求', '核心课程', '教学特色课程', '说明',
                  '学科专业类别(英)', '依托主干学科(英)', '培养目标(英)', '培养要求(英)', '核心课程(英)', '教学特色课程(英)', '说明(英)]']
        self.label_150.setText("共 " + str(total_page_res) + " 页")
        self.label_120.setText("共" + str(total_Numberofpieces) + "条")
        self.lineEdit_12.setText(str(self.current_plan_page))
        self.Set_table_view_no_width(headrs, self.tableView_11, res_list)  # 设置表格内容
        self.tableView_11.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高

        if str(self.current_plan_page) =="1":
            self.pushButton_50.setEnabled(False)
            self.pushButton_49.setEnabled(False)
            self.pushButton_51.setEnabled(True)
            self.pushButton_48.setEnabled(True)

    #教学计划信息 下一页
    def Get_Next_plan_info(self):
        self.pushButton_50.setEnabled(True)
        self.pushButton_49.setEnabled(True)
        self.pushButton_51.setEnabled(True)
        self.pushButton_48.setEnabled(True)
        self.current_plan_page += 1
        res_list, total_page_res, total_Numberofpieces = APITool.Get_teaching_plan_info(
            self.cob_school_year_31.currentText(), self.cob_school_year_27.currentText(),
            self.cob_school_year_24.currentText(), self.cob_school_year_32.currentText(),
            self.comboBox_14.currentText(), str(self.current_plan_page))
        headrs = ['年级', '专业号', '专业', '大类标识', '任务标记', '计划人数', '校区', '课程数', '专业方向个数', '班级个数', '最低毕业学分', '不收费学分', '第二课堂学分',
                  '辅修学分', '二专业学分', '二学位学分', '学制', '授予学位', '学科专业类别', '依托主干学科', '培养目标', '培养要求', '核心课程', '教学特色课程', '说明',
                  '学科专业类别(英)', '依托主干学科(英)', '培养目标(英)', '培养要求(英)', '核心课程(英)', '教学特色课程(英)', '说明(英)]']
        self.label_150.setText("共 " + str(total_page_res) + " 页")
        self.label_120.setText("共" + str(total_Numberofpieces) + "条")
        self.lineEdit_12.setText(str(self.current_plan_page))
        self.Set_table_view_no_width(headrs, self.tableView_11, res_list)  # 设置表格内容
        self.tableView_11.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高

        if str(self.current_plan_page)==str(total_page_res):
            self.pushButton_50.setEnabled(True)
            self.pushButton_49.setEnabled(True)
            self.pushButton_51.setEnabled(False)
            self.pushButton_48.setEnabled(False)

    # 教学计划信息 尾页
    def Get_End_plan_info(self):
        self.pushButton_50.setEnabled(True)
        self.pushButton_49.setEnabled(True)
        self.pushButton_51.setEnabled(False)
        self.pushButton_48.setEnabled(False)
        res_lists, total_page_ress, total_Numberofpiecess = APITool.Get_teaching_plan_info(
            self.cob_school_year_31.currentText(), self.cob_school_year_27.currentText(),
            self.cob_school_year_24.currentText(), self.cob_school_year_32.currentText(),
            self.comboBox_14.currentText(), "1")
        res_list, total_page_res, total_Numberofpieces = APITool.Get_teaching_plan_info(
            self.cob_school_year_31.currentText(), self.cob_school_year_27.currentText(),
            self.cob_school_year_24.currentText(), self.cob_school_year_32.currentText(),
            self.comboBox_14.currentText(), str(total_page_ress))
        self.current_plan_page=int(total_page_res)
        headrs = ['年级', '专业号', '专业', '大类标识', '任务标记', '计划人数', '校区', '课程数', '专业方向个数', '班级个数', '最低毕业学分', '不收费学分', '第二课堂学分',
                  '辅修学分', '二专业学分', '二学位学分', '学制', '授予学位', '学科专业类别', '依托主干学科', '培养目标', '培养要求', '核心课程', '教学特色课程', '说明',
                  '学科专业类别(英)', '依托主干学科(英)', '培养目标(英)', '培养要求(英)', '核心课程(英)', '教学特色课程(英)', '说明(英)]']
        self.label_150.setText("共 " + str(total_page_res) + " 页")
        self.label_120.setText("共" + str(total_Numberofpieces) + "条")
        self.lineEdit_12.setText(str(self.current_plan_page))
        self.Set_table_view_no_width(headrs, self.tableView_11, res_list)  # 设置表格内容
        self.tableView_11.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高

    #查询更多页的教学计划信息
    def Query_plan_page(self,string):
        self.pushButton_50.setEnabled(False)
        self.pushButton_49.setEnabled(False)
        self.pushButton_51.setEnabled(True)
        self.pushButton_48.setEnabled(True)
        self.current_plan_page=1
        res_list, total_page_res, total_Numberofpieces = APITool.Get_teaching_plan_info(
            self.cob_school_year_31.currentText(), self.cob_school_year_27.currentText(),
            self.cob_school_year_24.currentText(), self.cob_school_year_32.currentText(), self.comboBox_14.currentText(), "1")
        headrs = ['年级', '专业号', '专业', '大类标识', '任务标记', '计划人数', '校区', '课程数', '专业方向个数', '班级个数', '最低毕业学分', '不收费学分', '第二课堂学分',
                  '辅修学分','二专业学分', '二学位学分', '学制', '授予学位', '学科专业类别', '依托主干学科', '培养目标', '培养要求', '核心课程', '教学特色课程', '说明',
                  '学科专业类别(英)', '依托主干学科(英)', '培养目标(英)', '培养要求(英)', '核心课程(英)', '教学特色课程(英)', '说明(英)]']
        self.label_150.setText("共 " + str(total_page_res) + " 页")
        self.label_120.setText("共" + str(total_Numberofpieces) + "条")
        self.lineEdit_12.setText("1")
        self.Set_table_view_no_width(headrs, self.tableView_11, res_list)  # 设置表格内容
        self.tableView_11.verticalHeader().setDefaultSectionSize(50)  # 设置整体表格行高
        if str(total_page_res)=="1":
            self.pushButton_50.setEnabled(False)
            self.pushButton_49.setEnabled(False)
            self.pushButton_51.setEnabled(False)
            self.pushButton_48.setEnabled(False)


from PyQt5.Qt import *
from API.API_Tool import APITool
from API.API_Tool import Config
from API.API_Tool import Cache
from resource.main_page import Ui_Form
from Info_query_Page import InfoQuery
from Teaching_Evaluation_Page import Teaching_Evaluation
from Stu_Info_Maintain import Info_Maintain
from Select_Course_Page import Select_Course
import resource.img_rc
class main_sys(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

        self.Init()
        self.Init_background_img()
        #初始化相关页面对象
        self.Info_Query_Page=InfoQuery()
        #初始化教学评价页面对象
        self.Teach_Evaluation_Pages=Teaching_Evaluation()
        #初始化选课页面对象
        self.Select_Course_Pages=Select_Course()
        #初始化学生信息维护页面对象
        self.Stu_Info_Maintain_Page=Info_Maintain()
        #绑定返回信号槽函数
        def success_return_slot():
            self.show()
            self.comb_info_maintain.setCurrentIndex(0)
            self.comb_elective_course.setCurrentIndex(0)
            self.comb_info_select.setCurrentIndex(0)
            self.comb_teaching_evaluation.setCurrentIndex(0)
        # 绑定信号和槽
        self.Info_Query_Page.success_return.connect(success_return_slot)
        self.Teach_Evaluation_Pages.success_return.connect(success_return_slot)
        self.Select_Course_Pages.success_return.connect(success_return_slot)
        self.Stu_Info_Maintain_Page.success_return.connect(success_return_slot)
    #初始化页面
    def Init(self):
        #鼠标移入变成手势
        self.btn_curriculum_select.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_self_select_course.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stu_evaluate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_grade_select.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_course_Preselection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_idle_classroom.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_self_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_course_select.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_teaching_plan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_curriculum_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_academic_situation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stu_grade_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_rebuild_course_select.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_questionnaire.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_self_info_maintain.setCursor(QCursor(Qt.PointingHandCursor))
        # 改变表格样式
        self.Set_tabelwidget_style()

    #初始化页面背景图片
    def Init_background_img(self):
        #设置Log图
        pixmap = QPixmap(Config.Get_main_Log_file_path())
        self.lab_log.setPixmap(pixmap)
    #初始化显示页面
    def showEvent(self, QShowEvent):
        # 设置本人图片
        self.Get_my_img()
        #设置主页面成绩
        self.Get_achievement()
        #设置主页面个人简约信息
        self.Get_my_simple_info()

    # 获取本人图片
    def Get_my_img(self):
        APITool.download_Img_info()
        pixmap2 = QPixmap(Config.Get_img_file_path())
        self.lab_self_img.setPixmap(pixmap2)
        self.lab_self_img.setScaledContents(True)
    #获取主页面成绩
    def Get_achievement(self):
        res_dict=APITool.Get_Main_achievement_info()
        #设置成绩
        res_key=[]
        res_value=[]
        for itms in res_dict.keys():
            res_key.append(itms)
        for itms in res_dict.values():
            res_value.append(itms)
        #self.btn_achievement1.setText(str1)
        self.btn_achievement1.setText(res_key[0]+"     "+res_value[0])
        self.btn_achievement2.setText(res_key[1]+"     "+res_value[1])
        self.btn_achievement3.setText(res_key[2]+"     "+res_value[2])
        self.btn_achievement4.setText(res_key[3]+"     "+res_value[3])
        self.btn_achievement5.setText(res_key[4]+"     "+res_value[4])
    #获取个人简约信息
    def Get_my_simple_info(self):
        name, my_info=APITool.Get_my_Simple_info()
        self.lab_self_name.setText(name)
        self.labe_self_info.setText(my_info)
    #设置单元格格式
    def Set_tabelwidget_style(self):
        self.tableWidget.setSpan(0, 1, 1, 25)
        self.tableWidget.setSpan(1,2,1,6)
        self.tableWidget.setSpan(1, 8, 1, 5)
        self.tableWidget.setSpan(1, 13, 1, 5)
        self.tableWidget.setSpan(1, 18, 1, 6)
        self.tableWidget.setSpan(1, 24, 1, 2)

        #设置表格不可更改
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #self.tableWidget.item(0,1).setDefaultAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        #设置单元格颜色(2行24列)
        '''for row in range(2):
            for col in range(24):
                self.tableWidget.item(9-row,24-col).setForeground(QBrush(QColor(255,0,0)))
                #self.tableWidget.item()'''
    #退出
    def Main_window_close(self):
        self.close()

    #跳转信息查询页面
    def Jump_info_Inquire_page(self,string):
        if string=='查询个人信息':
            Cache.current_title_info='查询个人信息'#缓存导航信息
        elif string=='推荐课表打印':
            Cache.current_title_info = '推荐课表打印'  # 缓存导航信息
        elif string=='学生课表查询':
            Cache.current_title_info = '学生课表查询'  # 缓存导航信息
        elif string=='查询空闲教室':
            Cache.current_title_info = '查询空闲教室'  # 缓存导航信息
        elif string=='选课名单查询':
            Cache.current_title_info = '选课名单查询'  # 缓存导航信息
        elif string=='重修课程查询':
            Cache.current_title_info = '重修课程查询'  # 缓存导航信息
        elif string=='学生成绩查询':
            Cache.current_title_info = '学生成绩查询'  # 缓存导航信息
        elif string=='学生学业情况查询':
            Cache.current_title_info = '学生学业情况查询'  # 缓存导航信息
        elif string=='学生成绩总表打印':
            Cache.current_title_info = '学生成绩总表打印'  # 缓存导航信息
        elif string=='教学执行计划查看':
            Cache.current_title_info = '教学执行计划查看'  # 缓存导航信息
        self.hide()
        self.Info_Query_Page.show()
    #跳转教学评价页面
    def Jump_teaching_evaluation_page(self,string):
        if string == '学生评价':
            Cache.current_title_info = '学生评价'  # 缓存导航信息
        elif string=='过程评价':
            Cache.current_title_info = '过程评价'  # 缓存导航信息
        elif string=='问卷调查':
            Cache.current_title_info = '问卷调查'  # 缓存导航信息
        elif string=='教学信息反馈':
            Cache.current_title_info = '教学信息反馈'  # 缓存导航信息
        self.hide()
        self.Teach_Evaluation_Pages.show()
    #跳转选课页面
    def Jump_elective_course_page(self,string):
        if string == '学生课表查询':
            Cache.current_title_info = '学生课表查询'  # 缓存导航信息
        elif string=='课程预选':
            Cache.current_title_info = '课程预选'  # 缓存导航信息
        elif string=='自主选课':
            Cache.current_title_info = '自主选课'  # 缓存导航信息
        self.hide()
        self.Select_Course_Pages.show()
    #添砖信息维护页面
    def Jump_info_maintain_page(self,string):
        if string == '学生个人信息维护':
            Cache.current_title_info = '学生个人信息维护'  # 缓存导航信息
        self.hide()
        self.Stu_Info_Maintain_Page.show()
    #获取更多课程成绩
    def Get_More_Course_Results(self):
        pass

    #获取更多消息通知
    def Get_More_Msg(self):
        pass

    #修改密码
    def Alter_my_pwd(self):
        pass

    #添加应用
    def Add_app(self):
        pass


    #相关应用槽函数
    #获取学生课表查询
    def Class_schedule_inquiry(self):
        pass
    #自主选课
    def Self_selected_course(self):
        pass
    #学生评价
    def Stu_evaluate(self):
        pass
    #学生成绩查询
    def Stu_result_inquiry(self):
        pass
    #课程预选
    def Course_pre_selection(self):
        pass
    #查询空闲教室
    def Get_Idle_classroom(self):
        pass
    #查询个人信息
    def Get_my_info(self):
        pass
    #选课名单查询
    def Get_elective_course(self):
        pass
    #教学计划查看
    def Look_teaching_plan(self):
        pass
    #推荐课表打印
    def Curriculum_print(self):
        pass
    #学生学业情况
    def Stu_studies_situation(self):
        pass
    #学生成绩打印
    def Stu_grade_print(self):
        pass
    #重修课程查询
    def Get_rebuild_curriculum(self):
        pass
    #问卷调查
    def Get_Questionnaire(self):
        pass
    #个人信息维护
    def My_info_maintain(self):
        pass
from PyQt5.Qt import *
from resource.select_course_page import Ui_Form
from API.API_Tool import APITool
from API.API_Tool import Config
from API.API_Tool import Cache
class Select_Course(QWidget,Ui_Form):
    success_return = pyqtSignal()  # 返回主页信号
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

        self.Init()
    #初始化页面
    def Init(self):
        pass
    #返回主页
    def return_home(self):
        self.close()  # 关闭当前页面
        self.success_return.emit()  # 发送成功信号
    # 显示页面槽函数
    def showEvent(self, QShowEvent):
        if Cache.current_title_info == '学生课表查询':
            self.stackedWidget.setCurrentIndex(0)
        elif Cache.current_title_info == '课程预选':
            self.stackedWidget.setCurrentIndex(1)
        elif Cache.current_title_info == '自主选课':
            self.stackedWidget.setCurrentIndex(2)
        self.lab_title_info.setText(Cache.current_title_info)  # 设置标题
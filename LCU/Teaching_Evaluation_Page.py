from PyQt5.Qt import *
from resource.teaching_evaluation_page import Ui_Form
from API.API_Tool import APITool
from API.API_Tool import Config
from API.API_Tool import Cache
class Teaching_Evaluation(QWidget,Ui_Form):
    success_return = pyqtSignal()  # 返回主页信号
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

        self.Init()
    #初始化页面
    def Init(self):
        pass
    def return_home(self):
        self.close()#关闭当前页面
        self.success_return.emit()  # 发送成功信号
    # 显示页面槽函数
    def showEvent(self, QShowEvent):
        if Cache.current_title_info == '学生评价':
            self.stackedWidget.setCurrentIndex(0)
        elif Cache.current_title_info == '过程评价':
            self.stackedWidget.setCurrentIndex(1)
        elif Cache.current_title_info == '问卷调查':
            self.stackedWidget.setCurrentIndex(2)
        elif Cache.current_title_info == '教学信息反馈':
            self.stackedWidget.setCurrentIndex(3)
        self.lab_title_info.setText(Cache.current_title_info)  # 设置标题
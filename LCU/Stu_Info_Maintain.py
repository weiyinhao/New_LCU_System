from PyQt5.Qt import *
from resource.stu_info_maintain import Ui_Form
from API.API_Tool import APITool
from API.API_Tool import Config
from API.API_Tool import Cache
class Info_Maintain(QWidget,Ui_Form):
    success_return = pyqtSignal()  # 返回主页信号
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)

        self.Init()
    #初始化页面
    def Init(self):
        pass
    # 显示页面槽函数
    def showEvent(self, QShowEvent):
        self.lab_title_info.setText(Cache.current_title_info)  # 设置标题
        self.Set_tableView_show()
    # 返回主页
    def return_home(self):
        self.close()  # 关闭当前页面
        self.success_return.emit()  # 发送成功信号
    #设置表格显示
    def Set_tableView_show(self):
        headers = [QCheckBox(''),'学年', '流程跟踪', '学年', '学期', '申请状态', '申请时间', '审核状态', '最终审核时间', '附件','操作']
        model = QStandardItemModel(self.tableView)
        model.setColumnCount(len(headers))
        for idx, title in enumerate(headers):  # 设置退课视图的数据头
            model.setHeaderData(idx, Qt.Horizontal, title)
        self.tableView.setModel(model)
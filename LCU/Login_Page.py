from PyQt5.Qt import *
from resource.login import Ui_Form
from API.API_Tool import APITool
from API.API_Tool import Config
from API.API_Tool import Cache
class LoginPane(QWidget,Ui_Form):
    # 登录成功信号
    success_login = pyqtSignal()
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)
        self.Init()
    #初始化界面
    def Init(self):
        #self.setWindowFlags(Qt.FramelessWindowHint)#设置无边框
        self.user_Edit.setFocus()#设置鼠标焦点
        #设置背景图片
        pixmap=QPixmap(Config.Get_login_background_file_path())
        pixmap2 = QPixmap(Config.Get_login_code_file_path())
        self.lab_background.setPixmap(pixmap)
        self.lab_background.setScaledContents(True)
        self.lab_code.setPixmap(pixmap2)
        self.lab_code.setScaledContents(True)
    #登录
    def check_login(self):
        user=self.user_Edit.text()
        pwd=self.psw_Edit.text()
        if not APITool.Login(user,pwd):
            print("登录失败,请重试")
            return None
        else:
            print("登录成功")
            Cache.current_user=user#保存当前账号
            #APITool.download_Img_info() # 下载图片
            self.success_login.emit()#发送成功信号
    #判断输入框是否为空
    def Led_is_text(self,string):
        user = self.user_Edit.text()
        pwd = self.psw_Edit.text()
        if(len(user)==0 or len(pwd)==0):
            self.btn_login.setEnabled(False)
        else:
            self.btn_login.setEnabled(True)
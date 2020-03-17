from PyQt5.Qt import *
import qdarkstyle
from Login_Page import LoginPane
from main_system_page import main_sys
import resource.img_rc
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    login_page=LoginPane()
    login_page.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    #app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment(is_pyqtgraph=True))
    main_page=main_sys()#主页面
    # 定义槽函数
    def success_login_slot():
        # 隐藏当前窗口
        login_page.hide()
        # 展示查询窗口
        main_page.show()
    # 绑定信号和槽
    login_page.success_login.connect(success_login_slot)
    sys.exit(app.exec_())
from PyQt5.Qt import *
import requests
import time
import os
import API.RSAJS as RSAJS
import re
from API.hex2b64 import HB64
from bs4 import BeautifulSoup
#缓存类
class Cache(object):
    #保存当前登录学号(默认为空)
    current_user=''
    #保存当前打开的页面头部信息
    current_title_info=''
    #保存学院代码
    current_College_code=['', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '28', '29', '30', '40', '42', 'a14', 'a38', 'a39', 'a46']
    #保存学院
    current_college=['--全部--', '商学院', '政治与公共管理学院', '马克思主义学院', '教育科学学院', '体育学院', '文学院', '外国语学院', '美术学院', '历史文化与旅游学院', '数学科学学院', '物理科学与信息工程学院', '化学化工学院', '大学外语教育', '环境与规划学院', '生命科学学院', '传媒技术学院', '计算机学院', '材料科学与工程学院', '农学院', '音乐与舞蹈学院', '法学院', '建筑工程学院', '机械与汽车工程学院', '药学院', '后备军官学院', '社会体育部', '医学院', '质量学院', '季羡林学院', '运河研究院', '公共体育教学部', '管理学院', '创新创业学院', '教师教育学院', '研究生处']

    #保存学年
    current_school_year=['2021-2022', '2020-2021', '2019-2020', '2018-2019', '2017-2018', '2016-2017', '2015-2016', '2014-2015']
    #保存学期
    current_semester=['1', '2', '3']
#配置类
class Config(object):
    #登录页面背景图
    @staticmethod
    def Get_login_background_file_path():
        current_path = os.path.realpath(__file__)
        current_dir=os.path.dirname(current_path)
        current_parent_dir=os.path.dirname(current_dir)
        return current_parent_dir+r'\resource\img\login_bg_pic.jpg'

    # 登录页面二维码登录图
    @staticmethod
    def Get_login_code_file_path():
        current_path = os.path.realpath(__file__)
        current_dir = os.path.dirname(current_path)
        current_parent_dir = os.path.dirname(current_dir)
        return current_parent_dir + r'\resource\img\login_ewm.gif'

    #主页面Log图
    @staticmethod
    def Get_main_Log_file_path():
        current_path = os.path.realpath(__file__)
        current_dir = os.path.dirname(current_path)
        current_parent_dir = os.path.dirname(current_dir)
        return current_parent_dir + r'\resource\img\logo_jw_w.png'
    #个人照片
    @staticmethod
    def Get_img_file_path():
        current_path = os.path.realpath(__file__)
        current_dir = os.path.split(current_path)[0]
        return current_dir + r"\img.jpg"
#封装URL类
class API(object):
    #学校域名地址
    HEAD_URL="http://jwcweb.lcu.edu.cn/"
    #教务系统主页URL
    INIT_URL=HEAD_URL+"jwglxt/xtgl/login_slogin.html?language=zh_CN&_t={}"

    # 请求PublicKey的URL
    LOGIN_KEYURL = HEAD_URL+"jwglxt/xtgl/login_getPublicKey.html?time={}"

    #登录URL POST
    LOGIN_URL=HEAD_URL+"jwglxt/xtgl/login_slogin.html?time={}"

    #主页面个人照片 GET
    MESELF_IMG_URL=HEAD_URL+"jwglxt/xtgl/photo_cxXszp.html?xh_id={}&zplx=rxhzp"

    #主页面成绩 POST
    MAIN_achievement_URL=HEAD_URL+"jwglxt/xtgl/index_cxAreaFour.html?localeKey=zh_CN&gnmkdm=index&su={}"

    #主页面个人简约信息 GET
    MAIN_MY_SIMPLE_INFO_URL=HEAD_URL+"jwglxt/xtgl/index_cxYhxxIndex.html?xt=jw&localeKey=zh_CN&_={}&gnmkdm=index&su="

    #查询个人信息(包括基本信息 学籍信息 其它信息 联系方式) GET
    MY_DETAILEDINFO_URL=HEAD_URL+"jwglxt/xsxxxggl/xsgrxxwh_cxXsgrxx.html?gnmkdm=N100801&layout=default&su="

    #查询信息页面的成绩信息 POST
    '''xh_id: 
    xnm:
    xqm:
    _search: false
    nd: 1571064905029
    queryModel.showCount: 15
    queryModel.currentPage: 1
    queryModel.sortName:
    queryModel.sortOrder: asc
    time: 0'''
    GRADE_INFO_URL=HEAD_URL+"jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N100801&su="

    #查询信息页面的课程信息 POST
    '''xh_id: 
        xnm:
        xqm:
        _search: false
        nd: 1571064905029
        queryModel.showCount: 15
        queryModel.currentPage: 1
        queryModel.sortName:
        queryModel.sortOrder: asc
        time: 0'''
    COURSE_INFO_URL=HEAD_URL+"jwglxt/xsxxxggl/xsxxwh_cxXsxkxx.html?gnmkdm=N100801&su="

    #课表打印 GET
    CURRICULUM_PRINT_URL=HEAD_URL+"jwglxt/kbdy/bjkbdy_cxBjkbdyIndex.html?gnmkdm=N214505&layout=default&su="

    #详细课表打印信息 GET
    DETAILED_CURRICULUM_PRINT_URL=HEAD_URL+"jwglxt/xtgl/comm_cxBjdmList.html?jg_id={}&njdm_id={}&_={}&gnmkdm=N214505&su="

    #学生课表查询 POST
    STU_COURSE_QUERY_URL=HEAD_URL+"jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151"

    #选课名单查询 POST
    SELECT_COURSE_LIST_URL=HEAD_URL+"jwglxt/xkcx/xkmdcx_cxXkmdcxIndex.html?doType=query&gnmkdm=N255010&su="

    #重修课程 POST
    REBUILD_COURSE_URL=HEAD_URL+"jwglxt/cxkccx/cxkccx_cxCxkccxIndex.html?doType=query&gnmkdm=N255720&su="

    #学生成绩查询 POST
    STU_SCORE_QUERY_URL=HEAD_URL+"jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005"

    #获取学生绩点 GET
    JD_URL=HEAD_URL+"jwglxt/xsxy/xsxyqk_cxXsxyqkIndex.html?gnmkdm=N105515&layout=default&su="

    #学院到专业 GET
    DEPTH_TO_PROFESSION_URL=HEAD_URL+"jwglxt/xtgl/comm_cxZydmList.html?jg_id={}&_={}&gnmkdm=N153540&su={}"

    #教学计划信息 POST
    TEACHING_PLAN_URL=HEAD_URL+"jwglxt/jxzxjhgl/jxzxjhck_cxJxzxjhckIndex.html?doType=query&gnmkdm=N153540&su="
class APITool(QObject):
    session = requests.session()#公共session对象

    #获取登录的csrftoken密钥
    @classmethod
    def Get_csrftoken(cls):
        time_now = int(time.time())#当前时间戳
        rep=cls.session.get(API.INIT_URL.format(str(time_now)))
        soup = BeautifulSoup(rep.text, "html.parser")
        #获取token
        csrftoken=soup.find('input', attrs={'id': 'csrftoken'}).attrs['value']
        return csrftoken
    #获取RSA加密后的密码
    @classmethod
    def Get_RSApwd(cls,password):
        time_now = int(time.time())  # 当前时间戳
        #获取加密公钥
        key_html=cls.session.get(API.LOGIN_KEYURL.format(str(time_now)))
        key_data = key_html.json()
        modulus = key_data["modulus"]
        exponent = key_data["exponent"]
        #生成RSA加密密码
        rsaKey=RSAJS.RSAKey()
        rsaKey.setPublic(HB64().b642hex(modulus), HB64().b642hex(exponent))
        enPassword=HB64().hex2b64(rsaKey.encrypt(password))
        #print(enPassword)
        return enPassword
    #登录
    @classmethod
    def Login(cls,user,password):
        time_now = int(time.time())  # 当前时间戳
        #获取相关数据
        csrftoken=cls.Get_csrftoken()
        enPassword=cls.Get_RSApwd(password)
        data_dic={
            "csrftoken":csrftoken,
            "yhm":user,
            "mm":enPassword,
            "mm": enPassword
        }
        rep=cls.session.post(API.LOGIN_URL.format(str(time_now)),data=data_dic)
        soup = BeautifulSoup(rep.text, "html.parser")
        #print(soup)
        try:
            #判断是否登录成功
            soup.find('a', class_="dropdown-toggle").text
            #print(soup)
            return True
        except Exception as e:
            print("未连接服务器或者密码错误,请重新尝试!")
            return False
    # 下载个人图片
    @classmethod
    def download_Img_info(cls):
        rep = cls.session.get(API.MESELF_IMG_URL.format(Cache.current_user))
        img_file_path = Config.Get_img_file_path()
        with open(img_file_path, 'wb') as f:
            f.write(rep.content)
        return img_file_path
    #获取主页面成绩
    @classmethod
    def Get_Main_achievement_info(cls):
        rep = cls.session.post(API.MAIN_achievement_URL)
        soup = BeautifulSoup(rep.text, "html.parser")
        res_list=[]#保存当前主页面课程
        res_list2=[]#保存当前主页面课程成绩
        for child in soup.find_all('span',class_='title'):
            if str(child.string).strip()!='成绩':
                res_list.append(str(child.string).strip())
        for child in soup.find_all('span',class_='fraction float_r'):
            res_list2.append(str(child.string).strip())

        return dict(zip(res_list,res_list2))#返回map
    #获取主页面个人信息
    @classmethod
    def Get_my_Simple_info(cls):
        time_now = int(round(time.time() * 1000))  # 当前13位时间戳
        print(time_now)
        rep = cls.session.get(API.MAIN_MY_SIMPLE_INFO_URL.format(str(time_now))+Cache.current_user)
        soup = BeautifulSoup(rep.text, "html.parser")
        name=''
        for child in soup.find_all('h4', class_='media-heading'):
            name=str(child.string).strip()
        my_info=str(soup.find('p').string).strip()
        #print(name,my_info)
        return name,my_info
    #获取详细的个人信息(包括基本信息 学籍信息 其它信息 联系方式)
    @classmethod
    def Get_detailed_My_Info(cls):
        rep=cls.session.get(API.MY_DETAILEDINFO_URL+Cache.current_user)
        soup = BeautifulSoup(rep.text, "html.parser")
        tail_info_res=soup.find('div',class_="tab-content ")
        res_key = []
        res_value = []
        #for each in soup.find('div',class_="tab-content "):
        for child in tail_info_res.find_all("label",class_="col-sm-4 control-label"):
            res_key.append(str(child.string).strip())
        for child in tail_info_res.find_all("p",class_="form-control-static"):
            res_value.append(str(child.string).strip())
        tail_info_res_dict=dict(zip(res_key,res_value))
        print(tail_info_res_dict)
        return tail_info_res_dict
    #查询个人信息的成绩信息
    @classmethod
    def Get_MY_GRADE_INFO(cls,showCount,currentPage,times):
        time_now = int(round(time.time() * 1000))  # 当前13位时间戳
        data={
            'xh_id': Cache.current_user,
            'xnm':'',
            'xqm':'',
            '_search': 'false',
            'nd': str(time_now),
            'queryModel.showCount': showCount,
            'queryModel.currentPage': currentPage,
            'queryModel.sortName':'',
            'queryModel.sortOrder': 'asc',
            'time': times
        }
        rep = cls.session.post(API.GRADE_INFO_URL+Cache.current_user,data=data)
        res=rep.json()
        res_list = []
        for child in res['items']:
            res_list.append(child['xnmmc'])#学年
            res_list.append(child['xqmmc'])#学期
            res_list.append(child['kch'])#课程代码
            res_list.append(child['kcmc'])#课程名称
            res_list.append(child['xf'])#学分
            res_list.append(child['cj'])#成绩
            res_list.append(child['ksxz'])#考试性质
            res_list.append(child['jd'])#学年
            res_list.append(child['kcxzmc'])#课程属性
            res_list.append('') #成绩备注
        print(res['totalPage'])
        total_page_res=res['totalPage']#总页数
        total_Numberofpieces=res['totalResult']#总条数

        return res_list,total_page_res,total_Numberofpieces
    # 查询个人信息的课程信息
    @classmethod
    def Get_MY_CROUSE_INFO(cls, showCount, currentPage, times):
        time_now = int(round(time.time() * 1000))  # 当前13位时间戳
        data = {
            'xh_id': Cache.current_user,
            'xnm': '',
            'xqm': '',
            '_search': 'false',
            'nd': str(time_now),
            'queryModel.showCount': showCount,
            'queryModel.currentPage': currentPage,
            'queryModel.sortName': '',
            'queryModel.sortOrder': 'asc',
            'time': times
        }
        rep = cls.session.post(API.COURSE_INFO_URL + Cache.current_user, data=data)
        res = rep.json()
        res_list = []
        for child in res['items']:
            res_list.append(child['xnmc'])  # 学年
            res_list.append(child['xqmmc'])  # 学期
            res_list.append(child['kcmc'])  # 课程名称
            res_list.append(child['kkxy'])#开课学院
            res_list.append('')  # 课程类别
            res_list.append(child['xf'])  # 学分
            res_list.append(child['jxbmc'])  # 教学班名称
            res_list.append(child['jsxm'])  # 教师
            res_list.append('')  # 上课时间
            res_list.append('')  # 上课地点
        total_page_res = res['totalPage']  # 总页数
        total_Numberofpieces = res['totalResult']  # 总条数
        #print(res_list)
        return res_list, total_page_res, total_Numberofpieces
    #获取课表打印信息
    @classmethod
    def Get_curriculum_print_info(cls):
        rep = cls.session.get(API.CURRICULUM_PRINT_URL + Cache.current_user)
        soup = BeautifulSoup(rep.text, "html.parser")
        school_year_list=[]#学年
        semester_list=[]#学期
        Campus_list=[]#校区
        grade_list=[]#年级
        College_list=[]#学院
        College_code_list=[]#学院代码
        school_year_info=soup.find("select",attrs={"name":"xnm"})

        semester_info=soup.find("select",attrs={"name":"xqm"})
        Campus_info = soup.find("select", attrs={"name":"xqh_id"})
        grade_info = soup.find("select", attrs={"name":"njdm_id"})
        College_info = soup.find("select", attrs={"name":"jg_id"})
        for child in school_year_info.find_all("option"):
            school_year_list.append(str(child.string).strip())
        for child in semester_info.find_all("option"):
            semester_list.append(str(child.string).strip())
        for child in Campus_info.find_all("option"):
            Campus_list.append(str(child.string).strip())
        for child in grade_info.find_all("option"):
            grade_list.append(str(child.string).strip())
        for child in College_info.find_all("option"):
            College_list.append(str(child.string).strip())
            College_code_list.append(child['value'])
        return school_year_list,semester_list,Campus_list,grade_list,College_list,dict(zip(College_list,College_code_list))
    #获取详细的课表打印信息
    @classmethod
    def Get_detailed_curriculum_print_info(cls,College_code,grade):
        time_now = int(round(time.time() * 1000))  # 当前13位时间戳
        rep = cls.session.get(API.DETAILED_CURRICULUM_PRINT_URL.format(College_code,grade,str(time_now),str(Cache.current_user)))
        res=rep.json()
        res_list=[]
        for child in res:
            res_list.append(child['bj'])
        if res_list==[]:
            return ['全部']
        return res_list
    #获取查询课表内容
    @classmethod
    def Get_Query_Course_Info(cls,xnm,xqm):
        temp=''
        if xqm=='1':
            temp='3'
        elif xqm=='2':
            temp='12'
        data={
            'xnm':xnm,
            'xqm':temp
        }
        rep=cls.session.post(API.STU_COURSE_QUERY_URL,data=data)
        res = rep.json()
        res_list=[]
        kb_jc_list=[]#保存课表节次
        xq_list=[]#保存课表星期
        #对数据进行处理
        for each in res['kbList']:
            res_list.append(each['kcmc']+each["xslxbj"]+"\n"+'('+each['jc']+")"+each['zcd']+"\n"+each['xqmc']+" "+each['cdmc']+"\n"+each['xm']+"\n"
                            +each['kcxszc']+"\n")
            kb_jc_list.append(each['jc'])
            xq_list.append(each['xqjmc'])
        return res_list,kb_jc_list,xq_list
    #选课名单查询
    @classmethod
    def Get_select_course_list(cls,xnm,xqm):
        time_now = int(round(time.time() * 1000))  # 当前13位时间戳
        xqm_temp=''
        if xqm=="全部":
            xqm_temp=""
        elif xqm=="1":
            xqm_temp="3"
        elif xqm=="2":
            xqm_temp="12"
        elif xqm_temp=="3":
            xqm_temp="16"
        xnm_temp=''
        if xnm=="全部":
            xnm_temp=''
        else:
            xnm_temp=xnm
        data={
            'xnm':xnm_temp,
            'xqm':xqm_temp,
            'kkxy_id':'',
            'kclbdm':'',
            'kcxzmc':'',
            'kch':'',
            'kklxdm':'',
            'xxlx':'',
            'kkzt': '1',
            'jxbmc':'',
            'jsxx':'',
            'kcgsdm':'',
            '_search': 'false',
            'nd': str(time_now),
            'queryModel.showCount': '15',
            'queryModel.currentPage': '1',
            'queryModel.sortName':'',
            'queryModel.sortOrder': 'asc',
            'time': '24'
        }
        rep = cls.session.post(API.SELECT_COURSE_LIST_URL+Cache.current_user, data=data)
        res = rep.json()
        res_list = []
        for child in res['items']:
            res_list.append(child['xkbjmc'])
            res_list.append(child['xnmc'])
            res_list.append(child['xqmc'])
            res_list.append(child['kch'])
            res_list.append(child['kcmc'])
            res_list.append(' ')
            res_list.append(child['jgmc'])
            res_list.append(child['xf'])
            res_list.append(child['xh'])
            res_list.append(child['xm'])
            res_list.append(child['zjhm'])
            res_list.append(child['xxlxmc'])
            res_list.append(child['kkztmc'])
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(child['qsjsz'])
            res_list.append(' ')
            res_list.append(child['xqhmc'])
            res_list.append(child['kclbmc'])
            res_list.append(child['kcxzmc'])
            res_list.append(child['kklxmc'])
            res_list.append(child['jxbmc'])
            res_list.append(' ')
            res_list.append(child['xbmc'])
            res_list.append(child['kkxymc'])
            res_list.append(child['njmc'])
            res_list.append(child['zymc'])
            res_list.append(child['bjmc'])
        total_page_res = res['totalPage']  # 总页数
        total_Numberofpieces = res['totalResult']  # 总条数
        return res_list, total_page_res, total_Numberofpieces
    #重修课程查询
    @classmethod
    def Get_Rebuild_course_info(cls):
        pass
    #学生成绩查询
    @classmethod
    def Get_Stu_score_info(cls,xnm,xqm,showCount='15',currentPage='1'):
        xqm_dict={
            "全部":'',
            "1":'3',
            "2":'12',
            "3":'16'
        }
        time_now = int(round(time.time() * 1000))  # 当前13位时间戳
        temp_xnm=''
        if xnm!="全部":
            temp_xnm =xnm
        data={
            'xnm':temp_xnm,
            'xqm': xqm_dict[xqm],
            '_search': 'false',
            'nd': str(time_now),
            'queryModel.showCount': showCount,
            'queryModel.currentPage': currentPage,
            'queryModel.sortName':'',
            'queryModel.sortOrder': 'asc',
            'time': '6',
        }
        rep=cls.session.post(API.STU_SCORE_QUERY_URL,data=data)
        res=rep.json()
        res_list=[]
        for child in res['items']:
            res_list.append(child['xnmmc'])
            res_list.append(child['xqmmc'])
            res_list.append(child['kch'])
            res_list.append(child['kcmc'])
            res_list.append(child['kcxzmc'])
            res_list.append(child['xqm'])
            res_list.append(child['cj'])
            res_list.append(' ')
            res_list.append(child['jd'])
            res_list.append(child['ksxz'])
            res_list.append(child['cjsfzf'])
            res_list.append(child['sfxwkc'])
            res_list.append(child['kkbmmc'])
            res_list.append(child['kcbj'])
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(child['jxbmc'])
            res_list.append(child['jsxm'])
            res_list.append(child['xh'])
            res_list.append(child['xm'])
            res_list.append(child['xb'])
            res_list.append(' ')
            res_list.append(child['jgmc'])
            res_list.append(child['zymc'])
            res_list.append(child['xnm'])
            res_list.append(child['bj'])
        total_page_res = res['totalPage']  # 总页数
        total_Numberofpieces = res['totalResult']  # 总条数
        return res_list, total_page_res, total_Numberofpieces
    #获取学生绩点
    @classmethod
    def Get_Stu_Jd(cls):
        rep=cls.session.get(API.JD_URL+Cache.current_user)
        soup = BeautifulSoup(rep.text, "html.parser")
        res=soup.find("div",attrs={"id":"alertBox"})
        res_str=str(res.text).strip()
        return res_str
    #由学院获取相关专业
    @classmethod
    def Get_depth_to_profession(cls,depth):
        time_now = int(round(time.time() * 1000))  # 当前13位时间戳
        # key-value 学院学院代码
        current_depth_dict = dict(zip(Cache.current_college, Cache.current_College_code))
        depth_code=current_depth_dict[depth]
        cur_user=Cache.current_user
        rep = cls.session.get(API.DEPTH_TO_PROFESSION_URL.format(depth_code,str(time_now),cur_user))
        res=rep.json()
        res_list=[]
        for child in res:
            res_list.append(child['zymc'])
        return res_list
    #获取教学计划信息
    @classmethod
    def Get_teaching_plan_info(cls,jg_id,njdm_id,dlbs,zyh_id,showCount='15',currentPage='1'):
        time_now = int(round(time.time() * 1000))  # 当前13位时间戳
        # key-value 学院学院代码
        current_depth_dict = dict(zip(Cache.current_college, Cache.current_College_code))
        jg_id_temp=current_depth_dict[jg_id]
        njdm_id_temp = ''
        if njdm_id=="全部":
            njdm_id_temp=''
        else:
            njdm_id_temp=njdm_id
        dlbs_dict={"全部":"","大类":"0","专业":"1","二级专业":"2"}
        zyh_id_temp=''
        if zyh_id=="全部":
            zyh_id_temp=''
        else:
            zyh_id_temp=re.search('(\(.*?\))',zyh_id)
        data={
            'jg_id': jg_id_temp,
            'njdm_id': njdm_id_temp,
            'dlbs':dlbs_dict[dlbs],
            'zyh_id':zyh_id_temp,
            '_search': 'false',
             'nd': str(time_now),
            'queryModel.showCount': showCount,
            'queryModel.currentPage': currentPage,
             'queryModel.sortName':'',
            'queryModel.sortOrder': 'asc',
            'time': '1'
        }
        print(jg_id_temp,njdm_id_temp,dlbs_dict[dlbs],zyh_id)
        rep=cls.session.post(API.TEACHING_PLAN_URL+Cache.current_user,data=data)
        res=rep.json()
        res_list=[]
        for child in res['items']:
            res_list.append(child['njmc'])
            res_list.append(child['zyh'])
            res_list.append(child['zymc'])
            res_list.append(child['dlbs'])
            res_list.append(child['rwbj'])
            if 'jhrs' in child:
                res_list.append(child['jhrs'])
            else:
                res_list.append(' ')
            if 'xqmc'in child:
                res_list.append(child['xqmc'])
            else:
                res_list.append(' ')
            if 'kcs' in child:
                res_list.append(child['kcs'])
            else:
                res_list.append(' ')
            res_list.append(child['zyfxgs'])
            res_list.append(child['bjgs'])
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            if 'xz' in child:
                res_list.append(child['xz'])
            else:
                res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
            res_list.append(' ')
        total_page_res = res['totalPage']  # 总页数
        total_Numberofpieces = res['totalResult']  # 总条数
        print(res_list)
        return res_list, total_page_res, total_Numberofpieces
if __name__ == '__main__':
    APITool.Login('','')
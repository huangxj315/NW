# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/30 10:25
@Auth ： 黄香杰
@File ：base_NW.py

"""
import datetime
import random
import string
import allure
import pandas as pd
import xlrd
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import yaml
import time
from pykeyboard import PyKeyboard
from sympy.printing.numpy import const

from base import base
from time import sleep



url_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'parameter','url.xls')
user_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'parameter','users.xls')
parameter_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'parameter','parameter.xls')




class base_NW(base):
    def __init__(self,driver):
        self.driver = driver


    #后台登录
    def start_houtai(self,user,usertype):
        #获取系统地址
        url = self.get_url()
        #登录仿真后台系统
        self.driver.get(url)
        # #关闭放假提醒
        # self.get_element('login', 'fjtx_img').click()
        #获取账号、密码、验证码
        get_user,get_password,get_code,get_username = self.get_user(user,usertype)
        #判断账号输入框是否有值，有值则先清空
        if self.get_element('login','user_input').get_attribute("value"):
            # 清空 input 框
            self.get_element('login','user_input').clear()
        #输入账号
        self.get_element('login','user_input').send_keys(get_user)
        #输入密码
        self.get_element('login', 'pas_input').send_keys(get_password)
        #点击获取验证码
        self.get_element('login', 'send_code').click()
        sleep(1)
        code=self.get_element('login', 'send_code').get_attribute("value")
        if code=='获取验证码':
            # 点击验证码频繁弹窗
            self.get_element('login','okbutton').click()
            # 等待1分钟
            time.sleep(60)
            # 点击获取验证码
            self.get_element('login', 'send_code').click()
            # 输入验证码
            self.get_element('login', 'code_input').send_keys(get_code)
            # 点击登录
            self.get_element('login', 'login_button').click()
        else:
             # 输入验证码
             self.get_element('login', 'code_input').send_keys(get_code)
             # 点击登录
             self.get_element('login', 'login_button').click()




    #截屏功能
    def get_screen(self,def_name,num):
        pic_path = def_name
        pic_path = os.path.join(os.path.dirname(os.getcwd()), 'report','pic',pic_path)
        if os.path.exists(pic_path):
            pass
        else:
            os.makedirs(pic_path)
        pic_path = os.path.join(pic_path, num) + '.jpg'
        self.driver.get_screenshot_as_file(pic_path)


    #获取系统地址
    def get_url(self):
        urlFile = xlrd.open_workbook(url_file)
        urlSheet = urlFile.sheet_by_name('Sheet1')
        return urlSheet.cell_value(1,0)
    #获取供应商注册地址
    def get_registerurl(self):
        registerurl = self.get_paras('registerlink', 1)
        #登录仿真后台系统
        self.driver.get(registerurl)


    #获取登录用户名、密码、验证码
    def get_user(self,user,usertype):
        userFile = xlrd.open_workbook(user_file)
        userSheet = userFile.sheet_by_name('Sheet1')
        if usertype=='核心企业':
            row = userSheet.row_values(1) # 获取第二行数据
        if usertype=='供应商':
            row = userSheet.row_values(2) # 获取第三行数据
        if usertype=='运营':
            row = userSheet.row_values(3) # 获取第四行数据
        if usertype=='牌照':
            row = userSheet.row_values(4) # 获取第四行数据
        if usertype=='管理员':
            row = userSheet.row_values(5) # 获取第五行数据
        if usertype=='新供应商':
            row = userSheet.row_values(6) # 获取第五行数据
        getUser = row[0]
        getPassword = row[1]
        getCode = row[2]
        getUsername= row[3]
        return getUser,getPassword,getCode,getUsername



    #获取单个元素定位
    def get_element(self,y_name,e_name):
        self.driver.switch_to.default_content()
        y_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'element', y_name )
        with open(file=y_path, mode='rb') as f:
            infos = yaml.load(f, Loader=yaml.FullLoader)
        xpath = str(infos[e_name]['xpath'])
        if infos[e_name]['iframe'] == 'None':
            pass
        else:
            m = infos[e_name]['iframe']
            m = m.split(';')
            for x in m:
                a = str(x)
                iframe = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(a))
                self.driver.switch_to.frame(iframe)
        e = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(xpath))
        time.sleep(0.5)
        return e
    #获取批量元素定位
    def get_elements(self, y_name, e_name):
        self.driver.switch_to.default_content()
        y_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'element',y_name )
        with open(file=y_path, mode='rb') as f:
            infos = yaml.load(f, Loader=yaml.FullLoader)
        xpath = str(infos[e_name]['xpath'])
        if infos[e_name]['iframe'] == 'None':
            pass
        else:
            m = infos[e_name]['iframe']
            m = m.split(';')
            for x in m:
                a = str(x)
                iframe = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(a))
                self.driver.switch_to.frame(iframe)
        e = WebDriverWait(self.driver, 120).until(lambda x: x.find_elements_by_xpath(xpath))
        time.sleep(0.5)
        return e

    #上传文件
    def uploadFile(self,path):
        keyboard = PyKeyboard()
        time.sleep(2)
        keyboard.type_string(path)
        keyboard.tap_key(keyboard.enter_key)
        time.sleep(3)
        keyboard.tap_key(keyboard.enter_key)
        time.sleep(3)
    def get_current(self):
        time.sleep(2)
        windows = self.driver.window_handles
        return len(windows)

    def get_current_handle(self):
        time.sleep(2)
        windows = self.driver.window_handles
        return self.driver.switch_to.window(windows[len(windows) - 1])

    def get_pre_handle(self):
        time.sleep(2)
        windows = self.driver.window_handles
        return self.driver.switch_to.window(windows[len(windows) - 2])

    def get_next_handle(self):
        time.sleep(2)
        windows = self.driver.window_handles
        return self.driver.switch_to.window(windows[len(windows) - 1])

    def scroll_foot(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        time.sleep(3)

    def scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
        time.sleep(3)

    def refresh(self):
        self.driver.execute_script("history.go(0)")
    #获取parameter参数
    def get_paras(self,sheet,num):

        paraFile = xlrd.open_workbook(parameter_file)
        if sheet == 'billnum':
            paraSheet = paraFile.sheet_by_name('billnum')
            return paraSheet.cell_value(num-1,0)#第1行第1列
        if sheet == 'billno':
            paraSheet = paraFile.sheet_by_name('billno')
            return paraSheet.cell_value(num-1,0)
        if sheet == 'voucheramount':
            paraSheet = paraFile.sheet_by_name('voucheramount')
            return paraSheet.cell_value(num-1,0)
        if sheet == 'voucherexpirationdate':
            paraSheet = paraFile.sheet_by_name('voucherexpirationdate')
            return paraSheet.cell_value(num-1,0)
        if sheet == 'vouchernum':
            paraSheet = paraFile.sheet_by_name('vouchernum')
            return paraSheet.cell_value(num-1,0)
        if sheet == 'custname':
            paraSheet = paraFile.sheet_by_name('custname')
            return paraSheet.cell_value(num-1,0)
        if sheet == 'registerlink':
            paraSheet = paraFile.sheet_by_name('registerlink')
            return paraSheet.cell_value(num-1, 0)
        if sheet == 'klfname':
            paraSheet = paraFile.sheet_by_name('klfname')
            return paraSheet.cell_value(num-1, 0)
    #获取当前日期后的某个工作日
    def get_workingday(self,n):
        # 定义日期格式
        date_format = "%Y-%m-%d"
        # 获取今天的日期
        today = pd.Timestamp(datetime.date.today())
        count = 0
        # 遍历日期范围
        while count < n:
            today += pd.Timedelta(days=1)
            # 判断是否为工作日
            if today.weekday() < 5:
                count += 1
        working_day = today.strftime(date_format)
        return working_day

       # # 定义日期格式(取的当前日期后的第一个工作日)
       #  date_format = "%Y-%m-%d"
       #  # 获取今天的日期
       #  today = pd.Timestamp(datetime.date.today())
       #  # 定义日期范围
       #  date_range = pd.date_range(start=today, periods=10)
       #  # 遍历日期范围
       #  for date in date_range:
       #      working_day = date.strftime(date_format)
       #      # 判断是否为工作日
       #      if date.weekday() < 5 and date > today:
       #          print(working_day)
       #          return working_day
       #          break

    def get_randomtime(self):
        curr_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(curr_time, '%d%H%M%S')
        return time_str

    def get_currentrq(self):
        curr_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d')
        return time_str

    def generate_phone_number(self):
        fixed_part = "199"
        date_part = datetime.datetime.now().strftime("%m%d")
        random_part = str(random.randint(1000, 9999))

        phone_number = fixed_part + date_part + random_part
        return phone_number
    def generate_name(self):
        surnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '楚', '卫', '蒋']
        names = ['宇', '婷', '晨', '文', '杰', '炜', '斌', '雪', '彤', '涛', '萌', '思', '尧']

        surname = random.choice(surnames)
        name = random.choice(names)

        full_name = surname + name

        return full_name

    # 随机生成企业名称
    def generate_company_name(self):
        prefix = ['中国电力', '龙源电缆', '长江电力', '能源电力', '成蜀电缆']
        suffix = ['有限公司', '股份有限公司', '有限责任公司', '建设有限公司']
        return random.choice(prefix) + ' ' + random.choice(string.ascii_uppercase) + random.choice(
            string.ascii_lowercase) + ' ' + random.choice(suffix)

    def generate_id_number(self):
        province_code = '110000'  # 假设生成的身份证号码的省份代码为广东省（参考真实代码）
        birthday = '19900101'  # 假设生成的身份证号码的出生日期为1990年1月1日（参考真实日期）
        random_num = str(random.randint(100, 999))  # 随机生成3位顺序码
        check_code = 'X'  # 假设生成的身份证号码的校验码为X（参考真实码）
        id_number= province_code + birthday + random_num + check_code
        return id_number
        # 生成一个随机的身份证号码

    def generate_id(self):
        # 随机生成一个区域码(6位数)
        addr=[(110000, u'北京市'),(110101, u'东城区'),(110102, u'西城区'),(110103, u'崇文区'),(110104, u'宣武区')]
        addrInfo = random.randint(0, len(addr))  # 随机选择一个值
        region_code = str(110000)
        # 生成年份(4位数)
        year = str(random.randint(1949, 2022))
        # 生成月份(2位数)
        month = str(random.randint(1, 12)).rjust(2, '0')
        # 生成日期(2位数)
        day = str(random.randint(1, 28)).rjust(2, '0')
        # 生成顺序码(3位数)
        order = str(random.randint(1, 999)).rjust(3, '0')
        id17 = region_code + year + month + day + order
        # 系数列表
        factor_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        # 校验码列表
        check_code_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        # 根据前17位计算出校验码
        check_code = 0
        for i in range(len(id17)):
            check_code += int(id17[i]) * factor_list[i]
        check_code %= 11
        check_code=check_code_list[check_code]
        check_code_str = str(check_code)
        # 拼接身份证号码并返回
        return region_code + year + month + day + order + check_code_str


    def download_query_results(self,page,exportButton):
        # 指定下载文件的目录
        download_dir = "C:\\Users\\Administrator\\Downloads"
        # 记录下载前的文件数量
        file_count_before = len(os.listdir(download_dir))
        # 点击下载查询结果按钮
        self.get_element(page, exportButton).click()
        sleep(5)
        with allure.step("验证搜索结果和预期一样"):
            # 获取下载后的文件数量
            file_count_after = len(os.listdir(download_dir))
            if file_count_after > file_count_before:
                print("下载成功！")
            else:
                print("下载失败！")

    def generate_uscc(self):
        # 注册号（6位数字）
        reg_code = ''.join(random.choice(string.digits) for _ in range(8))

        # 机构类别代码（1位数字）
        ent_type = random.choice(string.digits)

        # 行政区划代码（6位数字）
        area_code = ''.join(random.choice(string.digits) for _ in range(8))

        # 校验码（1位数字或大写英文字母）
        check_code = random.choice(string.digits + string.ascii_uppercase)

        # 拼接各个部分获得18位统一社会信用代码
        code_with_checksum = reg_code + ent_type + area_code + check_code
        return code_with_checksum


if __name__ == "__main__":
    pass
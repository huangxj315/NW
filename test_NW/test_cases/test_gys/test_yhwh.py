# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/10 11:34
@Auth ： 黄香杰
@File ：test_yhwh.py

"""

import pytest
from time import sleep
import allure
from base import base



@allure.feature("供应商-用户维护新增账户")
class test_yhwh():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_XT', method.__name__)

    @allure.feature("供应商-用户维护新增有操作、消息接收权限用户账户")
    def test_xzyh(self, get_driver):
        #用户登录
        get_driver.start_houtai(1,'供应商')
        # 点击设置tab
        get_driver.get_element('homepage', 'shezhi_tab').click()
        # 点击用户维护
        get_driver.get_element('gysshezhi', 'yhwh').click()
        # 点击新增按钮
        get_driver.get_element('gysshezhi', 'addBtn').click()
        #输入用户姓名
        username=get_driver.generate_name()
        get_driver.get_element('gysshezhi','username').send_keys(username)
        #输入用户证件号码
        idnum=get_driver.generate_id_number()
        get_driver.get_element('gysshezhi','idnum').send_keys(idnum)
        #输入身份证开始时间
        get_driver.get_element('gysshezhi','idstartdate').send_keys('2023-07-18')
        #输入身份证结束时间-长期
        get_driver.get_element('gysshezhi','longeffect').click()
        #输入登录手机号
        tel=get_driver.generate_phone_number()
        get_driver.get_element('gysshezhi','telephone').send_keys(tel)
        #输入用户邮箱
        get_driver.get_element('gysshezhi','email').send_keys(tel+'@qq.com')
        #点击消息接收
        get_driver.get_element('gysshezhi','ismsger').click()
        #点击保存
        get_driver.get_element('gysshezhi','saveBtn').click()
        sleep(3)
        with allure.step("验证搜索结果和预期一样"):
            # 输入用户姓名
            get_driver.get_element('gysshezhi', 'yhname').send_keys(username)
            # 输入用户邮箱
            get_driver.get_element('gysshezhi', 'yhemail').send_keys(tel+'@qq.com')
            # 输入用户手机号
            get_driver.get_element('gysshezhi', 'yhtel').send_keys(tel)
            # 点击查询
            get_driver.get_element('gysshezhi', 'searchButton').click()
            sleep(30)
            #获取第一条数据名称
            result1 = get_driver.get_element('gysshezhi', 'cxresult').get_attribute('innerText')
            assert result1 == username
    @allure.feature("供应商-用户维护新增有审核、消息接收权限用户账户")
    def test_xzptyh(self, get_driver):
        #用户登录
        get_driver.start_houtai(1,'供应商')
        # 点击设置tab
        get_driver.get_element('homepage', 'shezhi_tab').click()
        # 点击用户维护
        get_driver.get_element('gysshezhi', 'yhwh').click()
        # 点击新增按钮
        get_driver.get_element('gysshezhi', 'addBtn').click()
        #输入用户姓名
        username=get_driver.generate_name()
        get_driver.get_element('gysshezhi','username').send_keys(username)
        #输入用户证件号码
        idnum=get_driver.generate_id_number()
        get_driver.get_element('gysshezhi','idnum').send_keys(idnum)
        #输入身份证开始时间
        get_driver.get_element('gysshezhi','idstartdate').send_keys('2023-07-18')
        #输入身份证结束时间-长期
        get_driver.get_element('gysshezhi','longeffect').click()
        #输入登录手机号
        tel=get_driver.generate_phone_number()
        get_driver.get_element('gysshezhi','telephone').send_keys(tel)
        #输入用户邮箱
        get_driver.get_element('gysshezhi','email').send_keys(tel+'@qq.com')
        #取消勾选角色类型-审核
        get_driver.get_element('gysshezhi','caozuo').click()
        #点击角色类型-审核
        get_driver.get_element('gysshezhi','shenhe').click()
        #点击保存
        get_driver.get_element('gysshezhi','saveBtn').click()
        sleep(3)
        with allure.step("验证搜索结果和预期一样"):
            # 输入用户姓名
            get_driver.get_element('gysshezhi', 'yhname').send_keys(username)
            # 点击查询
            get_driver.get_element('gysshezhi', 'searchButton').click()
            sleep(30)
            #获取第一条数据用户姓名
            result1 = get_driver.get_element('gysshezhi', 'cxresult').get_attribute('innerText')
            assert result1 == username
    @allure.feature("供应商-用户维护修改用户账户信息")
    def test_xgptyh(self, get_driver):
        #用户登录
        get_driver.start_houtai(1,'供应商')
        # 点击设置tab
        get_driver.get_element('homepage', 'shezhi_tab').click()
        # 点击用户维护
        get_driver.get_element('gysshezhi', 'yhwh').click()
        # 定位div元素
        div_element = get_driver.get_element('gysshezhi', 'div_locator')
        # 定位table元素
        table_element = div_element.find_element_by_xpath("//table")
        # 定位最后一行的元素
        last_row = table_element.find_elements_by_xpath(".//tr")[-1]
        # 定位最后一行最后一列的元素
        last_cell = last_row.find_elements_by_xpath(".//td")[-1]
        # 点击最后一行最后一列的元素
        last_cell.click()
        #输入用户姓名
        username=get_driver.get_element('gysshezhi', 'username').get_attribute('value')
        random=get_driver.get_randomtime()
        get_driver.get_element('gysshezhi','username').send_keys(random)
        newusername = get_driver.get_element('gysshezhi', 'username').get_attribute('value')
        #点击保存
        get_driver.get_element('gysshezhi','saveBtn').click()
        sleep(3)
        with allure.step("验证搜索结果和预期一样"):
            # 输入用户姓名
            get_driver.get_element('gysshezhi', 'yhname').send_keys(newusername)
            # 点击查询
            get_driver.get_element('gysshezhi', 'searchButton').click()
            sleep(3)
            #获取第一条数据用户姓名
            result1 = get_driver.get_element('gysshezhi', 'cxresult').get_attribute('innerText')
            assert result1 == newusername














if __name__ == "__main__":
        pytest.main()
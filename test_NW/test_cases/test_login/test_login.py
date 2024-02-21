# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_login.py

"""
import pytest
import allure
from time import sleep
from base import base




@allure.feature("登录模块")
@pytest.mark.flaky(reruns=2,reruns_delay=1)
class test_login():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    # @allure.story("用户不存在")
    # def test_login_001(self,get_driver):
    #     #获取后台系统地址
    #     url = get_driver.get_url()
    #     #登录仿真后台系统
    #     get_driver.driver.get(url)
    #     #关闭放假提醒
    #     get_driver.get_element('login', 'fjtx_img').click()
    #     #输入账号
    #     get_driver.get_element('login','user_input').send_keys('aaa')
    #     #输入密码
    #     get_driver.get_element('login', 'pas_input').send_keys('123456')
    #     #点击获取验证码
    #     get_driver.get_element('login', 'send_code').click()
    #     #输入验证码
    #     get_driver.get_element('login', 'code_input').send_keys('999999')
    #     #点击登录
    #     get_driver.get_element('login', 'login_button').click()
    #     #校验是否正确
    #     test = get_driver.get_element('login', 'user_error_msg').get_attribute('innerText')
    #     assert test == '用户名或密码错误'


    @allure.story("登录成功")
    def test_login_002(self,get_driver):
        #登录用户
        get_driver.start_houtai(1, '供应商')
        #校验是否正确
        sleep(3)
        test = get_driver.get_element('homepage', 'shouye').get_attribute('innerText')
        assert test == '首页'




if __name__ == "__main__":
    pytest.main()
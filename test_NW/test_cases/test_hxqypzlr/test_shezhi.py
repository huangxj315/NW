# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_shezhi.py

"""

from time import sleep
import pytest
import allure
from selenium import webdriver
from base import base
import pyperclip

@allure.feature("供应商-注册新的账户")
class test_shehzi():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    def test_shezhi(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '核心企业')
        # 点击设置tab
        get_driver.get_element('homepage', 'shezhi_tab').click()
        # 复制链接按钮
        get_driver.get_element('shezhi', 'copy_link').click()
        # 复制链接页面链接内容
        registerlink=get_driver.get_element('shezhi', 'linktext').get_attribute('innerText')
        with allure.step("将分享链接地址存到参数表中"):
            get_driver.parameter('test_NW', 'case', 'registerlink', registerlink, 1)



if __name__ == "__main__":
        pytest.main()

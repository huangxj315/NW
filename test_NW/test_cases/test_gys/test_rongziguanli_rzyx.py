# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_chaxuntongji_edsqjl.py

"""
import pytest
from time import sleep
import allure
from base import base
import os



@allure.feature("供应商-融资管理-融资意向")
class test_rzyx():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-融资意向有补充附件、详情、推荐信息操作")
    def test_rzyx(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击融资意向
        get_driver.get_element('rongziguanli-rzyx', 'rzyx').click()
        # 点击补充附件
        get_driver.get_element('rongziguanli-rzyx', 'bcfj').click()
        # 点击上传附件
        get_driver.get_element('rongziguanli-rzyx', 'uploanMYFile').click()
        # 点击选择文件按钮
        get_driver.get_element('rongziguanli-rzyx', 'webuploader-pick').click()
        sleep(3)
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\test.png")
        # 点击上传附件后的确定按钮
        get_driver.get_element('rongziguanli-rzyx', 'uploadbutton').click()
        # 点击提交按钮
        get_driver.get_element('rongziguanli-rzyx', 'savebutton').click()
        # 点击详情按钮
        get_driver.get_element('rongziguanli-rzyx', 'xq').click()
        # 点击详情页面的关闭按钮
        get_driver.get_next_handle()
        get_driver.get_element('rongziguanli-rzyx', 'closebutton').click()
        # 点击推荐信息按钮
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-rzyx', 'tjxx').click()
        # 点击推荐信息页面的详情按钮
        get_driver.get_element('rongziguanli-rzyx', 'tjxxxq').click()
        # 点击推荐信息详情页面的关闭按钮
        get_driver.get_next_handle()
        get_driver.get_element('rongziguanli-rzyx', 'closebutton').click()
        sleep(3)


if __name__ == "__main__":
        pytest.main()
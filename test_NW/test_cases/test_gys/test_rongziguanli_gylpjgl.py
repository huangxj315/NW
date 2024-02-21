# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_rongziguanli_gylpjgl.py

"""
import pytest
import datetime
import random
from time import sleep
import allure
from base import base
import os
from selenium.webdriver.support.select import Select



@allure.feature("供应商-融资管理-供应链票据管理")
class test_gylpjgl():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-供票收票阶段有背书转让、提示付款、查看详情操作")
    def test_shoupiao(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击供应链票据管理
        get_driver.get_element('rongziguanli-gylpjgl', 'gylpjgl').click()
        # 输入票据到期日起始日期
        curr_time = datetime.datetime.now()
        date_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d')
        get_driver.get_element('rongziguanli-gylpjgl', 'duedatebegin').send_keys(date_str)
        # 选中文本名称为"登记结果成功"选项
        status = get_driver.get_element('rongziguanli-gylpjgl', 'stageState')
        Select(status).select_by_visible_text("登记结果成功")
        # 点击查询
        get_driver.get_element('rongziguanli-gylpjgl', 'searchbutton').click()
        sleep(2)
        # 点击详情
        get_driver.get_element('rongziguanli-gylpjgl', 'xiangqing').click()
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-gylpjgl', 'closebutton').click()
        # 点击提示付款
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-gylpjgl', 'tishifukuan').click()
        billno=get_driver.get_element('rongziguanli-gylpjgl', 'tsbillno').get_attribute('innerText')
        # 输入提示付款意见
        get_driver.get_element('rongziguanli-gylpjgl', 'paytipRemark').send_keys('脚本自动的提示付款')
        # 点击提交
        get_driver.get_element('rongziguanli-gylpjgl', 'submit').click()
        sleep(2)
        with allure.step("验证该票据已经成功申请提示付款"):
            # 输入票据编号
            get_driver.get_element('rongziguanli-gylpjgl', 'crpayId').send_keys(billno)
            # 点击查询
            get_driver.get_element('rongziguanli-gylpjgl', 'searchButton').click()
            sleep(2)
            #获取第一条数据票据编号
            result = get_driver.get_element('rongziguanli-gylpjgl', 'cxbillno').get_attribute('innerText')
            assert result == billno




if __name__ == "__main__":
        pytest.main()
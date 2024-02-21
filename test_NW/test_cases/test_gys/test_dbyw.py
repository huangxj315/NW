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



@allure.feature("供应商-待办业务")
class test_rzgl():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-待办业务有提现操作")
    def test_tixian(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击待办业务tab
        get_driver.get_element('homepage', 'mytodo_tab').click()
        # 点击提现
        get_driver.get_element('mytodo', 'outmny').click()
        # 输入提现金额
        get_driver.get_next_handle()
        oldtamt=float(get_driver.get_element('mytodo', 'djmoney').get_attribute('innerText').replace(',', ''))
        get_driver.get_element('mytodo', 'AMT').clear()
        get_driver.get_element('mytodo', 'AMT').send_keys('1')
        # 输入提现备注
        get_driver.get_element('mytodo', 'memo').send_keys('脚本自动提现')
        # 点击下一步nextBtn
        get_driver.get_element('mytodo', 'nextBtn').click()
        # 点击获取验证码
        get_driver.get_element('mytodo', 'getCode').click()
        # 输入验证码
        get_driver.get_element('mytodo', 'msgcode').send_keys('999999')
        # 点击提交
        get_driver.get_element('mytodo', 'submitBtn').click()
        with allure.step("验证已提现成功"):
            #获取提示信息
            currentamt=float(get_driver.get_element('mytodo', 'djhmoney').get_attribute('innerText').replace(',', ''))
            newamt=oldtamt + 1
            assert currentamt == newamt


if __name__ == "__main__":
        pytest.main()
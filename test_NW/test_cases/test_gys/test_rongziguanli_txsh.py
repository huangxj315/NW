# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰

"""
import pytest
from time import sleep
import allure
from base import base
import os



@allure.feature("供应商-融资管理-提现审核")
class test_txsh():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-提现审核有查询、审核操作")
    def test_txsh(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击提现审核
        get_driver.get_element('rongziguanli-txsh', 'txsh').click()
        # 选择一条待审核数据点击审核
        get_driver.get_element('rongziguanli-txsh', 'sh').click()
        sqbh = get_driver.get_element('rongziguanli-txsh', 'sqbh').get_attribute('innerText')
        # 输入审核意见
        get_driver.get_element('rongziguanli-txsh', 'vetoreason').send_keys('脚本自动审核意见')
        # 点击保存
        get_driver.get_element('rongziguanli-txsh', 'saveBtn').click()
        sleep(3)
        with allure.step("验证提现审核成功"):
            #输入申请编号
            get_driver.get_element('rongziguanli-txsh', 'id').send_keys(sqbh)
            # 点击查询
            get_driver.get_element('rongziguanli-txsh', 'searchbtn').click()
            cxjg=get_driver.get_element('rongziguanli-txsh', 'sqjg').get_attribute('innerText')
            assert cxjg == "没有查询到符合条件的记录"


if __name__ == "__main__":
        pytest.main()
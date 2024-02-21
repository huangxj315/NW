# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰

"""
import pytest
from time import sleep
import allure
from base import base
import os



@allure.feature("供应商-融资管理-我的发票")
class test_wdfp():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-我的发票有查询、申请发票、查看发票操作")
    def test_wdfp(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击我的发票
        get_driver.get_element('rongziguanli-wdfp', 'wdfp').click()
        # 选择已申请状态
        get_driver.get_element('rongziguanli-wdfp', 'ysq').click()
        # 点击发票详情
        get_driver.get_element('rongziguanli-wdfp', 'fpxq').click()
        # 点击发票详情
        get_driver.get_element('rongziguanli-wdfp', 'fpxq').click()
        # 选择未申请状态
        get_driver.get_element('rongziguanli-wdfp', 'wsq').click()
        # 点击申请发票
        get_driver.get_element('rongziguanli-wdfp', 'drawinv').click()



if __name__ == "__main__":
        pytest.main()
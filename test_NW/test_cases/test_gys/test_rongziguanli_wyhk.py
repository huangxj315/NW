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



@allure.feature("供应商-融资管理-我要还款")
class test_rzgl():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-我要还款有查询、查看详情操作")
    def test_wyhk(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击借款编号查看借款详情
        get_driver.get_element('rongziguanli-wyhk', 'loannum').click()
        # 点击关闭按钮
        get_driver.get_next_handle()
        get_driver.get_element('rongziguanli-wyhk', 'closebutton').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-wyhk', 'searchButton').click()


if __name__ == "__main__":
        pytest.main()
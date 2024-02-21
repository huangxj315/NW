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



@allure.feature("供应商-查询统计-提现申请记录")
class test_txsqjl():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-提现申请记录有详情、查询、下载查询结果等操作")
    def test_txsqjl(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击提现申请记录
        get_driver.get_element('chaxuntongji-txsqjl', 'txsqjl').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-txsqjl', 'xqbutton').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_element('chaxuntongji-txsqjl', 'closebutton').click()
        # 点击查询按钮
        get_driver.get_element('chaxuntongji-txsqjl', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('chaxuntongji-txsqjl','exportButton')


if __name__ == "__main__":
        pytest.main()
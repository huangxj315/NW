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



@allure.feature("供应商-查询统计-放款信息查询")
class test_jkjl():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-放款信息查询有查询、详情下载操作")
    def test_fkxxcx(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击放款信息查询
        get_driver.get_element('chaxuntongji-fkxxcx', 'fkxxcx').click()
        # 点击查询按钮
        get_driver.get_element('chaxuntongji-fkxxcx', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('chaxuntongji-fkxxcx','exportButton')
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-fkxxcx', 'xqbutton').click()


if __name__ == "__main__":
        pytest.main()
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



@allure.feature("供应商-查询统计-供应链票据查询")
class test_dzzqpz():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-供应链票据查询有收票、背书转让、提示付款、贴现tab页面")
    def test_shoupiao(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击查询统计tab
        get_driver.get_element('homepage', 'chaxuntongji_tab').click()
        # 点击供应链票据查询
        get_driver.get_element('chaxuntongji-gylpjcx', 'gylpjcx').click()
        sleep(5)
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-gylpjcx', 'xqbutton').click()
        # xq.location_once_scrolled_into_view
        # xq.click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('chaxuntongji-gylpjcx', 'closebutton').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-dzzqpz', 'searchButton').click()
        # 点击背书转让
        get_driver.get_element('chaxuntongji-gylpjcx', 'beishuzhuanrang').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-gylpjcx', 'xqbutton').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('chaxuntongji-gylpjcx', 'closebutton').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-dzzqpz', 'searchButton').click()
        # 点击提示付款
        get_driver.get_element('chaxuntongji-gylpjcx', 'tishifukuan').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-gylpjcx', 'xqbutton').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('chaxuntongji-gylpjcx', 'closebutton').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-dzzqpz', 'searchButton').click()
        # 点击贴现
        get_driver.get_element('chaxuntongji-gylpjcx', 'tiexian').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('chaxuntongji-gylpjcx', 'xqbutton').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('chaxuntongji-gylpjcx', 'closebutton').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('chaxuntongji-dzzqpz', 'searchButton').click()


if __name__ == "__main__":
        pytest.main()
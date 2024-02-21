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



@allure.feature("供应商-融资管理-我的额度")
class test_wded():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-我的额度有查看详情操作")
    def test_wded(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击融资意向
        get_driver.get_element('rongziguanli-wded', 'wded').click()
        # 点击详情
        get_driver.get_element('rongziguanli-wded', 'xq').click()
        #获取列表长度
        get_driver.get_current_handle()
        counts = len(get_driver.get_elements('rongziguanli-wded','loannum'))
        for i in range(counts):
            get_driver.get_current_handle()
            loannum=get_driver.get_elements('rongziguanli-wded','loannum')
            loannum[i].click()
            # 点击详情页面的关闭按钮
            get_driver.get_next_handle()
            get_driver.get_element('rongziguanli-rzyx', 'closebutton').click()
        # 点击详情页面的关闭按钮
        get_driver.get_next_handle()
        get_driver.get_element('rongziguanli-rzyx', 'closebutton').click()
        sleep(3)


if __name__ == "__main__":
        pytest.main()
# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_rongziguanli_pzth.py

"""
import pytest
from time import sleep
import allure
from base import base
import os
from selenium.webdriver.support.select import Select



@allure.feature("供应商-融资管理-凭证退回")
class test_pingzhengtuihui():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-凭证退回有查询、凭证退回申请、查看详情操作")
    def test_pzth(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击凭证退回
        get_driver.get_element('rongziguanli-pzth', 'pzth').click()
        # 输入开立方
        klfname = get_driver.get_paras('klfname', 1)
        get_driver.get_element('rongziguanli-pzth', 'searchklf').send_keys(klfname)
        # 点击查询
        get_driver.get_element('rongziguanli-pzth', 'searchbutton').click()
        sleep(2)
        # 点击查看详情
        get_driver.get_element('rongziguanli-pzth', 'ckxq').click()
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-pzth', 'closebtn').click()
        # 点击凭证退回
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-pzth', 'pzthsq').click()
        # 输入凭证编号
        crpayid=get_driver.get_paras('vouchernum', 1)
        get_driver.get_element('rongziguanli-pzth', 'crpayid').send_keys(crpayid)
        # 输入开立方
        get_driver.get_element('rongziguanli-pzth', 'klfirmname').send_keys(klfname)
        # 输入退回原因
        get_driver.get_element('rongziguanli-pzth', 'backreqmemo').send_keys('脚本自动申请的凭证退回')
        # 点击提交
        get_driver.get_element('rongziguanli-pzth', 'submitBtn').click()
        sleep(2)
        with allure.step("验证该凭证已申请退回成功"):
            # 根据select下拉框的id定位
            statusselect = get_driver.get_element('rongziguanli-pzth', 'statusselect')
            # 选中索引值为1的选项"待审核"（index从0开始）
            Select(statusselect).select_by_index(1)
            # 输入凭证编号
            get_driver.get_element('rongziguanli-pzth', 'crpayidcx').send_keys(crpayid)
            # 点击查询
            get_driver.get_element('rongziguanli-pzth', 'searchbutton').click()
            sleep(2)
            #获取第一条数据财务凭证单号
            result = get_driver.get_element('rongziguanli-pzth', 'cxbh').get_attribute('innerText')
            assert result == crpayid



if __name__ == "__main__":
        pytest.main()
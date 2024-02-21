# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_qfpz.py

"""
from time import sleep

import pytest
import allure

from base import base

@allure.feature("核心企业-签发凭证")
class test_qfpz():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)


    @allure.story("签发债权凭证")
    def test_qfpz(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'核心企业')
        # 点击我的应付
        get_driver.get_element('homepage', 'mypay_tab').click()
        #点击债权凭证签发
        get_driver.get_element('qianfapingzheng', 'voucherissuance').click()
        #获取凭证编号
        billno=get_driver.get_paras('billno',1)
        # 输入应付单号关键字
        get_driver.get_element('qianfapingzheng', 'keyword_input').send_keys(billno)
        # 点击查询
        get_driver.get_element('qianfapingzheng', 'searchButton').click()
        sleep(3)
        # 获取第一条数据财务凭证单号对应的凭证到期日，并存入参数表中
        voucherexpirationdate = get_driver.get_element('qianfapingzheng', 'voucherexpirationdate').get_attribute('innerText')
        with allure.step("将凭证到期日存到参数表中"):
          get_driver.parameter('test_NW','case','voucherexpirationdate',voucherexpirationdate,1)
        # 获取第一条数据财务凭证单号对应的应付金额，并存入参数表中
        voucheramount = get_driver.get_element('qianfapingzheng', 'voucheramount').get_attribute('innerText')
        with allure.step("将应付金额存到参数表中"):
          get_driver.parameter('test_NW','case','voucheramount',voucheramount,1)
        # 点击签发按钮
        get_driver.get_element('qianfapingzheng', 'qianfa').click()
        # 获取第一条数据的开立方，并存入参数表中
        klfname = get_driver.get_element('qianfapingzheng', 'klffirmname').get_attribute('innerText')
        with allure.step("将开立方企业存到参数表中"):
          get_driver.parameter('test_NW','case','klfname',klfname,1)
        # 输入摘要
        get_driver.get_element('qianfapingzheng', 'zhaiyaoinput').send_keys('脚本自动签发凭证'+billno)
        # 点击下一步按钮
        get_driver.get_element('qianfapingzheng', 'nextBtn').click()
        #获取付款承诺函单号，并将财务凭证编号存入参数标中
        billnum = get_driver.get_element('qianfapingzheng', 'billnum').get_attribute('value')
        with allure.step("将财务凭证编号存到参数表中"):
          get_driver.parameter('test_NW','case','billnum',billnum,1)
          # 点击签署按钮
          get_driver.get_element('qianfapingzheng', 'cnfqianshu').click()
          sleep(13)
          # 点击合同确定按钮
          get_driver.get_element('qianfapingzheng', 'okBtn').click()
          # 点击获取验证码按钮
          get_driver.get_element('qianfapingzheng', 'getcode').click()
          # 输入验证码
          get_driver.get_element('qianfapingzheng', 'smscode').send_keys('999999')
          # 点击验证码弹窗确定按钮
          get_driver.get_element('qianfapingzheng', 'confirmBtn').click()
          sleep(3)
          # 再次点击另一个签署按钮
          get_driver.get_element('qianfapingzheng', 'klfqianshu').click()
          sleep(13)
          # 点击合同确定按钮
          get_driver.get_element('qianfapingzheng', 'okBtn').click()
          sleep(3)
          # 点击提交申请按钮
          get_driver.get_element('qianfapingzheng', 'subBtn').click()
          sleep(5)
          with allure.step("验证该凭证已签发成功"):
              result = get_driver.get_element('qianfapingzheng', 'qfwc')
              assert result.text == "签发完成"

if __name__ == "__main__":
        pytest.main()

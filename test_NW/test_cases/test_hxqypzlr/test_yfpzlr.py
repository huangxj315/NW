# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_yfpzlr.py

"""
import datetime
import random
from time import sleep

import pytest
import allure
from openpyxl import Workbook
from selenium import webdriver
from pymouse import PyMouse

from base import base

@allure.feature("核心企业-应付凭证录入")
class test_yfpzlr():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)


    @allure.story("进入我的应付tab")
    def test_yfpzlrfdf(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'核心企业')
        gmf = '大唐电信科技股份有限公司'
        xsf = '安阳钢铁集团有限责任公司'
        # 点击我的应付
        get_driver.get_element('homepage', 'hxmypay_tab').click()
        #生成合同编号
        curr_time = datetime.datetime.now()
        # 获取年月字符串
        year_month = curr_time.strftime('%Y%m')
        contno = curr_time.strftime(year_month + '%d%H%M%S')
        date_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d')
        amount=random.randint(1000, 99999)
        # 选择业务类型（非电费）
        get_driver.get_element('entryvoucher', 'billtype_fdf').click()
        # 输入合同编号
        get_driver.get_element('entryvoucher', 'contno_input').send_keys(contno)
        # 输入合同名称
        get_driver.get_element('entryvoucher', 'contnm_input').send_keys('脚本自动创建' + date_str + contno)
        # 输入合同金额
        get_driver.get_element('entryvoucher', 'contmny_input').send_keys(amount)
        # 输入签订日期
        get_driver.get_element('entryvoucher', 'contsgndt').send_keys(date_str)
        # 点击上传附件
        get_driver.get_element('entryvoucher', 'uploanMYFile').click()
        # 点击选择文件按钮
        get_driver.get_element('entryvoucher', 'webuploader-pick').click()
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\test.png")
        # 点击上传附件后的确定按钮
        get_driver.get_element('entryvoucher', 'uploadbutton').click()
        # 点击导入发票信息
        get_driver.get_element('entryvoucher', 'addCus').click()
        # 点击人工核验tab
        get_driver.get_next_handle()
        get_driver.get_element('entryvoucher', 'manualVerification').click()
        # 输入发票代码
        get_driver.get_element('entryvoucher', 'invcd_input').send_keys(str(contno))
        # 输入开票日期
        get_driver.get_element('entryvoucher', 'invodate').send_keys(date_str)
        # 输入发票号码
        get_driver.get_element('entryvoucher', 'invono_input').send_keys(str(contno))
        # 输入发票金额
        get_driver.get_element('entryvoucher', 'invoamount_input').send_keys(amount)
        # 输入发票总额
        get_driver.get_element('entryvoucher', 'invototalamount_input').send_keys(amount)
        # 输入购买方名称
        get_driver.get_element('entryvoucher', 'buynm_input').send_keys(gmf)
        # 输入销售方名称
        get_driver.get_element('entryvoucher', 'supnm_input').send_keys(xsf)
        # 点击选择文件按钮
        get_driver.get_element('entryvoucher', 'selectbutton').click()
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\test.png")
        # 点击导入按钮
        get_driver.get_element('entryvoucher', 'impBtn').click()
        # 点击保存按钮
        get_driver.get_element('entryvoucher', 'saveBtn').click()
        # 点击选择销售方
        get_driver.get_pre_handle()
        get_driver.get_element('entryvoucher', 'fzhSpan').click()
        #输入销售方名称
        get_driver.get_element('entryvoucher', 'firmname_input').send_keys(xsf)
        #点击销售方查询
        get_driver.get_element('entryvoucher', 'btnGray').click()
        #选择销售方
        get_driver.get_element('entryvoucher', 'select').click()
        #将销售方名称存到参数表
        custname = get_driver.get_element('entryvoucher', 'xiaoshoufang').get_attribute('innerText')
        with allure.step("将客户名称存到参数表中"):
            get_driver.parameter('test_NW', 'case', 'custname', custname, 1)
        #获取应付凭证单号
        billid = get_driver.get_element('entryvoucher', 'billid').get_attribute('value')
        with allure.step("将合同编号存到参数表中"):
          get_driver.parameter('test_NW','case','billno',billid,1)
        #输入应付金额
        get_driver.get_element('entryvoucher', 'paymoney_input').send_keys(amount)
        #获取下一个工作日
        workingday=get_driver.get_workingday(10)
        #输入付款日
        get_driver.get_element('entryvoucher', 'paydate').send_keys(workingday)
        #输入摘要
        get_driver.get_element('entryvoucher', 'billmemo_input').send_keys('脚本自动创建的凭证')
        #点击保存
        get_driver.get_element('entryvoucher', 'subBtn').click()
        sleep(3)
        with allure.step("验证搜索结果和预期一样"):
            # 点击债权凭证签发
            get_driver.get_element('qianfapingzheng', 'voucherissuance').click()
            # 输入应付单号关键字
            get_driver.get_element('qianfapingzheng', 'keyword_input').send_keys(billid)
            # 点击查询
            get_driver.get_element('qianfapingzheng', 'searchButton').click()
            sleep(2)
            #获取第一条数据财务凭证单号
            result1 = get_driver.get_element('qianfapingzheng', 'list_num1').get_attribute('innerText')
            assert result1 == billid

    def test_yfpzlrdf(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '核心企业')
        gmf = '大唐电信科技股份有限公司'
        xsf = '安阳钢铁集团有限责任公司'
        # 点击我的应付
        get_driver.get_element('homepage', 'hxmypay_tab').click()
        # 生成合同编号
        curr_time = datetime.datetime.now()
        # 获取年月字符串
        year_month = curr_time.strftime('%Y%m')
        contno = curr_time.strftime(year_month + '%d%H%M%S')
        date_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d')
        amount = random.randint(1000, 99999)
        # 选择业务类型（非电费）
        get_driver.get_element('entryvoucher', 'billtype_df').click()
        # 输入合同编号
        get_driver.get_element('entryvoucher', 'contno_input').send_keys(contno)
        # 输入合同名称
        get_driver.get_element('entryvoucher', 'contnm_input').send_keys('脚本自动创建' + date_str + contno)
        # 输入合同金额
        get_driver.get_element('entryvoucher', 'contmny_input').send_keys(amount)
        # 输入签订日期
        get_driver.get_element('entryvoucher', 'contsgndt').send_keys(date_str)
        # # 点击贸易合同上传附件
        # get_driver.get_element('entryvoucher', 'uploanMYFile').click()
        # # 点击选择文件按钮
        # get_driver.get_element('entryvoucher', 'webuploader-pick').click()
        # # 选择所需要上传的附件
        # get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\test.png")
        # # 点击上传附件后的确定按钮
        # get_driver.get_element('entryvoucher', 'uploadbutton').click()
        # # 点击导入发票信息
        # get_driver.get_element('entryvoucher', 'addCus').click()
        # # 点击人工核验tab
        # get_driver.get_next_handle()
        # get_driver.get_element('entryvoucher', 'manualVerification').click()
        # # 输入发票代码
        # get_driver.get_element('entryvoucher', 'invcd_input').send_keys(str(contno))
        # # 输入开票日期
        # get_driver.get_element('entryvoucher', 'invodate').send_keys(date_str)
        # # 输入发票号码
        # get_driver.get_element('entryvoucher', 'invono_input').send_keys(str(contno))
        # # 输入发票金额
        # get_driver.get_element('entryvoucher', 'invoamount_input').send_keys(amount)
        # # 输入发票总额
        # get_driver.get_element('entryvoucher', 'invototalamount_input').send_keys(amount)
        # # 输入购买方名称
        # get_driver.get_element('entryvoucher', 'buynm_input').send_keys(gmf)
        # # 输入销售方名称
        # get_driver.get_element('entryvoucher', 'supnm_input').send_keys(xsf)
        # # 点击选择文件按钮
        # get_driver.get_element('entryvoucher', 'selectbutton').click()
        # # 选择所需要上传的附件
        # get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\test.png")
        # # 点击导入按钮
        # get_driver.get_element('entryvoucher', 'impBtn').click()
        # # 点击保存按钮
        # get_driver.get_element('entryvoucher', 'saveBtn').click()
        # 点击选择销售方
        get_driver.get_pre_handle()
        get_driver.get_element('entryvoucher', 'fzhSpan').click()
        # 输入销售方名称
        get_driver.get_element('entryvoucher', 'firmname_input').send_keys(xsf)
        # 点击销售方查询
        get_driver.get_element('entryvoucher', 'btnGray').click()
        # 选择销售方
        get_driver.get_element('entryvoucher', 'select').click()
        # 将销售方名称存到参数表
        custname = get_driver.get_element('entryvoucher', 'xiaoshoufang').get_attribute('innerText')
        with allure.step("将客户名称存到参数表中"):
            get_driver.parameter('test_NW', 'case', 'custname', custname, 1)
        # 获取应付凭证单号
        billid = get_driver.get_element('entryvoucher', 'billid').get_attribute('value')
        with allure.step("将合同编号存到参数表中"):
            get_driver.parameter('test_NW', 'case', 'billno', billid, 1)
        # 输入应付金额
        get_driver.get_element('entryvoucher', 'paymoney_input').send_keys(amount)
        # 获取下一个工作日
        workingday = get_driver.get_workingday(10)
        # 输入付款日
        get_driver.get_element('entryvoucher', 'paydate').send_keys(workingday)
        # 输入摘要
        get_driver.get_element('entryvoucher', 'billmemo_input').send_keys('脚本自动创建的凭证')
        # 点击保存
        get_driver.get_element('entryvoucher', 'subBtn').click()
        sleep(3)
        with allure.step("验证搜索结果和预期一样"):
            # 点击债权凭证签发
            get_driver.get_element('qianfapingzheng', 'voucherissuance').click()
            # 输入应付单号关键字
            get_driver.get_element('qianfapingzheng', 'keyword_input').send_keys(billid)
            # 点击查询
            get_driver.get_element('qianfapingzheng', 'searchButton').click()
            sleep(2)
            # 获取第一条数据财务凭证单号
            result1 = get_driver.get_element('qianfapingzheng', 'list_num1').get_attribute('innerText')
            assert result1 == billid


if __name__ == "__main__":
    pytest.main()
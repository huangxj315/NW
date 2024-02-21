# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_gyschupiao.py

"""
from time import sleep

import pytest
import allure
from selenium.webdriver.support.ui import Select
from base import base

@allure.feature("供应商-供应链票据出票申请")
class test_gyschupiao():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)


    @allure.story("有合同信息出票申请")
    def test_gyscp(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'供应商')
        # 点击我的应付
        get_driver.get_element('homepage', 'mypay_tab').click()
        #点击出票申请
        get_driver.get_element('gyschupiao', 'cpsq').click()
        #获取凭证编号
        billno=get_driver.get_paras('billno',1)
        # 输入应付单号关键字
        get_driver.get_element('gyschupiao', 'keyword_input').send_keys(billno)
        # 点击查询
        get_driver.get_element('gyschupiao', 'searchButton').click()
        sleep(3)
        # # 获取第一条数据财务凭证单号对应的凭证到期日，并存入参数表中
        # voucherexpirationdate = get_driver.get_element('qianfapingzheng', 'voucherexpirationdate').get_attribute('innerText')
        # with allure.step("将凭证到期日存到参数表中"):
        #   get_driver.parameter('test_NW','case','voucherexpirationdate',voucherexpirationdate,1)
        # 获取第一条数据财务凭证单号对应的应付金额，并存入参数表中
        voucheramount = get_driver.get_element('qianfapingzheng', 'voucheramount').get_attribute('innerText')
        cpje = voucheramount.replace(",", "")
        # with allure.step("将应付金额存到参数表中"):
        #   get_driver.parameter('test_NW','case','voucheramount',voucheramount,1)
        # 点击申请按钮
        get_driver.get_element('gyschupiao', 'shenqing').click()
        # 点击出票方银行账户选择按钮
        chooses = get_driver.get_elements('gyschupiao', 'yhzhxz')
        for i in chooses:
            i.click()
            # 选择出票方银行账户
            table = get_driver.get_element('gyschupiao', 'zhlist')
            tbody = table.find_element_by_tag_name('tbody')
            # 迭代每个 <tbody> 元素
            for tr in tbody.find_elements_by_tag_name('tr'):
                # 获取此行中的每个单元格 <td>，并获取该单元格的文本
                tds = tr.find_elements_by_tag_name('td')
                kaihuhang = tds[2]  # 获取第三列元素
                choose = tds[-1]  # 获取最后一列元素
                if kaihuhang.text == '浙商银行股份有限公司杭州分行营业部':
                    choose.click()
                    sleep(1)
                    break
        # 输入出票金额
        get_driver.get_element('gyschupiao', 'cpamt').send_keys(cpje)
        #点击贸易方式
        myfs=Select(get_driver.get_element('gyschupiao', 'myfs'))
        myfs.select_by_visible_text("服务贸易")
        # 点击下一步
        get_driver.get_element('gyschupiao', 'nextBtn').click()
        # 点击提交申请
        get_driver.get_element('gyschupiao', 'subBtn').click()
        with allure.step("验证该应付已出票成功"):
            result = get_driver.get_element('gyschupiao', 'cpwc')
            assert result.text == "凭证已申请出票成功，请等待审核"
if __name__ == "__main__":
        pytest.main()

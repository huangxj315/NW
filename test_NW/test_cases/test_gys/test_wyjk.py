# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/26 11:28
@Auth ： 黄香杰
@File ：test_wyjk.py

"""
import locale
from time import sleep
import pytest
import allure
from base import base

@allure.feature("供应商-我要借款")
class test_wyjk():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)



    @allure.story("选择电子债权凭证我要借款--全额融资")
    def test_wyjkall(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'供应商')
        # 点击我要借款tab
        get_driver.get_element('homepage', 'mytoloan_tab').click()
        #点击电子债权凭证-英大牌照后的我要借款
        divs = get_driver.get_elements('mytoloan', 'div_locator')
        # 定义一个标志变量
        should_break = False
        for div in divs:
           # 找到每个 <div> 元素中的 <p> 元素
           fdjgs = div.find_elements_by_tag_name('p')
           for fdjg in fdjgs:
               # 英大放贷机构下的电子债权凭证
               if fdjg.text=='放贷机构：英大国际信托有限责任公司':
                  table=fdjg.find_element_by_xpath("following-sibling::table")
                  # 迭代每个 <table> 元素
                  for tr in table.find_elements_by_tag_name('tr'):
                      # 获取此行中的每个单元格 <td>，并获取该单元格的文本
                      tds = tr.find_elements_by_tag_name('td')
                      if len(tds) < 2:
                        continue

                      col1_element = tds[0]  # 获取第一列元素
                      last_cell = tds[-1]  # 获取最后一列元素
                      p_element1 = col1_element.find_element_by_xpath('.//h1')  # 在第一列的元素上查找 'h1' 标签
                      rzpz = p_element1.text  # 获取第一列的 'p' 标签文本
                      if rzpz == '电子债权凭证融资' :
                         last_cell.click()
                         # 设置标志变量为 True，表示应该跳出外层循环
                         should_break = True
                         break
                  # 检查标志变量是否为 True，如果是，则跳出外层循环
                  if should_break:
                     break
           if should_break:
            break
        #获取凭证金额
        # 设置当前的locale为你所使用的地区的格式
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        amount=get_driver.get_paras('voucheramount', 1)
        # 将字符串转换为浮点数
        amount_float = locale.atof(amount)
        money=int(amount_float)
        #获取凭证到期日
        expiredate=get_driver.get_paras('voucherexpirationdate', 1)
        # 获取我要借款列表
        table = get_driver.get_element('mytoloan', 'loanlist')
        tbody = table.find_element_by_tag_name('tbody')
        # 迭代每个 <tbody> 元素
        for tr in tbody.find_elements_by_tag_name('tr'):
            # 获取此行中的每个单元格 <td>，并获取该单元格的文本
            tds = tr.find_elements_by_tag_name('td')
            loanexpirdate = tds[0]  # 获取第一列元素
            vouchernum1 = tds[1]  # 获取第二列元素
            loanmoney1 = tds[4]  # 获取第五列元素
            loanmoney=loanmoney1.text
            num = int(loanmoney.replace(',', '').split('.')[0])
            loanbutton = tds[-1]  # 获取最后一列元素
            if loanexpirdate.text == expiredate and num == money:
                vouchernum=vouchernum1.text
                with allure.step("将凭证编号存到参数表中"):
                    get_driver.parameter('test_NW', 'case', 'vouchernum', vouchernum, 1)
                loanbutton.click()
                break
        #点击完善合同下一步
        get_driver.get_element('mytoloan', 'nextBtn').click()
        # 点击申请借款下一步
        get_driver.get_element('mytoloan', 'sqjknext').click()
        # 点击签署
        get_driver.get_element('mytoloan', 'signbtn').click()
        sleep(13)
        # 点击签署页面确定按钮
        get_driver.get_element('mytoloan', 'okBtn').click()
        sleep(3)
        # 点击提交按钮
        get_driver.get_element('mytoloan', 'subBtn').click()
        with allure.step("验证借款申请成功"):
            result = get_driver.get_element('mytoloan', 'jkcg')
            assert result.text == "您的借款申请已提交成功，请等待审核。"
        # 点击查看借款信息
        get_driver.get_element('mytoloan', 'ckjkxx').click()
        sleep(3)
        # 获取借款编号
        loannum = get_driver.get_element('mytoloan', 'jkbh').get_attribute('innerText')
        with allure.step("将借款编号存到参数表中"):
            get_driver.parameter('test_NW', 'case', 'loannum', loannum, 1)

if __name__ == "__main__":
        pytest.main()

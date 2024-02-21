# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_jksh.py

"""

from time import sleep
import allure
import pytest
import locale

from base import base

@allure.feature("运营端借款审核")
class test_jksh():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)



    @allure.story("借款审核")
    def test_jksh(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'运营')
        rq=get_driver.get_currentrq()
        # 设置当前的locale为你所使用的地区的格式
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        amount=get_driver.get_paras('voucheramount', 1)
        # 将字符串转换为浮点数
        amount_float = locale.atof(amount)
        money=int(amount_float)
        #点击凭证后的借款审核
        divs = get_driver.get_elements('yydjksh', 'div_locator')
        # 定义一个标志变量
        should_break = False
        for div in divs:
           table = div.find_element_by_tag_name('table')
           # 迭代每个 <table> 元素,内层循环
           for tr in table.find_elements_by_tag_name('tr'):
               # 获取此行中的每个单元格 <td>，并获取该单元格的文本
               tds = tr.find_elements_by_tag_name('td')
               if len(tds) < 2:
                continue
               col1_element = tds[0]  # 获取第一列元素
               col2_element = tds[1]  # 获取第一列元素
               last_cell = tds[-1]  # 获取最后一列元素
               p_element1 = col1_element.find_element_by_xpath('.//p[1]')  # 在第一列的元素上查找 'p' 标签
               p_element2 = col2_element.find_element_by_xpath('.//p[1]')  # 在第二列的元素上查找 'p' 标签
               date = p_element1.text  # 获取第一列的 'p' 标签文本
               loanmoney = p_element2.text  # 获取第二列的 'p' 标签文本
               num=int(loanmoney.replace(',', '').split('.')[0])
               # 检查第一列和第二列是否等于指定的值，如果是，则单击该行元素中的“签收凭证”按钮
               if date == rq and num == money:
                   last_cell.click()
                   # 设置标志变量为 True，表示应该跳出外层循环
                   should_break = True
                   break
           # 检查标志变量是否为 True，如果是，则跳出外层循环
           if should_break:
               break

        # 点击签署按钮
        get_driver.get_element('mytodo', 'jsfqianshu').click()





if __name__ == "__main__":
    pytest.main()
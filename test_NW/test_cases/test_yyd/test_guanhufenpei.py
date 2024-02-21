# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_guanhufenpei.py

"""
from time import sleep
import allure
from base import base

@allure.feature("首次管户分配")
class test_guanhufenpei():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)



    @allure.story("首次管户分配")
    def test_khfp(self,get_driver):
        #用户登录
        get_driver.start_houtai(1,'运营')
        #获取当前用户的用户名称
        _, _, _, getUsername = get_driver.get_user(1,'运营')
        # 点击客户管理
        get_driver.get_element('guanhufenpei', 'khgl').click()
        #获取待管户分配的列表
        divs = get_driver.get_elements('guanhufenpei', 'div_locator')
        # 定义一个标志变量
        should_break = False
        for div in divs:
           # 找到每个 <div> 元素中的 <table> 元素
           table = div.find_element_by_tag_name('table')
           tbody = table.find_element_by_tag_name('tbody')
           for tr in tbody.find_elements_by_tag_name('tr'):
               # 获取此行中的每个单元格 <td>，并获取该单元格的文本
               tds = tr.find_elements_by_tag_name('td')
               col2_element= tds[1]  # 获取第二列元素
               lastcol_element = tds[-1]  # 获取最后一列元素
               p_element1 = col2_element.find_element_by_xpath('.//p[1]')  # 在第二列的元素上查找 'p' 标签
               cusna = get_driver.get_paras('custname', 1)
               if p_element1.text == cusna:
                   lastcol_element.click()
                   break

           if should_break:
                     break

        # 点击客户管理
        get_driver.get_element('guanhufenpei', 'choose').click()
        #输入客户经理名称
        get_driver.get_element('guanhufenpei', 'nameinput').send_keys(getUsername)
        # 点击查询按钮
        get_driver.get_element('guanhufenpei', 'searchbutton').click()
        # 选中该客户经理
        get_driver.get_element('guanhufenpei', 'sel').click()
        # 选中该客户经理后，点击确定
        get_driver.get_element('guanhufenpei', 'confbtn').click()
        # 点击提交
        get_driver.get_element('guanhufenpei', 'saveBtn').click()
    @allure.story("管户分配后客户签收")
    def test_khqs(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '运营')
        # 点击客户管理
        get_driver.get_element('guanhufenpei', 'khgl').click()
        # 获取待管户分配的列表
        divs = get_driver.get_elements('guanhufenpei', 'div_locator')
        # 定义一个标志变量
        should_break = False
        for div in divs:
            # 找到每个 <div> 元素中的 <table> 元素
            table = div.find_element_by_tag_name('table')
            tbody = table.find_element_by_tag_name('tbody')
            for tr in tbody.find_elements_by_tag_name('tr'):
                # 获取此行中的每个单元格 <td>，并获取该单元格的文本
                tds = tr.find_elements_by_tag_name('td')
                col2_element = tds[1]  # 获取第二列元素
                lastcol_element = tds[-1]  # 获取最后一列元素
                p_element1 = col2_element.find_element_by_xpath('.//p[1]')  # 在第二列的元素上查找 'p' 标签
                cusna = get_driver.get_paras('custname', 1)
                if p_element1.text == cusna:
                    lastcol_element.click()
                    break

            if should_break:
                break

        # 点击提交
        # get_driver.get_element('guanhufenpei', 'saveBtn').click()

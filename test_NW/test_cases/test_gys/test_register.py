# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/17 15:34
@Auth ： 黄香杰
@File ：test_register.py

"""
import io
import re
from copy import copy
from xlutils.copy import copy

from selenium import webdriver
from time import sleep
import datetime
import requests
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from pytesseract import image_to_string
import pytest
import allure
from base import base
import xlrd
import os
from openpyxl import load_workbook



@allure.feature("供应商-注册新的账户")
class test_register():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    def test_register(self, get_driver):
        #打开注册地址
        get_driver.get_registerurl()
        #输入手机号
        telphonenum = get_driver.generate_phone_number()
        get_driver.get_element('gysregister', 'telphone_input').send_keys(telphonenum)
        # # 定义图片验证码的URL地址
        # img = get_driver.get_element('gysregister', 'codeimg')
        # # 获取验证码元素位置和大小
        # captcha_location = img.location
        # captcha_size = img.size
        #
        # # 截取验证码图片区域
        # screenshot = webdriver.get_screenshot_as_png()
        # screenshot_image = Image.open(io.BytesIO(screenshot))
        # captcha_image = screenshot_image.crop((captcha_location['x'], captcha_location['y'],captcha_location['x'] + captcha_size['width'],captcha_location['y'] + captcha_size['height']))
        #
        # # 保存验证码图片
        # captcha_image.save("captcha.png")
        # # 对验证码图片进行处理和识别
        # captcha_image = Image.open("captcha.jpg")
        # # 将彩色图像转换为灰度图像
        # gray_image = captcha_image.convert('L')
        #
        # # 进行二值化处理
        # threshold = 150  # 二值化阈值
        # binary_image = gray_image.point(lambda x: 0 if x < threshold else 255, '1')
        #
        # # 进行降噪处理,去除干扰线
        # denoised_image = binary_image.filter(ImageFilter.MedianFilter(size=3))
        # #denoised_image = binary_image.filter(ImageFilter.SMOOTH_MORE)
        # # 将降噪后的图像转换为 RGB 模式
        # rgb_image = denoised_image.convert("RGB")
        # # 增强对比度
        # enhancer = ImageEnhance.Contrast(rgb_image)
        # contrast_image = enhancer.enhance(2.0)  # 增强对比度的参数可以根据需求调整
        # # 将彩色图像转换为灰度图像
        # gray_image = contrast_image.convert('L')
        # # 保存降噪和增强后的图像
        # gray_image.save("captcha_processed.jpg")
        # convert_image = Image.open("captcha_processed.jpg")
        # imgcode_content = pytesseract.image_to_string(convert_image)
        # textCode = re.sub("\W", "", imgcode_content)
        # # 打印图片验证码内容
        # print(imgcode_content)
        # 输入图片验证码
        get_driver.get_element('gysregister', 'img_input').send_keys('9999')
        # 点击下一步
        get_driver.get_element('gysregister', 'nextbtn').click()
        sleep(2)
        # 输入短信验证码
        get_driver.get_element('gysregister', 'code_input').send_keys('999999')
        # 点击下一步
        get_driver.get_element('gysregister', 'nextbtn').click()
        sleep(2)
        # 输入密码
        get_driver.get_element('gysregister', 'pass_input').send_keys('a123456')
        # 输入确认密码
        get_driver.get_element('gysregister', 'pass2_input').send_keys('a123456')
        # 点击提交
        get_driver.get_element('gysregister', 'nextbtn').click()
        with allure.step("注册成功"):
            result = get_driver.get_element('gysregister', 'succ')
            assert result.text == "注册成功"
        with allure.step("将手机号存到登录表"):
            user_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),'parameter','users.xls')
            # # 打开 Excel 文件，获取工作对象
            userFile = xlrd.open_workbook(user_file)
            # 获取工作缝中的第一个工作表
            usersheet=userFile.sheet_by_index(0)
            #通过 CoDy 方法获取可写入的副本
            writeuser=copy(userFile)
            writeusersheet=writeuser.get_sheet(0)
            #修改指定单元格内容
            writeusersheet.write(6,0,telphonenum)
            #保存修改后的 Excel 文件
            writeuser.save(user_file)







if __name__ == "__main__":
        pytest.main()

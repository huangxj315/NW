# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/30 10:58
@Auth ： 黄香杰
@File ：conftest.py

"""
from selenium import webdriver
import pytest
from base import base
import os
from test_NW.base.base_NW import base_NW
import allure
from PIL import ImageGrab
import cv2
import numpy as np
import time,threading
import datetime
import xlrd


base = base()
video_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'video')

@pytest.fixture(scope='function')
def get_driver():
    # #添加初始系统测试数据
    #开始录制
    global video_flag
    video_flag = False
    #谷歌接口日志配置
    caps = {
        'browserName': 'chrome',
        'loggingPrefs': {
            'browser': 'ALL',
            'driver': 'ALL',
            'performance': 'ALL',
        },
        'goog:chromeOptions': {
            'perfLoggingPrefs': {
                'enableNetwork': True,
            },
            'w3c': False,
        },
    }
    #打开谷歌
    global driver
    # 个人资料路径
    user_data_dir = (r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
    # 加载配置数据
    option = webdriver.ChromeOptions()
    option.add_argument(user_data_dir)
    # 启动浏览器配置
    driver = webdriver.Chrome(options=option, executable_path=r'E:\Python\chromedriver.exe',desired_capabilities=caps)
    #窗口最大
    driver.maximize_window()
    NW = base_NW(driver)
    th = threading.Thread(target=video_record,args = (getVideoPath(),))
    th.start()
    yield NW
    video_flag = True
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    global caseResult
    if rep.when == "call" and rep.failed:
        caseResult = 'fail'
        allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
    else:
        caseResult = 'success'



def video_record(name):  # 录入视频
    fps = 15
    screen = ImageGrab.grab()  # 获取当前屏幕
    width, high = screen.size  # 获取当前屏幕的大小
    name = name + '.avi'
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # MPEG-4编码,文件后缀可为.avi .asf .mov等
    video = cv2.VideoWriter(name, fourcc, fps, (width, high))  # （文件名，编码器，帧率，视频宽高）
    # print('3秒后开始录制----')  # 可选
    # time.sleep(3)
    print('开始录制!')
    global start_time,video_flag,caseResult
    start_time = time.time()
    while True:
        if video_flag:
            print("录制结束！")
            global final_time
            final_time = time.time()
            video.release()  # 释放
            #若用例执行失败，则生成视频
            if caseResult == 'fail':
                getName_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'parameter','caseName.xls')
                xlsx = xlrd.open_workbook(getName_path)
                table = xlsx.sheet_by_name("Sheet1")
                value = table.cell_value(0,0)
                newName = os.path.join(video_path, value + '~' + name.split('\\')[-1])
                os.rename(name,newName)
            else:
                # 若用例执行成功，则删除视频
                os.remove(name)
            break
        im = ImageGrab.grab()  # 屏幕抓图，图片为RGB模式
        frame = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)  # 转为opencv的BGR模式
        video.write(frame)  # 写入vedio定义的文件
        # time.sleep(5) # 等待5秒再次循环,控制帧数
        # 等0.1毫秒---十分之一秒--10帧/秒


#获取录像名称
def getVideoPath():
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return os.path.join(video_path, nowTime)
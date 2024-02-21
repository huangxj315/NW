# -*- coding: utf-8 -*-
"""
@Time ： 2023/3/28 17:53
@Auth ： 黄香杰
@File ：base.py
"""
import os
import datetime
import subprocess
from datetime import datetime
import xlrd
from xlutils.copy import copy
import re


class base():
    # 获取当前时间函数
    def get_time(self):
        curr_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d-%H-%M-%S')
        return time_str

    #调用jmeter批量制作测试数据
    def add_TestData(self,path,jmx):
        now_time = self.get_time()#时间戳
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)),path)
        jmx_file = os.path.join(path,'jmx',jmx + '.jmx')  # jmx文件路径
        print(jmx_file)
        result_name = 'result-' + now_time + '.csv'#结果文件名
        result_file = os.path.join(path,result_name)#执行结果文件
        run_cmd = f'jmeter -n -t {jmx_file} -l {result_file}'  # 无界面运行JMeter压测命令
        # 需要获取屏幕输出是，可以使用subprocess.Popen()
        p1 = subprocess.Popen(run_cmd, shell=True, stdout=subprocess.PIPE)
        print(p1.stdout.read().decode('utf-8'))

    # 测试名称/结果写入caseName临时表
    def caseName(self, path, content):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path, 'parameter', 'caseName.xls')
        # 打开想要更改的excel文件
        old_excel = xlrd.open_workbook(path, formatting_info=True)
        # 将操作文件对象拷贝，变成可写的workbook对象
        new_excel = copy(old_excel)
        # 获得第一个sheet的对象
        ws = new_excel.get_sheet(0)
        ws.write(0, 0, content)
        # 另存为excel文件，并将文件命名
        new_excel.save(path)
    # 测试参数写入临时表
    def parameter(self, path,type,parametername,content,num):
        if type == 'main':
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path, 'parameter', 'parameter-main.xls')
        else:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path, 'parameter', 'parameter.xls')
        # 打开想要更改的excel文件
        old_excel = xlrd.open_workbook(path, formatting_info=True)
        # 将操作文件对象拷贝，变成可写的workbook对象
        new_excel = copy(old_excel)
        # 获得第一个sheet的对象
        if parametername=='partnername':
            ws = new_excel.get_sheet(0)
            ws.write(num-1, 0, content)
        # if parametername=='productname':
        #     ws = new_excel.get_sheet(1)
        #     ws.write(num-1, 0, content)
        if parametername == 'billno':
            ws = new_excel.get_sheet(1)
            ws.write(num-1, 0, content)
        if parametername == 'dpinvoicenum':
            ws = new_excel.get_sheet(2)
            ws.write(num-1, 0, content)
        if parametername == 'paymentnum':
            ws = new_excel.get_sheet(3)
            ws.write(num-1, 0, content)
        if parametername == 'shipmentnum':
            ws = new_excel.get_sheet(4)
            ws.write(num-1, 0, content)
        if parametername == 'piinvoicenum':
            ws = new_excel.get_sheet(5)
            ws.write(num-1, 0, content)
        if parametername=='otherinvoicenum':
            ws = new_excel.get_sheet(6)
            ws.write(num-1, 0, content)
        if parametername=='forwardername':
            ws = new_excel.get_sheet(7)
            ws.write(num-1, 0, content)
        # 另存为excel文件，并将文件命名
        new_excel.save(path)


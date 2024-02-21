# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：allureRun_allCase.py

"""
import os
import datetime
import pytest





#用例路径
case_path = os.path.join(os.path.dirname(os.getcwd()),'test_cases')
#结果数据路径
result_path = os.path.join(os.path.dirname(os.getcwd()),'report',datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
#allure报告路径
allure_path = os.path.join(result_path,'allure')


#生成路径文件夹
if os.path.exists(result_path):
    pass
else:
    os.mkdir(result_path)
    os.mkdir(allure_path)


#pytest执行全部用例
pytest.main(['-s','-vv',case_path,'--alluredir',result_path])
#生成allure报告
report_cmd = r'allure generate '+ '"' + result_path + '"' + r' -o ' + '"' + allure_path + '"' + ' --clean'
os.system(report_cmd)
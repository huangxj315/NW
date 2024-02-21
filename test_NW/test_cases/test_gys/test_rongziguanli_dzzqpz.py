# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_chaxuntongji_edsqjl.py

"""
import pytest
from time import sleep
import allure
from base import base
import os



@allure.feature("供应商-融资管理-电子债权凭证")
class test_dzzqpz():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    @allure.feature("供应商-电子债权凭证有待签收、已签收、已否决、已转让、已融资、已到期tab页面")
    def test_daiqianshou(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击电子债权凭证
        get_driver.get_element('rongziguanli-dzzqpz', 'dzzqpz').click()
        # 点击详情按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'xqbutton').click()
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'closebutton').click()
        # 点击查看流转路径按钮
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'lzljbutton').click()
        # 点击查看详情
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'chakanxiangqing').click()
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'closebutton').click()
        # 点击融资管理tab
        get_driver.get_pre_handle()
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击电子债权凭证
        get_driver.get_element('rongziguanli-dzzqpz', 'dzzqpz').click()
        # 点击查询按钮
        # get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('rongziguanli-dzzqpz','exportButton')
        # 点击签收按钮
        get_driver.get_element('rongziguanli-dzzqpz','qianshou').click()
        sleep(3)
        counts = len(get_driver.get_elements('rongziguanli-dzzqpz','qianshu'))
        for i in range(counts):
            qianshu=get_driver.get_elements('rongziguanli-dzzqpz','qianshu')
            qianshu[i].click()
            sleep(13)
            # 点击合同确定按钮
            get_driver.get_element('qianfapingzheng', 'okBtn').click()
            sleep(5)
        # 点击签收页面的取消按钮
        get_driver.download_query_results('rongziguanli-dzzqpz','cancelbutton')

    def test_yiqianshou(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击电子债权凭证
        get_driver.get_element('rongziguanli-dzzqpz', 'dzzqpz').click()
        # 点击已签收
        get_driver.get_element('rongziguanli-dzzqpz', 'yiqianshou').click()
        # 点击详情按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'xqbutton1').click()
        sleep(3)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'closebutton').click()
        # 点击凭证下载按钮
        get_driver.get_pre_handle()
        get_driver.download_query_results('rongziguanli-dzzqpz','xiazaibutton1')
        # 点击查看流转路径按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'lzljbutton1').click()
        # 点击查看详情
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'chakanxiangqing').click()
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'closebutton').click()
        # 点击融资管理tab
        get_driver.get_pre_handle()
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击电子债权凭证
        get_driver.get_element('rongziguanli-dzzqpz', 'dzzqpz').click()
        # 点击已签收
        get_driver.get_element('rongziguanli-dzzqpz', 'yiqianshou').click()
        # 点击查询按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'searchButton').click()
        sleep(2)
        # 点击下载查询结果按钮
        get_driver.download_query_results('rongziguanli-dzzqpz','exportButton')
        sleep(2)
        # 点击批量下载凭证按钮
        get_driver.download_query_results('rongziguanli-dzzqpz','downZipButton')
        sleep(2)
        # 点击转让按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'zhuanrang').click()
        # 点击选择接收方
        get_driver.get_element('rongziguanli-dzzqpz', 'fzhSpan').click()
        #输入接收方名称
        get_driver.get_element('rongziguanli-dzzqpz', 'firmname_input').send_keys('北京超越')
        #点击接收方查询
        get_driver.get_element('rongziguanli-dzzqpz', 'btnGray').click()
        #选择接收方
        get_driver.get_element('rongziguanli-dzzqpz', 'select').click()
        #输入付款金额
        get_driver.get_element('rongziguanli-dzzqpz', 'payamount').send_keys('10')
        #输入摘要
        get_driver.get_element('rongziguanli-dzzqpz', 'memo').send_keys('脚本自动转让')
        #点击下一步
        get_driver.get_element('rongziguanli-dzzqpz', 'nextBtn').click()
        # 点击签署按钮
        get_driver.get_element('rongziguanli-dzzqpz','qianshu').click()
        sleep(13)
        # 点击合同确定按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'okBtn').click()
        sleep(3)
        # 点击确认支付按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'savebutton').click()
        sleep(5)
        with allure.step("验证该凭证已转让成功"):
            result = get_driver.get_element('rongziguanli-dzzqpz', 'zrwc')
            assert result.text == "支付信息已提交，请等待收款方签收。"




    def test_yifoujue(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击电子债权凭证
        get_driver.get_element('rongziguanli-dzzqpz', 'dzzqpz').click()
        sleep(2)
        # 点击已否决
        get_driver.get_element('rongziguanli-dzzqpz', 'yifoujue').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'xqbutton2').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'closebutton').click()
        # 点击查看流转路径按钮
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'lzljbutton2').click()
        # 点击查询按钮
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('rongziguanli-dzzqpz','exportButton')
    def test_yizhuanrang(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击电子债权凭证
        get_driver.get_element('rongziguanli-dzzqpz', 'dzzqpz').click()
        sleep(2)
        # 点击已转让
        get_driver.get_element('rongziguanli-dzzqpz', 'yizhuanrang').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'xqbutton3').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'closebutton').click()
        # 点击查看流转路径按钮
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'lzljbutton3').click()
        # 点击凭证下载按钮
        get_driver.get_pre_handle()
        get_driver.download_query_results('rongziguanli-dzzqpz','xiazaibutton3')
        # 点击查询按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('rongziguanli-dzzqpz','exportButton')
    def test_yirongzi(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击电子债权凭证
        get_driver.get_element('rongziguanli-dzzqpz', 'dzzqpz').click()
        sleep(2)
        # 点击已融资
        get_driver.get_element('rongziguanli-dzzqpz', 'yirongzi').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'xqbutton4').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'closebutton').click()
        # 点击查看流转路径按钮
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'lzljbutton4').click()
        # 点击凭证下载按钮
        get_driver.get_pre_handle()
        sleep(2)
        get_driver.download_query_results('rongziguanli-dzzqpz','xiazaibutton4')
        # 点击查询按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('rongziguanli-dzzqpz','exportButton')
    def test_yidaoqi(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1, '供应商')
        # 点击融资管理tab
        get_driver.get_element('homepage', 'rongziguanli_tab').click()
        # 点击电子债权凭证
        get_driver.get_element('rongziguanli-dzzqpz', 'dzzqpz').click()
        sleep(2)
        # 点击已到期
        get_driver.get_element('rongziguanli-dzzqpz', 'yidaoqi').click()
        sleep(2)
        # 点击详情按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'xqbutton4').click()
        sleep(2)
        # 点击关闭按钮
        get_driver.get_current_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'closebutton').click()
        # 点击查看流转路径按钮
        get_driver.get_pre_handle()
        get_driver.get_element('rongziguanli-dzzqpz', 'lzljbutton4').click()
        # 点击凭证下载按钮
        get_driver.get_pre_handle()
        sleep(2)
        get_driver.download_query_results('rongziguanli-dzzqpz','xiazaibutton4')
        # 点击查询按钮
        get_driver.get_element('rongziguanli-dzzqpz', 'searchButton').click()
        # 点击下载查询结果按钮
        get_driver.download_query_results('rongziguanli-dzzqpz','exportButton')



if __name__ == "__main__":
        pytest.main()
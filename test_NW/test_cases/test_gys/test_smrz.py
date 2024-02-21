# -*- coding: utf-8 -*-
"""
@Auth ： 黄香杰
@File ：test_smrz.py

"""
import random
from time import sleep
import pytest
import allure
from base import base
from selenium.webdriver.support.ui import Select



@allure.feature("供应商-注册新的账户-新供应商实名认证")
class test_smrz():

    def setup_method(self,method):
        mybase = base()
        mybase.caseName('test_NW', method.__name__)

    def test_smrz(self, get_driver):
        # 用户登录
        get_driver.start_houtai(1,'新供应商')
        #生成企业名称
        companyname=get_driver.generate_company_name()
        #输入企业名称
        #get_driver.get_element('smrz','firmname').send_keys(companyname)
        get_driver.get_element('smrz', 'firmname').send_keys('山东鲁能光大电力器材有限公司')
        # 生成统一社会信用代码
        credit_code = get_driver.generate_uscc()
        #输入企业统一社会信用代码
        #get_driver.get_element('smrz','yingyezz').send_keys(credit_code)
        get_driver.get_element('smrz', 'yingyezz').send_keys('91370800726226375E')
        #点击企业规模
        qygm=Select(get_driver.get_element('smrz', 'qiygm'))
        qygm.select_by_visible_text("大型企业")
        #点击企业类型
        qygm=Select(get_driver.get_element('smrz', 'qiyeleix'))
        qygm.select_by_visible_text("国有")
        #点击所属行业
        qygm=Select(get_driver.get_element('smrz', 'oneselect'))
        qygm.select_by_visible_text("电力、热力、燃气及水生产和供应业")
        #点击所属行业
        qygm=Select(get_driver.get_element('smrz', 'twoselect'))
        qygm.select_by_visible_text("电力、热力生产和供应业")
        #点击所属行业
        qygm=Select(get_driver.get_element('smrz', 'threeselect'))
        qygm.select_by_visible_text("电力生产")
        #点击所属行业
        qygm=Select(get_driver.get_element('smrz', 'fourselect'))
        qygm.select_by_visible_text("太阳能发电")
        #点击大区
        qygm=Select(get_driver.get_element('smrz', 'areaSelect'))
        qygm.select_by_visible_text("华中")
        sleep(3)
        #点击省
        qygm=Select(get_driver.get_element('smrz', 'provinceSelect'))
        qygm.select_by_visible_text("河南省")
        #点击市
        qygm=Select(get_driver.get_element('smrz', 'citySelect'))
        qygm.select_by_visible_text("郑州市")
        #点击县
        qygm=Select(get_driver.get_element('smrz', 'regionSelect'))
        qygm.select_by_visible_text("管城回族区")
        #输入详细地址
        get_driver.get_element('smrz','streetname').send_keys('中兴南路309号步步高大厦')
        #输入开业时间
        get_driver.get_element('smrz','opendate').send_keys('2023-07-18')
        #输入经营开始时间
        get_driver.get_element('smrz','optestart').send_keys('2023-07-18')
        #输入经营结束时间
        get_driver.get_element('smrz','opteend').send_keys('2033-07-18')
        # 点击营业执照的上传图片
        get_driver.get_element('smrz', 'yyzzlink').click()
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\20k.jpg")
        sleep(3)
        #输入法人姓名
        frname=get_driver.generate_name()
        get_driver.get_element('smrz','farnname').send_keys(frname)
        #输入法人身份证号
        fridnum=get_driver.generate_id()
        #fridnum = get_driver.generate_id()
        get_driver.get_element('smrz','farnzjno').send_keys(fridnum)
        #输入身份证开始时间
        get_driver.get_element('smrz','credstarttime').send_keys('2023-07-18')
        #输入身份证结束时间
        get_driver.get_element('smrz','credendtime').send_keys('2033-07-18')
        #输入法人手机号
        frtel=get_driver.generate_phone_number()
        get_driver.get_element('smrz','farnshji').send_keys(frtel)
        #输入法人邮箱
        get_driver.get_element('smrz','farndzyx').send_keys(frtel+'@qq.com')
        # 点击法人的身份证正面
        get_driver.get_element('smrz', 'sfzzlink').click()
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\20k.jpg")
        sleep(3)
        # 点击法人的身份证反面
        get_driver.get_element('smrz', 'sfzflink').click()
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\20k.jpg")
        sleep(3)
        # 输入经办人姓名
        jbrname = get_driver.generate_name()
        get_driver.get_element('smrz', 'username').send_keys(jbrname)
        # 输入经办人身份证号
        jbridnum = get_driver.generate_id()
        get_driver.get_element('smrz', 'idnum').send_keys(jbridnum)
        # 输入身份证开始时间
        get_driver.get_element('smrz', 'idstartdate').send_keys('2023-07-18')
        # 输入身份证结束时间
        get_driver.get_element('smrz', 'idenddate').send_keys('2033-07-18')
        # 输入经办人邮箱
        get_driver.get_element('smrz', 'email').send_keys(frtel + '@qq.com')
        # 点击获取验证码
        get_driver.get_element('smrz', 'sendSms').click()
        # 输入验证码
        get_driver.get_element('smrz', 'code').send_keys('999999')
        # 点击下一步
        get_driver.get_element('smrz', 'nextBtn').click()
        # 点击企业基本信息下一步
        get_driver.get_element('smrz', 'qyxxnextbutton').click()
        #点击股东类型，选择类型
        qygm=Select(get_driver.get_element('smrz', 'gdlx'))
        qygm.select_by_visible_text("自然人")
        # 输入股东姓名
        gdname = get_driver.generate_name()
        get_driver.get_element('smrz', 'gdname').send_keys(gdname)
        #点击股东证件类型
        qygm=Select(get_driver.get_element('smrz', 'zjlx'))
        qygm.select_by_visible_text("身份证")
        # 输入股东身份证号
        gdidnum = get_driver.generate_id_number()
        get_driver.get_element('smrz', 'zjnum').send_keys(gdidnum)
        # 输入股东身份证开始时间
        get_driver.get_element('smrz', 'certstart').send_keys('2023-07-18')
        # 输入股东身份证结束时间
        get_driver.get_element('smrz', 'certend').send_keys('2033-07-18')
        # 输入股东持股比例
        get_driver.get_element('smrz', 'cgrate').send_keys('45')
        #选择是否控股股东或实际控制人
        qygm=Select(get_driver.get_element('smrz', 'iscontrol'))
        qygm.select_by_visible_text("是")
        #点击受益人类型，选择类型
        qygm=Select(get_driver.get_element('smrz', 'usertype'))
        qygm.select_by_visible_text("高管")
        # 输入受益人姓名
        syrname = get_driver.generate_name()
        get_driver.get_element('smrz', 'syrname').send_keys(syrname)
        #点击受益人证件类型
        syrgm=Select(get_driver.get_element('smrz', 'certtype'))
        syrgm.select_by_visible_text("身份证")
        # 输入受益人身份证号
        syridnum = get_driver.generate_id_number()
        get_driver.get_element('smrz', 'certno').send_keys(syridnum)
        # 输入受益人身份证开始时间
        get_driver.get_element('smrz', 'syrcertstart').send_keys('2023-07-18')
        # 输入受益人身份证结束时间
        get_driver.get_element('smrz', 'syrcertend').send_keys('2033-07-18')
        # 输入受益人地址
        get_driver.get_element('smrz', 'addr').send_keys('中国（上海）自由贸易试验区纳贤路701号1#楼3层')
        # 点击股东信息下一步
        get_driver.get_element('smrz', 'qyxxnextbutton').click()
        # 点击附件登记表上传附件
        get_driver.get_element('smrz', 'xxdjb').click()
        # 点击信息登记表选择文件按钮
        get_driver.get_element('smrz', 'webuploader-pick').click()
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\20k.jpg")
        # 点击上传附件后的确定按钮
        get_driver.get_element('smrz', 'uploadbutton').click()
        # 点击公司章程选择文件按钮
        get_driver.get_element('smrz', 'gszc').click()
        # 点击公司章程选择文件按钮
        get_driver.get_element('smrz', 'webuploader-pick').click()
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\20k.jpg")
        # 点击上传附件后的确定按钮
        get_driver.get_element('smrz', 'uploadbutton').click()
        # 点击财务报表选择文件按钮
        get_driver.get_element('smrz', 'cwbb').click()
        # 点击财务报表选择文件按钮
        get_driver.get_element('smrz', 'webuploader-pick').click()
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\20k.jpg")
        # 点击上传附件后的确定按钮
        get_driver.get_element('smrz', 'uploadbutton').click()
        # 点击社保名单选择文件按钮
        get_driver.get_element('smrz', 'sbmd').click()
        # 点击社保名单选择文件按钮
        get_driver.get_element('smrz', 'webuploader-pick').click()
        #选择所需要上传的附件
        get_driver.uploadFile("C:\\Users\\Administrator\\Pictures\\20k.jpg")
        # 点击上传附件后的确定按钮
        get_driver.get_element('smrz', 'uploadbutton').click()
        # 点击股东信息下一步
        get_driver.get_element('smrz', 'qyxxnextbutton').click()
        # 输入银行账户
        get_driver.get_element('smrz', 'accid').send_keys('20237311414001')
        #点击开户行
        get_driver.get_element('smrz', 'khh').click()
        get_driver.get_element('smrz', 'khhmc').click()
        #点击开户网点省份
        khsfgm=Select(get_driver.get_element('smrz', 'khwdsf'))
        khsfgm.select_by_visible_text("北京市")
        #点击开户网点市
        khsgm=Select(get_driver.get_element('smrz', 'khwds'))
        khsgm.select_by_visible_text("北京市")
        # 点击选择网点
        get_driver.get_element('smrz', 'khwdfzh').click()
        #输入网点名称
        get_driver.get_element('smrz', 'fkhmc1').send_keys('中国农业银行资金清算中心')
        #点击网点查询
        get_driver.get_element('smrz', 'searchButton').click()
        sleep(3)
        #选择网点
        get_driver.get_element('smrz', 'select').click()
        #点击打款银行卡信息页面下一步
        get_driver.get_element('smrz', 'nextbutton').click()
        #输入打款金额
        get_driver.get_element('smrz', 'amt').send_keys('0.36')
        #点击打款认证页面下一步
        get_driver.get_element('smrz', 'amtnextBtn').click()
        #在提示框页面点击确定
        get_driver.get_element('smrz', 'okbtn').click()
        sleep(5)












if __name__ == "__main__":
        pytest.main()
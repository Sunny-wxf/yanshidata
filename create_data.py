__author__ = 'Wangxiaofeng'
# !/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import random
from logger import Log
from oracle import MyOracle
from getdata import GetData as GetData
import sys


class CreateData(object):

    __logging = Log().get_instance('tw_create_data')

    def __init__(self):
        """
        为测试方法的初始化，每个case运行前执行一次
        :param self.url: 请求域名
        :param self.user_info: 请求参数
        """
        self.url = 'http://192.168.3.186:8090/twweb'
        self.user_info = {'mobile': 14611110000, 'password': 'e10adc3949ba59abbe56e057f20f883e'}
        self.oracle = MyOracle()
        self.name = GetData.get_name()
        self.id = GetData.generator()

    def real_name(self):
        """
        实名认证：读取数据库中未实名认证过的user_id,将user_id匹配随机姓名与身份证号通过接口生成
        :return:null
        """
        self.__logging.debug('-----------------------------------------------------------------')
        url_real_name = self.url + '/RealNameAuthApplicationController_4M/insertRealNameAuthApplication.action'
        user_id = random.sample(self.oracle.select_all('select id from user_info u where u.real_name_id is NULL'),
                                int(sys.argv[1]))
        for i in range(1, int(sys.argv[1])+1):
            name = self.name[i]
            form_register = {
                'name': name,
                'user_id': user_id[i-1][0],
                'face_id': '%2F9j',
                'id_end_time': '2024-06-10',
                'alipay_user_id': '2088022880191155',
                'pt_id_number': self.id[1],
                'open_user': name,
                'bank_id': '-1',
                'open_bank': '-1 ',
                'mobile': '-1 ',
                'my_photo': '%2F9j'
            }
            r = requests.post(url_real_name, data=form_register)
            if r.status_code == 200:
                self.__logging.debug('序号' + str(i) + ':  ' + user_id[i-1][0] + '--' + name + '  实名认证成功')
            else:
                self.__logging.debug('The request error,please check')

    def apply_provincial_agent(self):
        """
        申请代理商
        :return:
        """
        self.__logging.debug('Is it authenticated by real name?')
        url_login = self.url + '/RealNameAuthApplicationController_4M/selectRealNameAuthApplicationRecent.action?'
        user_info1 = self.user_info.copy()
        user_info1['logintype'] = '2'
        r = requests.post(url_login, data=user_info1)
        return r.cookies


if __name__ == '__main__':
    create_data = CreateData()
    create_data.real_name()








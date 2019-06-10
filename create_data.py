__author__ = 'Wangxiaofeng'
#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from urllib import parse
import random
from logger import Log
from oracle import MyOracle
import getdata


class CreateData(object):

    __logging = Log().get_instance('tw_agent')

    def __init__(self):
        """
        为测试方法的初始化，每个case运行前执行一次
        :param self.url: 请求域名
        :param self.user_info: 请求参数
        """
        self.url = 'http://39.105.191.175:8080/twweb'
        self.user_info = {'mobile': 14611110000, 'password': 'e10adc3949ba59abbe56e057f20f883e'}
        self.oracle = MyOracle()
        self.name = getdata.get_name()

    def real_name(self):
        url_real_name = self.url + '/RealNameAuthApplicationController_4M/insertRealNameAuthApplication.action'
        name = self.name
        user_id = random.sample(self.oracle.select_all('select id from user_info u where u.real_name_id is NULL'), 1)
        form_register = {
            'name':'',
            'user_id': user_id[0][0],
            'face_id': '%2F9j',
            'id_end_time': '2024-06-10',
            'alipay_user_id': '',
            'pt_id_number': 110101199003071110,
            'open_user': '',

            'bank_id' = -1,

                      'open_bank' = -1 &

                                  mobile = -1 &

                                           my_photo
        }
        r = requests.post(url_real_name, data=form_register)
        print(r.text)

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
        self.assertIn('登录成功', parse.unquote(parse.unquote(r.text)))
        return r.cookies




if __name__ == '__main__':
    createdata = CreateData()
    createdata.real_name()








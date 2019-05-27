__author__ = 'Wangxiaofeng'
#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import unittest
from urllib import parse
import HTMLTestRunner
from datetime import datetime
import random
from logger import Log


class Agent(object):
    # 增加代理商数据

    __logging = Log().get_instance('tw_agent')

    def setUp(self):
        """
        为测试方法的初始化，每个case运行前执行一次
        :param self.url: 请求域名
        :param self.user_info: 请求参数
        """
        self.url = 'http://39.105.191.175:8080/twweb'
        self.user_info = {'mobile': 14611110000, 'password': 'e10adc3949ba59abbe56e057f20f883e'}

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
    suite = Suite()
    suite.test_report()








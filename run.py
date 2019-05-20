__author__ = 'Wangxiaofeng'
#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from login import Suite as login
from homepage import Suite as homepage
from logger import Log
import HTMLTestRunner
from datetime import datetime


class Suite(unittest.TestSuite):

    __logging = Log().get_instance('tw_run')

    def suite(self):
        '''
        所有测试用例套件
        :return:
        '''
        self.__logging.debug('Integrate all test cases')
        test_case = unittest.TestSuite()
        test_login_suits = login()
        test_homepage_suits = homepage()
        test_case.addTests([test_login_suits.test_login_suite(), test_homepage_suits.home_suite()])
        return test_case


class CreateReport(Suite):
    def test_report(self):
        '''
        生成测试报告
        :return:
        '''
        with open("F:/ScriptReport/report_" + datetime.now().strftime('%Y%m%d-%H-%M') + ".html", 'wb') as report:
            runner = HTMLTestRunner.HTMLTestRunner(stream=report, title='测试报告', description='详情')
            runner.run(self.suite())


if __name__ == '__main__':
    report = CreateReport()
    report.test_report()





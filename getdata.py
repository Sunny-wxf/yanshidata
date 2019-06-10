import requests
import re
from xlwt import Workbook
from conf import Config as Config
import random
# import xlrd
# import time


def get_name():
    # 获取百家姓对应名字集的链接
    url = Config().getconf("name").url_name
    res = requests.get(url)
    reg_last_name = 'href="//[A-Za-z]+\.'
    reg_last_name = re.compile(reg_last_name)
    last_name = re.findall(reg_last_name, res.text)
    last_name_dic = []
    for last_name in last_name:
        url_last_name = 'http:' + last_name[6:len(last_name) - 1] + '.resgain.net/name_list.html'
        last_name_dic.append(url_last_name)
    # 获取百家姓中每个姓氏随机10个名字
    name_dic = []
    for link in last_name_dic:
        res = requests.get(link)
        reg_get_name = '(?<=href="/name/).*?(?=.html" class)'
        reg_name = re.compile(reg_get_name)
        name = re.findall(reg_name, res.text)
        [name_dic.append(x) for x in random.sample(name, 4)]
    print(name_dic)


if __name__ == '__main__':
    get_name()
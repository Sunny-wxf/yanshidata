import requests
import re
from conf import Config as Config
import random
import datetime
import sys
# import threading
from concurrent.futures import ThreadPoolExecutor,Future
import os


class GetData(object):
    # 为生成数据获取各种类型的数据
    def __init__(self):
        self.name_dic = []
        self.exec_counts = 0

    def get_last_name(self):
        """
        姓名
        :return: name_dic
        """
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
        return last_name_dic

    def get_name(self):
        # 获取百家姓中每个姓氏随机8个名字
        res = requests.get(random.sample(self.get_last_name(), 1)[0])
        self.exec_counts += 1
        # print('线程pid: %s: ' % (os.getpid()) + '获取姓氏' + str(self.exec_counts) + '次')
        # print(res)
        reg_get_name = '(?<=href="/name/).*?(?=.html" class)'
        reg_name = re.compile(reg_get_name)
        name = re.findall(reg_name, res.text)
        if len(name) >= 8:
            [self.name_dic.append(x) for x in random.sample(name, 8)]
        else:
            pass
        return self.name_dic
        # print(self.name_dic)

    def parse(self, name_dic):
        print('子线程pid: %s: ' % (os.getpid()) + name_dic.result()[0])

    def get_name_threads(self):
        name_length = sys.argv[1]
        counts = 1
        pool = ThreadPoolExecutor(5)
        for i in range(int(int(name_length)/8)):
            pool.submit(self.get_name).add_done_callback(self.parse)
            # pool.map(self.get_name())
            print("提交" + str(counts) + "次")
            counts += 1
        # print(self.name_dic)

    def generator(self):
        """
        生成随机身份证号
        :return:id_list
        """
        id_list = []
        with open('./area.csv', mode="r", encoding="utf-8") as file:
            codelist = file.readlines()
        num = 1
        while num <= int(sys.argv[1]):
            id_number = codelist[random.randint(0, len(codelist) - 1)].split(" ")[0]  # 地区项
            id_number = id_number + str(random.randint(1980, 2019))  # 年份项
            da = datetime.date.today() + datetime.timedelta(days=random.randint(1, 366))  # 月份和日期项
            id_number = id_number + da.strftime('%m%d')
            id_number = id_number + str(random.randint(100, 300))  # 顺序号简单处理
            i = 0
            count = 0
            weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
            check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5',
                         '8': '5', '9': '3', '10': '2'}  # 校验码映射
            for i in range(0, len(id_number)):
                count = count + int(id_number[i]) * weight[i]
            id_number = id_number + check_code[str(count % 11)]  # 算出校验码
            id_list.append(id_number)
            num += 1
        return id_list


if __name__ == '__main__':
    print('注线程pid: %s: ' % (os.getpid()) )
    get_data = GetData()
    get_data.get_name_threads()
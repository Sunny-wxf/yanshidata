#!/usr/bin/python
# -*- coding:utf-8-sig -*-

import os
import configparser


class Dictionary(dict):
    """
    把config.ini中的参数添加值dict
    """
    def __getattr__(self, keyname):
        # 如果key值不存在则返回默认值"not find config keyname"
        return self.get(keyname, "config.ini中没有找到对应的keyname")


class Config(object):
    """
    ConfigParser二次封装，在字典中获取value
    """

    def __init__(self):
        # 设置conf.ini路径
        current_dir = os.path.dirname(__file__)
        file_name = current_dir + "\\config\\conf.ini"
        # 实例化ConfigParser对象
        self.config = configparser.ConfigParser()
        self.config.read(file_name)
        # 根据section把key、value写入字典
        for section in self.config.sections():
            setattr(self, section, Dictionary())
            for keyname, value in self.config.items(section):
                setattr(getattr(self, section), keyname, value)

    def getconf(self, section):
        """
        用法：
        conf = Config()
        info = conf.getconf("user").user_id
        """
        if section in self.config.sections():
            pass
        else:
            print('config.ini 找不到该 section')
        return getattr(self, section)


if __name__ == '__main__':
    conf = Config()
    info = conf.getconf("user").user_id
    print(info)


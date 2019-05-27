#!/usr/bin/python
# -*- coding:utf-8 -*-

import cx_Oracle
from conf import Config as Config


def ConnectDb():
    # 连接数据库
    db_user = Config().getconf("db").ttw
    # 这里的顺序是用户名 / 密码 @ oracleserver的ip地址 / 数据库名字
    conn = cx_Oracle.connect(db_user)
    # 使用cursor()方法获取操作游标
    get_redis_ares = conn.cursor()
    get_redis_ares.execute("SELECT ra.id,ra.fullname FROM REDIS_AREA ra ")
    redis_ares = get_redis_ares.fetchall()
    get_job_class = conn.cursor()
    get_job_class.execut
    a = len(redis_ares)
    print(a)
    get_redis_ares .close()
    # conn.commit()
    conn.close()


if __name__ == '__main__':
    ConnectDb()

#!/usr/bin/python
# -*- coding:utf-8-sig -*-

import cx_Oracle

conn = cx_Oracle.connect('xzt/xzt@localhost/testdb')#这里的顺序是用户名/密码@oracleserver的ip地址/数据库名字
cur = conn.cursor()
sql = "SELECT * FROM DUAL"
cur.execute(sql)
cur.close()
conn.commit()
conn.close()

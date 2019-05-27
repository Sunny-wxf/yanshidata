# -*- coding:utf-8 -*-

# -*- coding: utf-8 -*-
import cx_Oracle
import datetime
from conf import Config as Config


class MyOracle(object):

    SHOW_SQL = True

    def __init__(self):
        # 得到配置的数据库信息
        self.db_user = Config().getconf("db").ttw

    def get_con(self):
        try:
            conn = cx_Oracle.connect(self.db_user)
            return conn
        except cx_Oracle.Error as e:
            print("cx_Oracle Error:%s" % e)

    def select_all(self, sql):
        con = self.get_con()
        # print con
        # 使用cursor()方法获取操作游标
        cur = con.cursor()
        try:
            cur.execute(sql)
            fc = cur.fetchall()
            return fc
        except cx_Oracle.Error as e:
            print("cx_Oracle Error:%s" % e)
        finally:
            cur.close()
            con.close()

    def select_by_where(self, sql, data):
        con = self.get_con()
        cur = con.cursor()
        try:
            s=str()
            d = data
            cur.execute(sql, d)
            fc = cur.fetchall()
            # if len(fc) > 0:
            #     for e in range(len(fc)):
            #         print(fc[e])
            return fc
        except cx_Oracle.Error as e:
            print("cx_Oracle Error:%s" % e)
        finally:
            cur.close()
            con.close()

    def dml_by_where(self, sql, params):
        con = self.get_con()
        cur = con.cursor()
        try:
            for d in params:
                if self.SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cur.execute(sql, d)
            con.commit()
        except cx_Oracle.Error as e:
            con.rollback()
            print("cx_Oracle Error:%s" % e)
        finally:
            cur.close()
            con.close()

    # 不带参数的更新方法
    def dml_nowhere(self, sql):
        con = self.get_con()
        cur = con.cursor()
        try:
            count = cur.execute(sql)
            con.commit()
            return count
        except cx_Oracle.Error as e:
            con.rollback()
            print("cx_Oracle Error:%s" % e)
        finally:
            cur.close()
            con.close()

# 开始测试函数


def select_all():
    sql = "select * from use_info"
    fc = my_oracle.select_all(sql)
    for row in fc:
        print(row)


def select_by_where():
    sql = "select * from user_info where id=d[:1]"
    data = ['42542bcee55f437e9d28917ba36d206e', '25f4432083f44c57a9aebbccd0bf5b02']
    fc = my_oracle.select_by_where(sql, data)
    for row in fc:
        print(row)

'''
def ins_by_param():
    sql = "insert into dave(USERNAME,USER_ID,CREATED) values(:1,:2,:3)"
    date = datetime.datetime.now()
    data = [('http://www.cndba.cn', 0551, date), ('http://www.cndba.cn/dave', 0556, date)]
    my_oracle.dml_by_where(sql, data)


def del_by_where():
    sql = "delete from dave where USERNAME = :1 and USER_ID=:2"
    data = [('HR', 107)]
    my_oracle.dml_by_where(sql, data)


def update_by_where():
    sql = "update dave set USER_ID=:1 where USER_ID=:2"
    data = [(0551, 0556)]
    my_oracle.dml_by_where(sql, data)


def del_nowhere():
    sql = "delete from dave"
    print(my_oracle.dml_nowhere(sql))
'''

if __name__ == "__main__":
    my_oracle = MyOracle()
    # del_nowhere()
    select_by_where()



# -*- coding:utf-8 -*-

# -*- coding: utf-8 -*-
import cx_Oracle
import datetime
from conf import Config as Config

class MyOracle(object):

    SHOW_SQL = True

    def __init__(self):
        # 得到配置的数据库信息
        self.__db_user = Config().getconf("db").ttw
        try:
            self.__conn = cx_Oracle.connect(self.__db_user)
            self.__cur = self.__conn.cursor()
        except cx_Oracle.Error as e:
            print("cx_Oracle Error:%s" % e)

    def get_con(self):
        try:
            conn = cx_Oracle.connect(self.__db_user)
            return conn
        except cx_Oracle.Error as e:
            print("cx_Oracle Error:%s" % e)

    def select_all(self, sql):
        try:
            self.__cur.execute(sql)
            fc = self.__cur.fetchall()
            return fc
        except cx_Oracle.Error as e:
            print("cx_Oracle Error:%s" % e)
        finally:
            self.__cur.close()
            self.__conn.close()

    def select_by_where(self, sql, data):
        data_dic = {}
        for i in range(len(data)):
            data_dic[str(i+1)] = data[i]
        try:
            self.__cur.execute(sql, data_dic)
            fc = self.__cur.fetchall()
            # if len(fc) > 0:
            #     for e in range(len(fc)):
            #         print(fc[e])
            return fc
        except cx_Oracle.Error as e:
            print("cx_Oracle Error:%s" % e)
        finally:
            self.__cur.close()
            self.__conn.close()

    def dml_by_where(self, sql, params):
        try:
            for d in params:
                if self.SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                self.__cur.execute(sql, d)
            self.__cur.commit()
        except cx_Oracle.Error as e:
            self.__cur.rollback()
            print("cx_Oracle Error:%s" % e)
        finally:
            self.__cur.close()
            self.__conn.close()

    # 不带参数的更新方法
    def dml_nowhere(self, sql):
        try:
            count = self.__cur.execute(sql)
            self.__cur.commit()
            return count
        except cx_Oracle.Error as e:
            self.__cur.rollback()
            print("cx_Oracle Error:%s" % e)
        finally:
            self.__cur.close()
            self.__conn.close()

# 开始测试函数


def select_all():
    sql = "select * from use_info"
    fc = my_oracle.select_all(sql)
    print(fc)
    # for row in fc:
    #     print(row)


def select_by_where():
    sql = "select * from user_info where id =:1"
    data = ['42542bcee55f437e9d28917ba36d206e']
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



# -*- coding:utf-8 -*-

# -*- coding: utf-8 -*-
import cx_Oracle
# import datetime
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
            return fc
        except cx_Oracle.Error as e:
            print("cx_Oracle Error:%s" % e)
        finally:
            self.__cur.close()
            self.__conn.close()

    def dml_by_where(self, sql, params):
        params_dic = {}
        for i in range(len(params)):
            params_dic[str(i+1)] = params[i]
        try:
            if self.SHOW_SQL:
                print('执行sql:[{}],参数:[{}]'.format(sql, params_dic))
            self.__cur.execute(sql, params_dic)
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

if __name__ == "__main__":
    my_oracle = MyOracle()
    my_oracle.dml_nowhere('select * from user_info')


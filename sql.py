#!/usr/local/bin/env python3
#-*- coding=utf-8 -*-

import configparser
import pymysql

class mysql:
    """A class for connection to mysql and operation"""
    def __init__(self):
        self.setting_file = ""

    def __connect(setting_file, session="DEFAULT"):
        config = configparser.ConfigParser()
        config.read("sql.ini")
        #config.read(setting_file)
        default = config["DEFAULT"]
        try:
            con = pymysql.connect(host=default['server'],
                    user=default['user'],
                    passwd=default['passwd'],
                    db=default['db'],
                    charset='utf8')
            return con
        except pymysql.err.OperationalError as e:
            print(e)

    def insert_log(self, user_name, logtype, content):
        """insert the log into the mysql"""
        con = self.__connect("sql.ini")
        cur = con.cursor()
        cur.execute("INSERT INTO irclog (user, type, content) VALUES (%s, %s, %s)", 
                (user_name, logtype, content))
        cur.connection.commit()
        cur.close()
        con.close()

    def select_log(self, log_id, colume=None):
        result = None
        con = self.__connect("sql.ini")
        cur = con.cursor()
        if colume == None:
            cur.execute("SELECT * FROM irclog WHERE id=%s", log_id)
        else:
            cur.execute("SELECT %s FROM irclog WHERE id=%s", (colume, log_id))
        result = cur.fetchone()
        cur.close()
        con.close()
        return result

    def select_all(self):
        result = None
        con = self.__connect("sql.ini")
        cur = con.cursor()
        cur.execute("SELECT * FROM irclog")
        result = cur.fetchall()
        cur.close()
        con.close()
        return result

if __name__ == "__main__":
    sql = mysql()
    sql.insert_log("test", "test", "test from sql.py")
    for row in sql.select_all():
        print(row)


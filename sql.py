#!/usr/local/bin/env python3
#-*- coding=utf-8 -*-

import configparser
import pymysql

class mysql:
    """A class for connection to mysql and operation"""
    def __init__(self, setting_file):
        self.setting_file = ""

    def __connect(setting_file, session="default"):
        config = configparser.ConfigParser()
        config.read(setting_file)
        default = config[session]
        try:
            conn = pymysql.connect(host=default['server'],
                    user=default['user'],
                    passwd=default['passwd'],
                    db=default['db'])
            return conn
        except pymysql.err.OperationalError as e:
            print(e)

    def insert_log(self, user_name, logtype, content):
        """insert the log into the mysql"""
        con_obj = __connect("sql.ini")
        cur = con_obj.cursor()
        cur.execute("INSERT INTO irclog (user_name, logtype, content) VALUES (%s, %s, %s)"
                % (user_name, logtype, content))
        cur.close()
        con_obj.close()

    def select_log(self, log_id, colume=None):
        result = None
        con_obj = __connect("sql.ini")
        cur = con_obj.cursor()
        if colume == None:
            cur.execute("SELECT * FROM irclog WHERE id=&s" % log_id)
        else:
            cur.execute("SELECT %s FROM irclog WHERE id=%s" % (colume, log_id))
        result = cur.fetchone()
        cur.close()
        con_obj.close()
        return result


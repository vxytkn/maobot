#!/usr/local/bin/env python3
#-*- coding = utf-8 -*-

import irc
import sql
import user

i = irc.irc()
s = sql.sql()

i.irc_conn()
i.login()
i.join()

while(1):
    buffer = i.IRC.recv(1024).decode("iso-2022-jp")
    msg = buffer.split()
    if len(msg) >= 4 and msg[1] == "PRIVMSG":
        u_info = msg[0]
        l_msg = ""
        spker = user.user()
        spker.l_name = u_info[1:u_info.find("!")
        spker.n_name = u_info[(u_info.find("!")+2):u_info.find("@")]
        l_msg = " ".join(msg[3:])
        with s:
            if s.find(l_name):
                s.insert_log("MaO", "PRIVMSG", msg[3][1:])

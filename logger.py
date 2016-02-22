#!/usr/local/bin/env python3
#-*- coding = utf-8 -*-

import irc
import sql

i = irc.irc()
s = sql.mysql()

i.irc_conn()
i.login()
i.join()

while(1):
    buffer = i.IRC.recv(1024).decode("iso-2022-jp")
    msg = buffer.split()
    if len(msg) >= 4 and msg[1] == "PRIVMSG" and "MaO" in msg[0]:
        s.insert_log("MaO", "PRIVMSG", msg[3][1:])


#!/usr/local/bin/env python3
#-*- coding = utf-8 -*-

from checker import check
import irc
import sql
import user

i = irc.irc()
s = sql.sql()

with s:
    i.irc_conn()
    i.login()
    for ch in s.show_channels():
        i.add_channel(ch[1])
    i.join_all()

while(1):
    try:
        buffer = i.IRC.recv(1024).decode("iso-2022-jp")
    except UnicodeDecodeError as e:
        buffer = "ERROR: UnicodeDecodeError"
    msg = buffer.split()
    print(msg)
    #PING PONG
    if msg[0] == "PING":
        i.send_data("PONG %s" % msg[1])
    if len(msg) >= 4 and msg[1] == "PRIVMSG":
        check(buffer, msg, i, s)
        """
        u_info = msg[0]
        i_msg = buffer[buffer.find(buffer.split()[3])+1:]
        spker = user.user()
        spker.l_name = u_info[1:u_info.find("!")]
        spker.n_name = u_info[(u_info.find("!")+2):u_info.find("@")]
        if "[enter]#" in buffer:
            j_ch = buffer[buffer.find("[enter]")+7:]
            i.join(j_ch)
            with s:
                s.insert_channel(j_ch)
        with s:
            s.insert_channel(msg[2])
            s.insert_log(spker.l_name, msg[1], msg[2], i_msg[1:])
        """

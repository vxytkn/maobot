#!/usr/local/bin/env python3
#-*- coding=utf-8 -*-

import socket, string
from urllib.request import urlopen
import sql

class irc():
    def __init__(self):
        self.server = "irc.ircnet.ne.jp"
        self.port = 6667
        self.nickname = "maobot_test"
        self.channel = "#maobot_test"

    IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def irc_conn(self):
        self.IRC.connect((self.server, self.port))

    def send_data(self, command):
        self.IRC.send(command.encode("ISO-2022-JP") + b'\n')

    def join(self):
        self.send_data("JOIN %s" % self.channel)

    def login(self, nickname="maobot_test", username="maobot_test", password=None,
            realname="maobot_test", hostname="IRCnet", servername="IRCnet"):
        self.send_data("USER %s %s %s %s" % (username, hostname, servername, realname))
        self.send_data("NICK " + nickname)

    def send_msg(msg):
        send_data("PRIVMSG %s %s" % (self.channel, msg))

    def test(self):
        self.irc_conn()
        self.login()
        self.join()

        while(1):
            buffer = self.IRC.recv(1024).decode("iso-2022-jp")
            msg = buffer.split()
            print(msg)
            if msg[0] == "PING":
                print("hai")
                self.send_data("PONG %s" % msg[1])
            if (len(msg) >= 3 and msg[3] == ":PING"):
                self.send_data("PRIVMSG %s PONG" % self.channel)
            if (len(msg) >= 3 and "ガルパン" in msg[3]):
                self.send_msg("ガルパンはいいぞ")

if __name__ == '__main__':
    i = irc()
    i.test()

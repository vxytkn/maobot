#!/usr/local/bin/env python3
#-*- coding=utf-8 -*-

import socket, string

class irc():
    """connection with IREnet(irc.ircnet.ne.jp)"""
    def __init__(self):
        self.server = "irc.ircnet.ne.jp"
        self.port = 6667
        self.nickname = "maobot_test"
        self._channel = []

    IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def irc_conn(self):
        self.IRC.connect((self.server, self.port))

    def send_data(self, command):
        self.IRC.send(command.encode("ISO-2022-JP") + b'\n')

    def add_channel(self, channel):
        self._channel.append(channel)

    def join(self, channel):
        self.__send_data("JOIN %s" % channel)
    
    def join_all(self):
        for ch in self._channel:
            self.join(ch)

    def login(self, username="maobot_test", password=None, realname="maobot_test", 
            hostname="IRCnet", servername="IRCnet"):
        self.__send_data("USER %s %s %s %s" % (username, hostname, servername, realname))
        self.__send_data("NICK " + self.nickname)

    def send_msg(self, msg):
        self.send_data("PRIVMSG %s %s" % (self.channel, msg))

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
            if (len(msg) >= 4 and msg[3] == ":PING"):
                self.send_msg("PONG")
            if (len(msg) >= 4 and msg[1] == "PRIVMSG"):
                self.send_msg("ガルパンはいいぞ")

if __name__ == '__main__':
    i = irc()
    i.test()

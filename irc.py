#!/usr/local/bin/env python3
#-*- coding=utf-8 -*-

import socket, string
from urllib.request import urlopen
import sql

SERVER = "irc.ircnet.ne.jp"
PORT = 6667
NICKNAME = "maobot_test"
CHANNEL = "#maobot_test"

IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def irc_conn():
    IRC.connect((SERVER, PORT))

def send_data(command):
    IRC.send(command.encode("ISO-2022-JP") + b'\n')

def join(channel):
    send_data("JOIN %s" % channel)

def login(nickname, username="maobot_test", password=None,
        realname="maobot_test", hostname="IRCnet", servername="IRCnet"):
    send_data("USER %s %s %s %s" % (username, hostname, servername, realname))
    send_data("NICK " + nickname)

def send_msg(msg):
    send_data("PRIVMSG %s %s" % (CHANNEL, msg))

irc_conn()
login(NICKNAME)
join(CHANNEL)

while(1):
    buffer = IRC.recv(1024).decode("iso-2022-jp")
    msg = buffer.split()
    print(msg)
    if msg[0] == "PING":
        print("hai")
        send_data("PONG %s" % msg[1])
    if (len(msg) >= 3 and msg[3] == ":PING"):
        send_data("PRIVMSG %s PONG" % CHANNEL)
    if (len(msg) >= 3 and "ガルパン" in msg[3]):
        send_msg("ガルパンはいいぞ") 

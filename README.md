# maobot
an irc bot for KGB

## TODO
IRCLogger
IMAGEDownloader
VIDEODownloader

## DATABASE
###user

  id INT(5) NOT NULL AUTO_INCREMENT
  
  username VARCHAR(20)
  
  l_name VARCHAR(20)                      -> loginname for IRC
  
  n_name VARCHAR(20)                      -> nickname for IRC
  
  password VARCHAR(100)
  
###channel

  id INT(5) NOT NULL AUTO_INCREMENt
  
  name VARCHAR(20)
  
  topic VARCHAR(100)
  
  usernum INT(3)

###irclog
  
  id BIGINT(7) NOT NULL AUTO_INCREMENT
  
  user VARCHAR(20)
  
  type VARCHAR(8)
  
  channel VARCHAR(20)
  
  content VARCHAR(10000)
  
  created TIMESTAMP NOT NULL CURRENT_TIMESTAMP

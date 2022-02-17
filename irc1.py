import socket
import time
import string
import math

server = 'irc.root-me.org'
port = 6667 
botname = 'opertune'
channel = '#root-me_challenge'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    time.sleep(3)
    s.send(bytes('USER ' + botname + ' ' + botname + ' ' + botname +' :Python IRC\r\n', 'UTF-8'))
    time.sleep(3)
    s.send(bytes('NICK ' + botname + '\r\n', 'UTF-8'))
    time.sleep(3)
    s.send(bytes('JOIN ' + channel + '\r\n', 'UTF-8'))
    time.sleep(3)

    while True:
        data = s.recv(16000).decode('UTF-8')
        print(data)
        if 'PING' in data:
            s.send(bytes("PONG " + data.split()[1] + "\n", 'UTF-8'))
            s.send(bytes('PRIVMSG Candy :!ep1\r\n', 'UTF-8'))
        if 'PRIVMSG' in data:
            msg = data.split('PRIVMSG')
            msg2 = msg[1].split(':')
            msg3 = msg2[1].split('/')
            nb1 = msg3[0]
            nb2 = msg3[1].split('\r')[0]
            val1 = math.sqrt(int(nb1)) * int(nb2)
            val2 = round(val1, 2)
            s.send(bytes('PRIVMSG Candy :!ep1 -rep '+str(val2)+'\r\n', 'UTF-8'))
            print('msg send, val: '+str(val2))
            break
    s.close()
except socket.error as err:
    print(err)
    print('conn close')
    s.close()


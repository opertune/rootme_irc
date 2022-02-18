import socket
import time
import zlib
import base64

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
            s.send(bytes('PRIVMSG Candy :!ep4\r\n', 'UTF-8'))
        if 'PRIVMSG' in data:
            msg = data.split('PRIVMSG')
            msg2 = msg[1].split(':')[1]
            msg2 = base64.b64decode(msg2)
            decompressed_data = zlib.decompress(msg2)
            # print(decompressed_data.decode('utf-8'))
            s.send(bytes('PRIVMSG Candy :!ep4 -rep '+decompressed_data.decode('utf-8')+'\r\n', 'UTF-8'))
            # break
    s.close()
except socket.error as err:
    print(err)
    print('conn close')
    s.close()


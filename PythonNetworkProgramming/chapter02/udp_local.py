# -*- coding: utf-8 -*-
# @Author: zxy987872674
# @Date:   2018-08-19 22:54:26
# @Last Modified by:   zxy987872674
# @Last Modified time: 2018-08-19 23:56:23
# 使用自环接口的UDP服务器和客户端
# udp client and server on localhost

import argparse
import socket
from datetime import datetime

MAX_BYTES = 65535


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is {} '.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parse = argparse.ArgumentParser(description='Send and receive UDP locally')
    parse.add_argument('-p', metavar='PORT', type=int, default=1061, help='UDP port (default 1060)')
    args = parse.parse_args()
    function = choices[args.role]
    function(args.p)

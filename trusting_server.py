from socket import *
import _thread
import time
import json

def handler(client_sock, addr):
    f = open("data.txt", "a+")
    time.sleep(2)
    data = client_sock.recv(65535)
    g = str(data.decode()).split("\r\n\r\n")[1]
    object = json.loads(g)
#    print(object['key1'], object['key2'], object['key3'])
    output = json.dumps(object)
    f.write("\n{}".format(output))
    client_sock.close()


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 5555
    ADDR = (HOST, PORT)

    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind(ADDR)
    server_sock.listen(5)

    while 1:
        print('waiting for connection...')
        client_sock, addr = server_sock.accept()
        print('...connected from: ', addr)
        _thread.start_new_thread(handler, (client_sock, addr))

import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock,s_addr):
    s_sock.send(str.encode('Welcome to the Server\n'))
    while True:
        data = str(s_sock.recv(2048).decode())
        choice,val = data.split('.')
        if choice == "1":
            print(str(s_addr) + " did logarithm")
            answer = str(math.log(int(val)))
            s_sock.send(str.encode(answer))
        elif choice == "2":
            print(str(s_addr) + " did square root")
            answer = str(math.sqrt(int(val))) 
            s_sock.send(str.encode(answer))
        elif choice == "3":
            print(str(s_addr) + " did exponential function")
            answer = str(math.exp(int(val)))
            s_sock.send(str.encode(answer))
        elif choice == "0":
            s_sock.close()
             
    s_sock.close()
        

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,s_addr))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:        
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	s.close()
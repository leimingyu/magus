#!/usr/bin/env python
import socket
import time
import sys


def main(argv):

    msg_to_pass   = argv[0]
    time_to_sleep = float(argv[1])

    # wait for starting
    time.sleep(time_to_sleep)

    # start connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 9000))

    print time.time()

    data = str(msg_to_pass) 
    print "send : ", data
    sock.sendall(data)

    #result = sock.recv(1024)
    #print result

    #
    # finish all the client work
    #
    sock.close()




if __name__ == "__main__":
    main(sys.argv[1:])

""" This is only placeholder code for the real deal, which is yet to be made, will be changed shortly"""

import DisorderCategories
import socket

HOST = '127.0.0.1'
PORT = 55555


def recvdataclient():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketinstance:
        socketinstance.connect((HOST, PORT))
        data = socketinstance.recv(2048)
        print("Data received from server is : ", data)
        return data


def senddataclient():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketinstance:
        socketinstance.connect((HOST, PORT))
        # Send required input here
        socketinstance.sendall(b'Hello, world')




def main():
    print("This is the main interface for communication with the AI")
    while True:
        getdata()

def getdata():
    senddataclient()
    serverdata = recvdataclient()
    while serverdata == None:
        serverdata = recvdataclient()

if __name__ == "__main__":
    main()
""" This is only placeholder code for the real deal, which is yet to be made, will be changed shortly"""

import DisorderCategories
import socket

HOST = '127.0.0.1'
PORT = 55555

# String consisting of previous statement from client
client_answer = ""

def recvdataserver():
    global client_answer, HOST, PORT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketinstance:
        socketinstance.bind((HOST, PORT))
        socketinstance.listen()
        connection, address = socketinstance.accept()
        with connection:
            print("Connected by : ", address)
            while True:
                data = connection.recv(2048)
                client_answer = data
                return client_answer
                if not data:
                    break



def senddataserver():
    global client_answer, HOST, PORT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketinstance:
        socketinstance.bind((HOST, PORT))
        connection, address = socketinstance.accept()
        with connection:
            # Send a single line of data to client, from AI ( should be from some rule through prev input)
            if client_answer != "":
                data = input("This is the query")
            else:
                data = "Hello, happy to be of service, I am glad you are here. I might have som questions for you."
                connection.sendall(data)


def main():
    print("This is the server : ")
    senddataserver()
    recvdataserver()
    while client_answer == "":
        recvdataserver()


if __name__ == "__main__":
    main()
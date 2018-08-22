#coding:utf-8

from socket import *

serverPort = 12000
server = '127.0.0.1'

while True:

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server, serverPort))

    comando = raw_input("")
    if comando != "sair":
        clientSocket.send(comando.encode('utf-8'))

        recebeComando = clientSocket.recv(1024).decode('utf-8')

        print (recebeComando)
    else:
        print "Encerrando conexão"
        

clientSocket.close()

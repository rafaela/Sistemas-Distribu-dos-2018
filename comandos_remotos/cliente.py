#coding:utf-8

import socket
import subprocess

serverPort = 12001
server = '127.0.0.1'

while True:
	comando = raw_input("")
	if comando == "sair":
		print "Encerrando conexão"
		break
	else:
		try:
			clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			clientSocket.connect((server, serverPort))
		    
			clientSocket.send(comando.encode('utf-8'))

			tamanhoEsperado = int(clientSocket.recv(10).decode('utf-8'))
			print ('Tamanho: ', tamanhoEsperado)
			tamanhoLido = 0
			resposta = ""
			while tamanhoLido < tamanhoEsperado:
				r = clientSocket.recv(1024).decode('utf-8')
				resposta += r
				tamanhoLido += len(r)
			
			#print (resposta)
			clientSocket.close()
		except socket.error:
			saida = subprocess.check_output(comando, shell = True)
			print('LOCAL', saida)
		    


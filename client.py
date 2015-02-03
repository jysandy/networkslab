import socket

server = '127.0.0.1'
port = 8000

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((server, port))
	s.sendall('so mimsy were ye borogroves')
	reply = s.recv(4096)
	s.shutdown(socket.SHUT_RDWR)
	print reply
	s.close()
except socket.error, msg:
	print str(msg[0])
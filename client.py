import socket

server = '127.0.0.1'
port = 8000

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((server, port))
	s.sendall(raw_input('Enter a sentence:'))
	reply = s.recv(4096)
	s.shutdown(socket.SHUT_RDWR)
	print 'Received response:\n' + reply
	s.close()
except socket.error, msg:
	print str(msg[0])

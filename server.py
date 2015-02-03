import socket

host = ''
port = 8000

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(10)
	while True:
		conn, addr = s.accept()
		data = conn.recv(4096)
		conn.sendall(data.upper())
	conn.close()
	s.close()
except socket.error, msg:
	print str(msg[0])
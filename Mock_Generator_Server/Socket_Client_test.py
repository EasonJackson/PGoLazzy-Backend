import socket


SERVER_HOST = ''
SERVER_PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_HOST, SERVER_PORT))
s.send('42.2746,-71.8063,41.2710,-70.8093')
s.close()
import socket, time

host = '192.168.0.102'
port = 9999
buf_size = 1024
address = (host, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
while True:
    data = raw_input("Your command:").strip()
    if not data or data == 'exit':
        break
    client.sendall('%s\r\n' % data)
    data = client.recv(buf_size)
    if not data:
        print ""
    print data.strip()
client.close()

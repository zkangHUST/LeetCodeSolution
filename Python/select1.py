import select
import socket
import time
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口
s.listen(5)                 # 监听，等待客户端连接
s.setblocking(False)
inputs = [s]
outputs = []

while inputs:
    print ('waiting for the next event')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for v in readable:
        if v is s:
            connection, client_addr = v.accept()
            print ('connection from', client_addr)
            connection.setblocking(0)
            inputs.append(connection)
        else :
            data = v.recv(1024)
            data = str(data,'utf-8')
            print(data)
            if data == '88':
                inputs.remove(v)
                v.close()

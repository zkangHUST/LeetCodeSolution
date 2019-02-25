import socket               # 导入 socket 模块
import time    
import errno
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口
s.listen(5)                 # 等待客户端连接
c, addr = s.accept()        # 建立客户端连接。
c.setblocking(False)
print("connected from :%s:%s"%(addr[0],addr[1]))
while True:
    print("wating for client input")
    try:
        data = c.recv(1024)
    except socket.error as e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            time.sleep(1)
            print("no data available")
            continue
        else:
            print(e)
            c.close()
            break
    else:
        data = str(data,'utf-8')
        print(data)
        if data == '88':
            c.close()
            break
print("client closed connection")
s.close()
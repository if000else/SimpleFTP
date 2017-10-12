import socket
from conf import settings
p_port = ('127.0.0.1',8888)
sk = socket.socket()
sk.bind(p_port)
sk.listen(5)  # 最大等待人数
sk.settimeout(60)
while True:
    conn,address =  sk.accept()
    conn.sendall('1'.encode())#test connect
    Flag = True
    while Flag:
        data = conn.recv(1024).decode()
        if not data:
            continue
        elif data.startswith('upload'):#received request
            in_data = conn.recv(4096).decode()#receive data
            lis = data.split(" ")
            path = "%s/%s"%(settings.F_SERVER,lis[1])#filename
            f=open(path,'w')
            f.write(in_data)
            f.close()
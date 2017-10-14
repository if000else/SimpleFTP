import socket,os,sys
from pathlib import Path
BASEDIR = Path(__file__).parent.parent
sys.path.append(str(BASEDIR))
from conf import settings
from modules import log


ip_port = (settings.ADDR, settings.PORT)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(settings.MAXCONN)  # 最大等待人数
sk.settimeout(settings.TMOUT)
while True:
    conn,address = sk.accept()
    log.logger("server").info("Client [%s] connected ." % conn)
    conn.sendall('Service is on!.'.encode())#test connect
    Flag = True
    while Flag:
        command = conn.recv(settings.MAXSIZE).decode()
        print("recv command:",command)
        if command=='upload':#received request
            filename = conn.recv(settings.MAXSIZE).decode()  # receive filename
            print("filename:",filename)
            data = conn.recv(settings.MAXSIZE).decode()#receive data
            with open("%s/%s"%(settings.F_SERVER,filename),'w') as f:
                f.write(data)
                log.logger("server").info("Recv data from [%s] ." % conn)
        elif command=='download':#received request
            filename = conn.recv(settings.MAXSIZE).decode()  # receive filename
            print("filename:", filename)
            with open("%s/%s"%(settings.F_SERVER,filename)) as f:
                data = f.read()
                conn.sendall(data.encode())
                log.logger("server").info("Send data to [%s] ." % conn)
        elif command == "quit":
            log.logger("server").info("Client [%s] disconnected! ." % conn)
            Flag = False
        else:
            conn.sendall("unsupported command!".encode())
            log.logger("server").info("command formate error")


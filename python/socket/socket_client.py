import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 1234))
    while True:
        msg = input("Enter message (type 'exit' to quit): ")
        if msg.lower() == 'exit': # 将字符串换为小写
            break
        s.sendall(msg.encode()) # 发送消息给服务器
        data = s.recv(1024)
        print("收到了：", repr(data.decode()))
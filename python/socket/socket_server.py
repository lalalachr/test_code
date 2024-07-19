import socket
import threading

# 这种写法只能接受一个客户端的请求
# 创建socket AF_INET代表IPv4  SOCK_STREAM代表TCP协议
# with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
#     s.bind(("0.0.0.0",1234))    # 关联到网址和端口
#     s.listen()                  # 监听
#     c, addr = s.accept()        # 返回新的socket c 和 一个地址
#     with c:
#         print(addr, "connected.")
#         while True:
#             data = c.recv(1024)
#             if not data:
#                 break
#             c.sendall(data)
#             if data.decode().strip() == "exit":
#                 c.close()

# 采用多线程实现多个接收多个客户端的请求
def handle_client(c, addr):
    print(addr, "connected.")
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.sendall(data)


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 1234))
    s.listen()

    while True:
        c, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(c, addr))
        t.start()

if __name__ == '__main__':
   start_server()







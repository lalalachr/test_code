import socket
import threading
import os
from urllib.parse import unquote

WEBROOT = r"D:\ZE\induction plan\code\python\socket"

def handle_client(c, addr):
    print(addr, "connected.")
    with c:
        request = c.recv(1024)
        headers = request.split(b"\r\n")

        if len(headers) > 0:
            path = headers[0].split()[1].decode('utf-8')
            path = unquote(path) # 解码 URL 编码

        if path == "/weiking":
            path = "/weiking/"
        
        # 如果路径以斜杠结尾，追加默认文件名
        if path.endswith("/"):
            path += "index.html"

        print(path)

        file_path = os.path.join(WEBROOT, path[1:] if path.startswith("/") else path)

        try:
            with open(file_path, "rb") as f:
                content = f.read()
            response = b"HTTP/1.0 200 OK\r\n\r\n" + content
        
        except FileNotFoundError:
            response = b"HTTP/1.0 404 NOT FOUND\r\n\r\nFile not found!"
        
        c.sendall(response)

def start_http_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 80))
    s.listen()
    while True:
        c, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(c, addr))
        t.start()



if __name__ == '__main__':
   start_http_server()

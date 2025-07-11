"""
演示socket开发
"""

# 导入socket模块
import socket
from socketserver import BaseRequestHandler

# 创建socket对象
socket_server = socket.socket()

# 绑定端口
socket_server.bind(("localhost", 8888))

# 监听端口, listen表示接受的连接数量
socket_server.listen(1)
print(f"服务端已成功运行，正在等待链接")

# 等待客户端连接 accept返回的是连接对象和客户端地址信息
result:tuple = socket_server.accept()
conn = result[0]
address = result[1]
# 也可写成conn, address = socket_server()
# accept是阻塞的方法，如果没有客户端连接，那么代码暂停在这里
print(f"客户端已连接，地址{address}")

while True:
    # 接受客户端信息，使用客户端和服务端本次链接对象，而非socket-server对象
    data:str = conn.recv(1024).decode('utf-8')
    if data == 'exit':
        break
    # recv接受的是缓冲区的大小，一般给1024即可
    # recv返回的是bytes，可以通过decode转化utf-8
    print(f"客户端发来的消息是：{data}")
    # 发送回复消息
    msg = input("你要发送的消息").encode('utf-8')
    conn.send(msg)

# 关闭连接
conn.close()
# 关闭客户端
socket_server.close()

import socketserver
class MYHandler(socketserver.BaseRequestHandler):
    def handler(self):
        msg = self.request.recv(1024).decode('utf-8')
        data = ''
        self.request.send(data).encode('utf-8')
        self.request.close()




















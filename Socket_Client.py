import socket

socket_client = socket.socket()

socket_client.connect(("localhost", 8888))

while True:
    msg = input("请输入你要发送的信息：")
    socket_client.send(msg.encode('utf-8'))
    if msg == 'exit':
        break
    data = socket_client.recv(1024).decode()
    print(f"服务端回复的消息是：{data}")

socket_client.close()
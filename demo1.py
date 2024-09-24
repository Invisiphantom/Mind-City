import socket


def tcp_client():
    # 创建 TCP 套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    server_address = ("localhost", 12345)
    client_socket.connect(server_address)

    try:
        while True:
            # 输入小写消息
            message = input("请输入小写字母消息（输入 'exit' 退出）: ")
            if message.lower() == "exit":
                break

            # 发送消息
            client_socket.sendall(message.encode())

            # 接收响应
            data = client_socket.recv(1024)
            print(f"接收到来自服务器的响应: {data.decode()}")

    finally:
        client_socket.close()


if __name__ == "__main__":
    tcp_client()

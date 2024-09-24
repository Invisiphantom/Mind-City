import socket


def tcp_server():
    # 创建 TCP 套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址和端口
    server_address = ("localhost", 12345)
    server_socket.bind(server_address)

    # 开始监听
    server_socket.listen(1)
    print("TCP 服务器正在运行，等待连接...")

    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        print(f"已连接到 {client_address}")

        try:
            while True:
                # 接收数据
                data = client_socket.recv(1024)
                if not data:
                    break  # 如果没有数据，退出循环

                message = data.decode()
                print(f"接收到消息: {message}")

                # 转换为大写并发送响应
                response = message.upper()
                client_socket.sendall(response.encode())

        finally:
            client_socket.close()
            print(f"已断开与 {client_address} 的连接")


if __name__ == "__main__":
    tcp_server()

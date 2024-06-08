import socket

def main():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)
    
    try:
        message = input("Enter message to send: ")
        while message.lower().strip() != 'quit':
            client_socket.sendto(message.encode(), server_address)
            data = client_socket.recvfrom(1024)
            print(f"Отримано відповідь від сервера: {data.decode()}")
    except:
        client_socket.close()

if __name__ == '__main__':
    main()
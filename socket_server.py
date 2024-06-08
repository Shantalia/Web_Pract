import socket

def main():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f'Connection from...')
    while True:
        data, address = server_socket.recvfrom(1024)
        if not data:
            print(f"З'єднання з {address} завершено.")
            break
        print(f'Received message {address}: {data.decode()}')
        message = input('>>> ')
        server_socket.sendto(message.encode(), address)
    server_socket.close()

if __name__ == '__main__':
    main()
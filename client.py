import socket, threading

def send():
    while True:
        msg = input('\nMe > ')
        cli_sock.send(msg.encode())

def receive():
    while True:
        
        data = cli_sock.recv(1024)

        print('\n' + str(data.decode()))

if __name__ == "__main__":   
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5023
    cli_sock.connect((HOST, PORT))     
    print('Connected to remote host...')
    uname = input('Enter your name to enter the chat > ')
    cli_sock.send(uname.encode())

    thread_send = threading.Thread(target = send)
    thread_send.start()

    thread_receive = threading.Thread(target = receive)
    thread_receive.start()

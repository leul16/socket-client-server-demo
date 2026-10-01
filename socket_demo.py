import socket
import argparse
import threading

DEFAULT_PORT = 4444
DEFAULT_MAX = 4096


def decode_and_strip(buf):
    return buf.decode('latin-1').strip()


def server_thread(sock):
    sock.send(b'------- Connected! --------')

    try:
        while True:
            data = sock.recv(DEFAULT_MAX)

            if not data:
                break

            message = decode_and_strip(data)

            if message:
                print(f'Client: {message}')

                response = f'Server received: {message}'
                sock.send(response.encode('latin-1'))

    except:
        pass
    finally:
        sock.close()


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', DEFAULT_PORT))
    sock.listen()

    print('-------------- Starting TCP Server ---------------')

    while True:
        client_sock, addr = sock.accept()

        print(f'--------------- Connection Established with {addr} ------------------')

        threading.Thread(
            target=server_thread,
            args=(client_sock,)
        ).start()


def send_thread(sock):
    try:
        while True:
            message = input()

            if message.lower() == 'exit':
                break

            sock.send(message.encode('latin-1'))

    except:
        pass
    finally:
        sock.close()


def recv_thread(sock):
    try:
        while True:
            data = sock.recv(DEFAULT_MAX)

            if not data:
                break

            output = decode_and_strip(data)

            if output:
                print(output, flush=True)

    except:
        pass


def client(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('--------------- Connecting to TCP Server ---------------')

    sock.connect((ip, DEFAULT_PORT))

    threading.Thread(
        target=send_thread,
        args=(sock,)
    ).start()

    threading.Thread(
        target=recv_thread,
        args=(sock,)
    ).start()


parser = argparse.ArgumentParser()

parser.add_argument(
    '-c',
    '--connect',
    help='connect to TCP server'
)

parser.add_argument(
    '-l',
    '--listen',
    action='store_true',
    help='start TCP server'
)

args = parser.parse_args()

if args.listen:
    server()
elif args.connect:
    client(args.connect)

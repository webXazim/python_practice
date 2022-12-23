import sys
import string
import itertools
import socket


def main(hostname, port):
    with socket.socket() as client:
        address = (str(hostname), int(port))
        client.connect(address)

        base_char = string.ascii_lowercase + string.digits
        for i in range(1, 4):
            for x in itertools.product(base_char, repeat=i):
                password = ''.join(x)
                data = password.encode()
                client.send(data)
                if client.recv(1024).decode() == 'Connection success!':
                    print(password)


main(sys.argv[1], sys.argv[2])

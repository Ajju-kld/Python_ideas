import socket

def main():
    host = "127.0.0.1"
    port = 8000

    s = socket.socket()
    s.bind((host, port)) #binding host and port no
    

    s.listen(1)
    print("Listening for incoming connections...")
    conn, addr = s.accept()
    print("Connection from: " + str(addr))

    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = str(data).upper()
        print("sending: " + str(data))
        conn.send(data.encode('utf-8'))
        print(s.getsockname())

    conn.close()

if __name__ == '__main__':
    main()

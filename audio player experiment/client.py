import socket
HOST = socket.gethostname()
PORT = 3741


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        full_data = b""

        while True:
            chunk = conn.recv(6)  # Read in chunks
            if b"<END>" in chunk:
                break  # Stop when end marker is received
            full_data += chunk

        print("Received:", full_data.decode())

import socket

HOST = socket.gethostname()  # Change as needed
PORT = 3741

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    data = "This is a test message that will be split into chunks."
    chunk_size = 6  # Example size
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        s.sendall(chunk.encode())

    s.sendall(b"<END>")  # Send an end marker

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3741))
s.listen(5)

audioDat = "some audio data idk"
"""k=4
chunks = [audioDat[i:i+k] for i in range(0, len(audioDat), k)]
print(chunks)"""

while True:
    client, addr = s.accept()
    for j in range(1,5):
        client.send(bytes(audioDat, "utf-8"))
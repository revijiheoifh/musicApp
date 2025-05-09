lalala = []
packet_length = 26

with open("musicApp/textToSend.txt", "r") as f:
    stringToSend = f.read()
    stringLen = len(stringToSend)
    current_position = 0

    while current_position < stringLen:
        segment = stringToSend[current_position:current_position + packet_length]
        lalala.append(segment)
        current_position += packet_length

print(lalala)
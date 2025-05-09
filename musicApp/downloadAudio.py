import subprocess
import socket

class fetchAudio:
    def __init__(self, link):
        self.link=link

    def commands(self):
        self.download = [
        'yt-dlp',
        '--format', 'bestaudio/best',
        '--quiet',
        '--no-warnings',
        '-o-',
        *self.link
        ]

        self.conversion = [
        'ffmpeg',
        '-i', 'pipe:0',      # Input from stdin
        '-f', 'wav',         # Output format WAV
        '-acodec', 'pcm_s16le',  # PCM codec (16-bit LE)
        '-ar', '44100',      # Sample rate
        '-ac', '2',         # Channels (stereo)
        '-loglevel','warning',
        'pipe:1'             # Output to stdout
        ]
    
    def downloading(self):
        downloadAudio = subprocess.Popen(self.download, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        convertToWAV = subprocess.Popen(self.conversion, stdin=downloadAudio.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.result, error = convertToWAV.communicate()
        downloadAudio.wait()

        if downloadAudio.returncode == 0 and convertToWAV == 0:
            print("this works\n")

        else:
            print("error: ", error.decode())

        return self.result



class sending:
    def __init__(self, audioBytes, ip, port):
        self.audioBytes=audioBytes
        self.ip=ip
        self.port=port
        self.packetLength = 65535
        self.packets=[]
    
    def setUpSender(self):
        try:
            self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.ip, self.port)

        except ConnectionRefusedError:
            print('Connection refused. Retrying in Now seconds...')

        except Exception as e:
            print(f'An error occurred: {e}')
            
    def segmentAudio(self):
        # read the string
        # get the length of the string
        self.audioLen = len(self.audioBytes)
        # track the position that the loop has reached
        self.currentPosition = 0

        while self.currentPosition < self.audioLen:
            self.segment = self.audioBytes[self.currentPosition:self.currentPosition + self.packetLength]
            self.packets.append(self.segment)
            self.currentPosition+=self.packetLength

        print("packet length: ", len(self.packets))
    def sendAudioBytes(self):
        pass

    

if __name__ == "__main__":
    downloadAud=fetchAudio(['https://www.youtube.com/watch?v=VAXg78MKJcM'])
    downloadAud.commands()

    sendAud = sending(downloadAud.downloading(), socket.gethostbyname(socket.gethostname()), 3256)
    print("audio length: ", len(downloadAud.downloading()))
    sendAud.segmentAudio()
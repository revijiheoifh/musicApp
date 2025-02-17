import subprocess

class fetchAudio:
    def __init__(self, link):
        self.audioBytes=b''
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

fetcher = fetchAudio(['https://www.youtube.com/watch?v=R8rlVgbNpEQ'])
fetcher.commands()
fetcher.downloading()
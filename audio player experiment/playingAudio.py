# import the libraries
from io import BytesIO
import subprocess
import pyaudio

mem_file = BytesIO()

url = ['https://www.youtube.com/watch?v=SSbBvKaM6sk']

download = [
    'yt-dlp',
    '--format', 'bestaudio/best',
    '--quiet',
    '--no-warnings',
    '-o-',
    *url
]

conversion = [
    'ffmpeg',
    '-i', 'pipe:0',  # Input from stdin
    '-f', 'wav',     # Format as MP3
    '-acodec', 'pcm_u8',  # Use MP3 codec
    '-ab', '192k',   # Bitrate
    'pipe:1'         # Output to stdout
]

downloadAudio = subprocess.Popen(download, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
convertToWAV = subprocess.Popen(conversion, stdin=downloadAudio.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result, error = convertToWAV.communicate()
downloadAudio.wait()

if downloadAudio.returncode == 0 and convertToWAV == 0:
    print("this works\n")

else:
    print("error: ", error.decode())



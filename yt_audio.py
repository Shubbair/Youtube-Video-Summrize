import os
from pytube import YouTube

def download_audio(vid_url):
    
    # Create a YouTube object
    yt = YouTube(vid_url)

    # Get the best audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Download the audio
    audio_path = 'audio/'
    audio_stream.download(output_path=audio_path)

    old_filename = f'{audio_path}/{yt.title}.mp4'
    new_filename = f'{audio_path}/temp.wav'

    os.rename(old_filename, new_filename)

    print(f"Audio saved as {new_filename}")

vid_url = 'https://www.youtube.com/watch?v=AVMi3gcMzOI'
download_audio(vid_url)
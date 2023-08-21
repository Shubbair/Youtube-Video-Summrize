#!/usr/bin/env python3

import os
import sys
import youtube_dl
import speech_recognition as sr

video_url = None

try:
    if(len(sys.argv[1]) > 5):        
        video_url = sys.argv[1]
except:
    print("No Input Provided")

# download video audio
def download_mp3(url, output_file_name):
    ydl_opts = {
        'verbose': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_file_name}.%(ext)s',
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except youtube_dl.utils.DownloadError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)

# get text from audio
def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)  # Record the audio from the file

    try:
        # Perform speech recognition
        text = recognizer.recognize_google(audio,language="ar-EG")
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

output_name = 'temp'
try:
    download_mp3(video_url, output_name)
except:
    print('There is error occur during download the audio')

audio_file_path = 'temp.wav'

if(os.path.exists(audio_file_path)):
    text = transcribe_audio(audio_file_path)
    
    if text:
        print("Transcribed text")
        output_file_path = 'text.txt'
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)

Youtube_ID = "SW14tOda_kI"

from youtube_transcript_api import YouTubeTranscriptApi

try:
    texts = YouTubeTranscriptApi.get_transcript(Youtube_ID,languages=['en'])
    text_data : str = ''
    for item in range(0,len(texts)):
        text_data += texts[item]['text']

    if text_data:
        output_file_path = 'text.txt'
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text_data)
        print("text saved in text.txt file")
except:
    print('There is no captions')
import re
import time
import streamlit as st
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

# function to get if from youtube url
def get_youtube_video_id(url):
    pattern = r"(?:v=|\/videos\/|embed\/|youtu.be\/|\/v\/|\/e\/|watch\?v=|&v=|embed\?v=|\/d\/|\/v\/|\?v=)([\w-]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

def main():
    st.title("Video Summrizer")
    
    # Sidebar for user input
    search_query = st.text_input("Enter YT URL:",max_chars=150)
    
    if search_query:
        video_id = get_youtube_video_id(str(search_query))
        
        text_data : str = ''

        try:
            texts = YouTubeTranscriptApi.get_transcript(video_id,languages=['en'])
            # import large language summrizer from facebook ~Bart
            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

            for item in range(0,len(texts)):
                text_data += texts[item]['text']

            # while(summarizer):
            #     with st.spinner('Wait for it...'):
            #         time.sleep(5)
            # else:
            st.subheader('Summrized Text : ')
            text_summary = summarizer(text_data, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
            st.markdown("<p style='text-align: left; color: grey;'>"+text_summary+"</p>", unsafe_allow_html=True)

        except:
            st.text('This video has no captions :(')
        
if __name__ == "__main__":
    main()
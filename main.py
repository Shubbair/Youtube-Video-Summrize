import time
import streamlit as st

# Youtube_ID = "SW14tOda_kI"

# from youtube_transcript_api import YouTubeTranscriptApi

# try:
#     texts = YouTubeTranscriptApi.get_transcript(Youtube_ID,languages=['en'])
#     text_data : str = ''
#     for item in range(0,len(texts)):
#         text_data += texts[item]['text']

#     if text_data:
#         output_file_path = 'text.txt'
#         with open(output_file_path, 'w', encoding='utf-8') as output_file:
#             output_file.write(text_data)
#         print("text saved in text.txt file")
# except:
#     print('There is no captions')

def main():
    st.title("Video Summrizer")
    
    # Sidebar for user input
    search_query = st.sidebar.text_input("Enter YT URL:")
    
    # Display search results
    st.subheader("the search : " + search_query)

    # search_button = st.sidebar.button("Search")
    if search_query:
        # Display spinner while performing the search
        while(len(search_query) < 5):
            with st.spinner('Wait for it...'):
                time.sleep(5)
        else:
            print('yeas')

if __name__ == "__main__":
    main()
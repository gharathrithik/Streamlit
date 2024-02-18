import streamlit as st
from PIL import Image

st.title('1. Image with Path')
img = Image.open(r'C:\Users\ghara\OneDrive\Desktop\Streamlit\Models.jpeg')
st.image(img)

st.title('2. Image with Link')
st.image('https://img.hotstar.com/image/upload/v1656431456/web-images/logo-d-plus.svg', width = 700)

st.title('3. Video')
video_file = open(r'C:\Users\ghara\OneDrive\Desktop\Streamlit\video.mp4', 'rb')
st.video(video_file)

st.title('4. Audio')
audio_file = open(r'C:\Users\ghara\OneDrive\Desktop\Streamlit\sample.mp3', 'rb')
st.audio(audio_file.read())

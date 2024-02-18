import pandas as pd
import streamlit as st
from PIL import Image

st.title('File Uploading')

st.subheader('1. Uploading an Image')
img_file = st.file_uploader('Upload a file', type = ['png', 'svg', 'jpg', 'jpeg'])
if img_file is not None:
    file_details = {'File Name' : img_file.name, 'File Type' : img_file.type, 'File Size' : img_file.size}
    st.write(file_details)
    st.image(img_file)

st.subheader('2. Uploading an Audio')
audio_file = st.file_uploader('Upload a file', type = ['wav', 'mp3'])
if audio_file is not None:
    file_details = {'File Name' : audio_file.name, 'File Type' : audio_file.type, 'File Size' : audio_file.size}
    st.write(file_details)
    st.audio(audio_file.read())

st.subheader('3. Uploading a Video')
video_file = st.file_uploader('Upload a file', type = ['mov', 'mp4'])
if video_file is not None:
    file_details = {'File Name' : video_file.name, 'File Type' : video_file.type, 'File Size' : video_file.size}
    st.write(file_details)
    st.video(video_file)

st.subheader('4. Uploading a CSV File')
csv_file = st.file_uploader('Upload a file', type = ['csv', 'xlsx', 'txt'])
if csv_file is not None:
    file_details = {'File Name' : csv_file.name, 'File Type' : csv_file.type, 'File Size' : csv_file.size}
    st.write(file_details)
    df = pd.read_csv(csv_file)
    st.dataframe(df)

import streamlit as st
from PIL import Image

st.title('Image Converter')

def convert_image(image_path, new_format):
    with Image.open(image_path) as img:

        new_name   = image_path.name.split('.')[0] + '.' + new_format
        final_path = 'C:/Users/ghara/OneDrive/Desktop/Streamlit' + '/' + new_name

        img.save(final_path)
        
        st.success('Image Saved in .' + new_format + ' Format Successfully')


image_path = st.file_uploader('Upload a File', type = ['png', 'jpg', 'jpeg'])

new_format = st.selectbox('Select the format of the Image', ['png', 'jpg', 'jpeg'])

if st.button('Convert'):
    if image_path is not None:
        convert_image(image_path, new_format)
    else:
        st.error('Please upload a File')

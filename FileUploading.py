import pandas as pd
import streamlit as st
from PIL import Image

st.title('File Uploading')

# 1. Image
st.subheader('1. Uploading an Image')
img_file = st.file_uploader('Upload Image', type = ['png','jpeg','jpg'])
if img_file is not None:
    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                    'file_size' : img_file.size}
    st.write(file_details)
    st.image(Image.open(img_file), width = 500)

# 2. Audio
st.subheader('2. Uploading an Audio')
aud_file = st.file_uploader('Upload Image', type = ['wav','mp3'])
if aud_file is not None:
    file_details = {'file_name' : aud_file.name, 'file_type' : aud_file.type,
                    'file_size' : aud_file.size}
    st.write(aud_file)
    st.audio(aud_file)

# 3. Video
st.subheader('3. Uploading an Video')
vid_file = st.file_uploader('Upload Video', type = ['mov','mp4'])
if vid_file is not None:
    file_details = {'file_name' : vid_file.name, 'file_type' : vid_file.type,
                    'file_size' : vid_file.size}
    st.write(vid_file)
    st.video(vid_file)

# 3. CSV
st.subheader('4. Uploading a CSV File')
csv_file = st.file_uploader('Upload CSV File', type = ['csv'])
if csv_file is not None:
    file_details = {'file_name' : csv_file.name, 'file_type' : csv_file.type,
                    'file_size' : csv_file.size}
    st.write(file_details)
    st.dataframe(csv_file)
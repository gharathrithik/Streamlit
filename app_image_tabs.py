import numpy as np
import pandas as pd
import streamlit as st

tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])
tab1.image('https://static.streamlit.io/examples/cat.jpg')
tab2.image('https://static.streamlit.io/examples/dog.jpg')
tab3.image('https://static.streamlit.io/examples/owl.jpg')

img_link = pd.read_csv(r'C:\Users\ghara\OneDrive\Desktop\Streamlit\imgs.csv')['img_link']

tabs = st.tabs(['ID'] * 10)

for tab in tabs:
    image = img_link[np.random.randint(1, 1000)]
    tab.image(image)

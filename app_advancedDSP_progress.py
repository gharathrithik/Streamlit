import streamlit as st
import time

st.set_page_config(page_title = 'GeeksForGeeks', page_icon = '👨‍💻', layout = 'wide')

with st.spinner('Wait for it'):
    time.sleep(5)

with st.empty():
    for percent_comp in range(101):
        st.progress(percent_comp, 'Processing')
        time.sleep(.1)
    st.success('Congratulations !!!')

st.balloons()
st.snow()

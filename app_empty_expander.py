import numpy as np
import pandas as pd
import streamlit as st
import time

cases = []
for i in range(100):
    cases.append(np.random.randint(1, 7))

data = []
for ct in range(1, 7):
    data.append(cases.count(ct))

st.header('Frequency of getting each face')
st.bar_chart({'data' : data})

with st.expander('See Explanation'):
    st.write('''
        The chart shows some numbers I got from rolling a dice 100 times and its
        basically about how many times each face appears
    ''')
    st.image('https://static.streamlit.io/examples/dice.jpg', width = 200)

with st.empty():
    for seconds in range(11):
        st.write('⏳ ' + str(seconds) + ' seconds remaining')
        time.sleep(1)
    st.write('10 seconds completed')

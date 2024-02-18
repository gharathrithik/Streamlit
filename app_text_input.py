import datetime
import streamlit as st

st.subheader('1. Text Input')
name = st.text_input('Enter your name: ', placeholder = 'Eg. Hrithik Gharat')
st.write('Hello ' + name)

st.subheader('2. Password Input')
st.text_input('Enter your password: ', type = 'password', help = 'Atleast 8 Characters')

st.subheader('3. Text Area')
st.text_area('Tell me about your yourself: ', height = 200, max_chars = 500, help = 'Max 500 Characters Allowed')

st.subheader('4. Number Input')
st.number_input('Enter your Age: ', min_value = 1, max_value = 100)

date = datetime.date.today()
st.subheader('5. Date Input')
st.date_input('Enter a Date: ', min_value = date, max_value = date.replace(year = date.year + 1))

import streamlit as st

def func_name():
    return 'Hrithik'
with st.echo():
    greetings = 'Hi there'
    def func_punc():
        return '!!!'
    name = func_name()
    punc = func_punc()
    st.write(greetings, name, punc)

first_name = st.text_input('Enter your First Name: ')
if not first_name:
    st.warning('Please enter your first name.')
    st.stop()
last_name = st.text_input('Enter your Last Name: ')
if not last_name:
    st.warning('Please enter your last name.')
    st.stop()

st.success('Thank you for entering the name !')

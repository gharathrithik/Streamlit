import streamlit as st

st.title('BMI Calculator')

with st.form('BMI Calculator'):
    col1, col2, col3 = st.columns([3, 2, 1])
with col1:
    weight = st.number_input('Enter your weight in kgs')
with col2:
    height = st.number_input('Enter your Height in meters')
with col3:
    submit = st.form_submit_button('Calculate')

if submit:
    BMI = weight / (height ** 2)
    if BMI <= 18.5:
        st.error('Underweight')
    elif BMI > 18.5 and BMI <= 24.9:
        st.success('Healthy / Normal weight')
    elif BMI > 24.9 and BMI <= 29.9:
        st.warning('Overweight')
    elif BMI > 29.9:
        st.error('Obese')
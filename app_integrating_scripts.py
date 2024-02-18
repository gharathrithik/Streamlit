import streamlit as st

def bmi_calculator():
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



def rate_yourself():
    with st.sidebar:
        st.title('Rate Yourself')
        languages = st.text_input('Enter the programming languages you know with comma separation', value='Python')
        languages = [i.strip() for i in languages.split(',')]

    st.subheader('How would you rate your experience in the following programming languages & tools?')

    for language in languages: 
        st.slider(language, min_value = 0., max_value = 10., step = 0.5)



choice = st.sidebar.selectbox("Menu", ['BMI Calculator', 'Rate Yourself'])

if choice == 'BMI Calculator':
    bmi_calculator()
elif choice ==  'Rate Yourself':
    rate_yourself()

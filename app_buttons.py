import streamlit as st

st.subheader('1. Radio Buttons')
gender = st.radio('Select your gender', options = ('Male', 'Female', 'Others'), help = 'Choose One', horizontal = True)
st.write('You have selected', gender)

career_options = ('Data Analysis', 'ML', 'DL', 'AI')
st.subheader('2. Select Box')
career = st.selectbox('Select your Gender', career_options, help = 'Choose One')
st.write('You have selected', career)

st.subheader('3. Multi-Select Box')
st.multiselect('Select your Gender', options = ('Data Analysis', 'ML', 'DL', 'AI'), help = 'Choose One', default = 'Data Analysis')

st.subheader('4. Button')
if st.button('Say Hello'):
    st.write('Hi')

st.subheader('5. Checkbox')
if st.checkbox('I agree to the following terms and conditions', help = 'Please agree the terms and conditions'):
    st.write('Thanks for agreeing!')

st.subheader('6. Colour Picker')
colour = st.color_picker('Select your favourite colour', '#FFFFFF')
st.write('You have selected', colour, 'colour')

st.button('Submit', use_container_width = True)
import pandas as pd
import streamlit as st

df = pd.read_csv(r'C:\Users\ghara\OneDrive\Desktop\Streamlit\abalone.csv')

st.subheader('1. Displaying the DataFrame')
st.dataframe(df)

st.subheader('2. Displaying the First 5 rows')
st.dataframe(df.head())

st.subheader('3. Displaying the Last 5 rows')
st.dataframe(df.tail())

st.subheader('4. Displaying in the Table Format (First 10 rows)')
st.table(df.head(10))

st.subheader('5. Displaying JSON')
st.json([{'pid' : 1, 'name' : '5 star'}, {'pid' : 2, 'name' : 'Milky Bar'},
         {'pid' : 3, 'name' : 'Mars'}, {'pid' : 4, 'name' : 'Dairy Milk'}])

st.subheader('6. Displaying the Description of Data')
st.table(df.describe())

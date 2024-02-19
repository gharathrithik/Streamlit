import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader('Data Visualization using Matplotlib and Seaborn')

st.text('1. Displaying the Dataset')
df = pd.read_csv(r'C:\Users\ghara\OneDrive\Desktop\Streamlit\Iris.csv')
st.dataframe(df)

st.text('2. Bar plot using Matplotlib')
fig = plt.figure(figsize = (15, 8))
df['Species'].value_counts().plot(kind = 'bar')
st.pyplot(fig)

st.text('3. DistPlot using Seaborn')
fig = plt.figure(figsize = (15, 8))
sns.distplot(df['SepalLengthCm'])
st.pyplot(fig)

st.text('4. Displaying Multiple Graphs')
col1, col2 = st.columns(2)
with col1:
    col1.write('KDE = False')
    fig = plt.figure()
    sns.distplot(df['SepalLengthCm'], kde = False)
    st.pyplot(fig)
with col2:
    col2.write('Hist = False')
    fig = plt.figure()
    sns.distplot(df['SepalLengthCm'], hist = False)
    st.pyplot(fig)

st.text('5. Changing the Styles of Graphs')
col1, col2 = st.columns(2)
with col1:
    sns.set_style('darkgrid')
    sns.set_context('poster')
    fig = plt.figure()
    sns.distplot(df['SepalLengthCm'], hist = False)
    st.pyplot(fig)
with col2:
    sns.set_theme(style = 'darkgrid', context = 'notebook')
    fig = plt.figure()
    sns.distplot(df['SepalLengthCm'], hist = False)
    st.pyplot(fig)

st.text('6. Scatter Plot')
fig, ax = plt.subplots(figsize = (15, 8))
ax.scatter(*np.random.random(size = (2, 100)))
st.pyplot(fig)

st.text('7. Count Plot')
fig = plt.figure(figsize = (15, 8))
sns.countplot(data = df, x = 'Species')
st.pyplot(fig)

st.text('8. Box Plot')
fig = plt.figure(figsize = (15, 8))
sns.boxplot(data = df, x = 'Species', y = 'SepalLengthCm')
st.pyplot(fig)

st.text('9. Violin Plot')
fig = plt.figure(figsize = (15, 8))
sns.violinplot(data = df, x = 'Species', y = 'SepalLengthCm')
st.pyplot(fig)

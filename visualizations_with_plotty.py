import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

st.title('Visualizations with Plotty')
df = pd.read_csv(r'C:\Users\ghara\OneDrive\Desktop\Streamlit\tips.csv')

st.text('1. Pie Chart')
fig = px.pie(data_frame = df, values = 'total_bill', names = 'day')
st.plotly_chart(fig)

st.text('2. Pie Chart with a Hole')
fig = px.pie(data_frame = df, values = 'total_bill', names = 'day', opacity = .8, hole = .5,
             color_discrete_sequence = px.colors.sequential.Burg_r)
st.plotly_chart(fig)

st.text('3. Multiple Dist Plots')
x1 = np.random.randn(200) + 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) - 2

hist_data = [x1, x2, x3]
group_labels = ['G1', 'G2', 'G3']

fig = ff.create_distplot(hist_data, group_labels, bin_size = [.1, .1, .1])
st.plotly_chart(fig)

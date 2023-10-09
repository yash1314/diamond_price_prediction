import streamlit as st
import time
import joblib

@st.cache_resource()
def model_load(path):
    model = joblib.load(path)
    return model

model = model_load('model1.joblib')


st.title('Diamond Price Prediction')
st.markdown('#### The goal is to predict price of given diamond using various parameters. The model has an accuracy score of 97.3%')


st.markdown('##### Carat')
carat = st.text_input('Enter carat in range of  0.2-3.5: ')
st.markdown('##### Cut')
cut = st.text_input('Enter cut as numerical value from: Fair: 1, Good: 2, Very Good: 3, Premium: 4, Ideal: 5: ')
st.markdown('##### Color')
color = st.text_input('Enter color as numerical value from: D:1, E:2 ,F:3 ,G:4 , H:5 , I:6, J:7')
st.markdown('##### Clarity')
clarity = st.text_input('Enter clarity value as numerical value from: I1:1, SI2:2, SI1:3, VS2:4, VS1:5, VVS2:6, VVS1:7, IF:8')
st.markdown('##### Depth')
depth = st.text_input('Enter depth value in range of 52-72')
st.markdown('##### Table')
table = st.text_input('Enter depth value in range of 49-79')

if st.button('Predict'):

    # 2. predict
    result = model.predict([[carat, cut, color, clarity, depth, table]])

    bar = st.progress(50)
    time.sleep(1)
    bar.progress(100)
    st.success('Success')

    # 3. display
    st.header(f'The predicted price of diamond is: {result}$')





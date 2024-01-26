import pandas as pd
import streamlit as st
import time
import joblib

@st.cache_resource()
def model_load(path):
    model = joblib.load(path)
    return model

model = model_load('model/model1.joblib')


st.title(':rainbow[Diamond Price Prediction]:rainbow')
st.markdown('----------------------------------------------')
st.markdown('The goal is to predict price of given diamond using various parameters. The model has an accuracy score of 97.3%')
st.markdown(' ')
cols1, cols2 = st.columns(2)

with cols1:
    st.markdown('#### Carat')
    carat = st.slider(" ", 0.2, 3.5)

    st.markdown('#### Clarity')
    clarity = st.slider(" ", 1, 8)

    st.markdown('#### Depth')
    depth = st.slider(" ", 52, 72)


with cols2:
    st.markdown('#### Table')
    table = st.slider(" ", 49, 79)


    st.markdown('#### Cut')
    cut = st.selectbox("Cut range : Fair, Good, Very Good, Premium, Ideal",
                       ["Fair", "Good", "Very Good", "Premium", "Ideal"])
    cut = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}.get(cut)


    st.markdown('#### Color')
    color = st.selectbox('Color range : D, E, F, G, H, I, J',
                         ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    color = {'D': 1, 'E': 2, 'F': 3, 'G': 4, 'H': 5, 'I': 6, 'J': 7}.get(color)


if st.button('Predict'):
    try:
        # prediction
        result = model.predict([[carat, cut, color, clarity, depth, table]])

    except Exception as e:
        st.markdown(e)
        st.info('Enter valid details!')

    else:
        bar = st.progress(50)
        time.sleep(1)
        bar.progress(100)
        
        # 3. result display
        st.subheader(f'The predicted price of diamond is: {result} $')
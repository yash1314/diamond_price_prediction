import streamlit as st
import time
import joblib

@st.cache_resource()
def model_load(path):
    model = joblib.load(path)
    return model

model = model_load('model\model1.joblib')


st.title('Diamond Price Prediction')
st.markdown('The goal is to predict price of given diamond using various parameters. The model has an accuracy score of 97.3%')
st.markdown(' ')
cols1, cols2 = st.columns(2)

with cols1:
    st.markdown('##### Carat')
    carat = st.text_input('Range : 0.2-3.5: ')
    st.markdown('##### Cut')
    cut = st.text_input('Fair: 1, Good: 2, Very Good: 3, Premium: 4, Ideal: 5: ')
    st.markdown('##### Color')
    color = st.text_input('Color range : D:1, E:2 ,F:3 ,G:4 , H:5 , I:6, J:7')

with cols2:
    st.markdown('##### Clarity')
    clarity = st.text_input('Range: 1-10, in increasing order of clarity.')
    st.markdown('##### Depth')
    depth = st.text_input('Depth range: 52-72')
    st.markdown('##### Table')
    table = st.text_input('Table range: 49-79')

if st.button('Predict'):

    
    try:
        # 2. predicts
        result = model.predict([[carat, cut, color, clarity, depth, table]])

    except Exception as e:
        st.info('Enter valid details!')

    else:
        bar = st.progress(50)
        time.sleep(1)
        bar.progress(100)
        

        # 3. result display
        st.header(f'The predicted price of diamond is: {result}$')





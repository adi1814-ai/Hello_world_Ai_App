import streamlit as st
import numpy as np
from model import train

#Title
st.title("Hello World AI App")
st.subheader("A simple regression model")

#Train model
model= train()
#SIDEBAR
st.sidebar.header("Input Features")
input_value=st.sidebar.slider("Select the value of x", 1,10,1)

input_array=np.array([[input_value]])
Prediction=model.predict(input_array)

#display_result
st.write(f'### Input value : {input_value}')
st.write(f'### Output value : {Prediction[0]:.2f}')
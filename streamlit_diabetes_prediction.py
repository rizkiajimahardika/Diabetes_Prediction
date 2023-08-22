# importing Important Liberaries
import pickle
import streamlit as st
import numpy as np

# Load model
model_diabetes = pickle.load(open('model_diabetes.sav', 'rb'))

# Web Title
st.title('Diabetes Prediction')

# Split Columns
col1, col2 = st.columns(2)

with col1 :
  Pregnancies = st.number_input('Enter the Pregnancies value')

with col2 :
  Glucose = st.number_input('Enter the Glucose value')
  
with col1 :
  BloodPressure = st.number_input('Enter the Blood Pressure value')

with col2 :
  SkinThickness = st.number_input('Enter the Skin Thickness value')

with col1 :
  Insulin = st.number_input('Enter the Insulin value')

with col2 :
  BMI = st.number_input('Enter the BMI value')

with col1 :
  DiabetesPedigreeFunction = st.number_input('Enter the Diabetes Pedigree Function value')

with col2 :
  Age = st.number_input('Enter the Age value')
  
# Prediction
diabetes_diagnosis = ''

if st.button('Diabetes Prediction Test'):
  diabetes_prediction = model_diabetes.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
  
  if(diabetes_prediction[0]==1):
    diabetes_diagnosis = 'The patient has diabetes'
  else :
    diabetes_diagnosis = 'The patient does not have diabetes'

st.success(diabetes_diagnosis)


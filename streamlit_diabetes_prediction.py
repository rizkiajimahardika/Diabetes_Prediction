# importing Important Liberaries
import pickle
import streamlit as st

# Load model
model_diabetes = pickle.load(open('model_diabetes.sav', 'rb'))

# Web Title
st.title('Diabetes Prediction')

# Split Columns
col1, col2 = st.columns(2)

with col1 :
  Pregnancies = st.text_input('Enter the Pregnancies value')

with col2 :
  Glucose = st.text_input('Enter the Glucose value')
  
with col1 :
  Blood_Pressure = st.text_input('Enter the Blood Pressure value')

with col2 :
  Skin_Thickness = st.text_input('Enter the Skin Thickness value')

with col1 :
  Insulin = st.text_input('Enter the Insulin value')

with col2 :
  BMI = st.text_input('Enter the BMI value')

with col1 :
  Diabetes_Pedigree_Function = st.text_input('Enter the Diabetes Pedigree Function value')

with col2 :
  Age = st.text_input('Enter the Age value')
  
# Prediction
diabetes_diagnosis = ''

if st.button('Diabetes Prediction Test'):
  diabetes_prediction = model_diabetes.predict([[Pregnancies,Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,Diabetes_Pedigree_Function,Age]])
  
  if(diabetes_prediction[0]==0):
    diabetes_diagnosis = 'The patient does not have diabetes'
  else :
    diabetes_diagnosis = 'The patient has diabetes'

st.success(diabetes_diagnosis)


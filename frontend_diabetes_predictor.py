import streamlit as st
import pickle
import numpy as np

# Load model + scaler
model = pickle.load(open('model1.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Diabetes Prediction App")

# Inputs
glucose = st.number_input("Glucose")
bloodpressure = st.number_input("Blood Pressure")
skinthickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
diabetespedigreefunction = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Predict"):
    input_data = np.array([[glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]])
    
    # ✅ APPLY SCALING (THIS WAS MISSING)
    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Person is Diabetic")
    else:
        st.success("Person is Not Diabetic")
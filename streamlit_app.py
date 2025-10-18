import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ---- Load Model (replace 'your_model.pkl' with your model file) ----
# model = pickle.load(open('your_model.pkl', 'rb'))

st.title("Health Risk Prediction App")

# ---- User Inputs ----
st.header("Enter your details:")

# Numerical Inputs
age = st.number_input("AGE",min_value=0,value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
waist_to_hip_ratio = st.number_input("Waist to Hip Ratio", min_value=0.5, max_value=1.5, value=0.85)
systolic_bp = st.number_input("Systolic BP", min_value=80, max_value=200, value=120)
diastolic_bp = st.number_input("Diastolic BP", min_value=50, max_value=120, value=80)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=120, value=70)
cholesterol_total = st.number_input("Total Cholesterol", min_value=100, max_value=400, value=180)
hdl_cholesterol = st.number_input("HDL Cholesterol", min_value=20, max_value=100, value=50)
ldl_cholesterol = st.number_input("LDL Cholesterol", min_value=50, max_value=300, value=100)
triglycerides = st.number_input("Triglycerides", min_value=30, max_value=400, value=150)
glucose_fasting = st.number_input("Fasting Glucose", min_value=60, max_value=200, value=90)
glucose_postprandial = st.number_input("Postprandial Glucose", min_value=80, max_value=300, value=120)
insulin_level = st.number_input("Insulin Level", min_value=0.0, max_value=50.0, value=10.0)
hba1c = st.number_input("HbA1c", min_value=4.0, max_value=15.0, value=6.0)
diet_score = st.number_input("Diet Score", min_value=0.0, max_value=10.0, value=5.0)
sleep_hours_per_day = st.number_input("Sleep Hours Per Day", min_value=0.0, max_value=15.0, value=7.0)
screen_time_hours_per_day = st.number_input("Screen Time Hours Per Day", min_value=0.0, max_value=20.0, value=5.0)
physical_activity_minutes_per_week = st.number_input("Physical Activity Minutes Per Week", min_value=0, max_value=1000, value=150)

family_history_diabetes = st.selectbox("Family History of Diabetes", [0, 1])
hypertension_history = st.selectbox("Hypertension History", [0, 1])
cardiovascular_history = st.selectbox("Cardiovascular History", [0, 1])

gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
ethnicity = st.selectbox("Ethnicity", ['Asian', 'White', 'Hispanic', 'Black', 'Other'])
education_level = st.selectbox("Education Level", ['Highschool', 'Graduate', 'Postgraduate', 'No formal'])
income_level = st.selectbox("Income Level", ['Lower-Middle', 'Middle', 'Low', 'Upper-Middle', 'High'])
employment_status = st.selectbox("Employment Status", ['Employed', 'Unemployed', 'Retired', 'Student'])
smoking_status = st.selectbox("Smoking Status", ['Never', 'Former', 'Current'])
alcohol_consumption_per_week = st.number_input("Alcohol Consumption per Week", min_value=0, max_value=20, value=2)

input_data = pd.DataFrame({
    "age": [age],
    "gender": [gender],
    "ethnicity": [ethnicity],
    "education_level": [education_level],
    "income_level": [income_level],
    "employment_status": [employment_status],
    "smoking_status": [smoking_status],
    "alcohol_consumption_per_week": [alcohol_consumption_per_week],
    "physical_activity_minutes_per_week": [physical_activity_minutes_per_week],
    "diet_score": [diet_score],
    "sleep_hours_per_day": [sleep_hours_per_day],
    "screen_time_hours_per_day": [screen_time_hours_per_day],
    "family_history_diabetes": [family_history_diabetes],
    "hypertension_history": [hypertension_history],
    "cardiovascular_history": [cardiovascular_history],
    "bmi": [bmi],
    "waist_to_hip_ratio": [waist_to_hip_ratio],
    "systolic_bp": [systolic_bp],
    "diastolic_bp": [diastolic_bp],
    "heart_rate": [heart_rate],
    "cholesterol_total": [cholesterol_total],
    "hdl_cholesterol": [hdl_cholesterol],
    "ldl_cholesterol": [ldl_cholesterol],
    "triglycerides": [triglycerides],
    "glucose_fasting": [glucose_fasting],
    "glucose_postprandial": [glucose_postprandial],
    "insulin_level": [insulin_level],
    "hba1c": [hba1c]
})


st.dataframe(input_data)

if st.button("Predict"):
    try:
        import requests  
        response = requests.post("http://127.0.0.1:5000/predict", json=input_data.to_dict(orient='records')[0])
        result = response.json()
        if 'prediction' in result:
            st.success(f"Predicted Health Risk: {result['prediction']}")
        else:
            st.error(result.get('error', 'Unknown error'))
    except Exception as e:
        st.error(f"Error connecting to Flask API: {e}")
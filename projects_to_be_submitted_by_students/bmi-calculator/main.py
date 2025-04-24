import streamlit as st
import pandas as pd

st.title("BMI Calculator")

# Slider for height input
height = st.slider("Enter your height (in cm):", 100, 250, 175)
# Slider for weight input
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

# Check if height is zero to avoid division by zero
if height > 0:
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is {bmi:.2f}")

    st.write("### BMI Categories ###")
    st.write("_Underweight: BMI less than 18.5_")
    st.write("_Normal weight: BMI between 18.5 and 24.9_")
    st.write("_Overweight: BMI between 25 and 29.9_")
    st.write("_Obesity: BMI 30 or greater_")
else:
    st.write("Error: Height cannot be zero.")

import streamlit as st
import joblib as jb
import pandas as pd
# Load the trained model
model = jb.load('/home/rashmin/Codeshit/techsaksham/module3/energy_model.pkl')
# Create a Streamlit app
st.write("Energy Consumption Prediction App")
data = pd.read_csv('/home/rashmin/Codeshit/techsaksham/module3/appliance_energy.csv')
st.write("Dataset Preview:")
st.write(data.head())
st.line_chart(data['Energy Consumption (kWh)'])
# User input for temperature
temp = st.number_input("Enter the temperature (°C):", value=20.0)
# Predict energy consumption
if st.button("Predict Energy Consumption"):
    predicted_energy = model.predict([[temp]])
    st.write(f"Predicted energy consumption for temperature {temp}°C: {predicted_energy[0]:.2f} kWh")
import streamlit as st
import pandas as pd
from src.predict import predict_score
from src.generate_data import generate_dataset
from src.train_model import train
import os

st.title("Student Score Predictor")

st.sidebar.header("Actions")
if st.sidebar.button("Generate Dataset"):
    generate_dataset()
    st.sidebar.success("Dataset generated!")

if st.sidebar.button("Train Model"):
    train()
    st.sidebar.success("Model trained!")

st.header("Predict Student Score")

hours = st.number_input("Study Hours", min_value=0.0, max_value=10.0, value=5.0)
attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0, value=80.0)
previous = st.number_input("Previous Marks", min_value=0.0, max_value=100.0, value=70.0)

if st.button("Predict Score"):
    if os.path.exists("../model/model.pkl"):
        score = predict_score(hours, attendance, previous)
        st.success(f"Predicted Final Score: {score:.2f}")
    else:
        st.error("Model not found. Please train the model first.")

st.header("Dataset Preview")
if os.path.exists("../data/dataset.csv"):
    df = pd.read_csv("../data/dataset.csv")
    st.dataframe(df.head())
else:
    st.write("Dataset not found. Generate dataset first.")
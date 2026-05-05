# Student Score Predictor

This project uses supervised learning (Linear Regression) to predict student scores.

## Steps to Run the Student Score Predictor

1. Install dependencies:
   pip install -r requirements.txt

2. Generate dataset:
   python src/generate_data.py

3. Train model:
   python src/train_model.py

4. Run prediction (CLI):
   python main.py

5. Run Streamlit Web App:
   streamlit run streamlit_app.py

## Features

- Generate synthetic dataset
- Train linear regression model
- Predict student scores based on study hours, attendance, and previous marks
- Interactive web interface with Streamlit
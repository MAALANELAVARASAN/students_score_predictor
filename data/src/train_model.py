import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from utils import save_model
import os

def train():
    df = pd.read_csv("../data/dataset.csv")

    X = df[['hours', 'attendance', 'previous']]
    y = df['score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    error = mean_absolute_error(y_test, predictions)

    os.makedirs("../model", exist_ok=True)
    save_model(model, "../model/model.pkl")

    print(" Model trained and saved!")
    print(" Mean Absolute Error:", error)

if __name__ == "__main__":
    train()
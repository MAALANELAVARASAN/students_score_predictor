from utils import load_model

def predict_score(hours, attendance, previous):
    model = load_model("../model/model.pkl")
    result = model.predict([[hours, attendance, previous]])
    return result[0]
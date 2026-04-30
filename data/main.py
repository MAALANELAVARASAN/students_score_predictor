from src.predict import predict_score

print(" Student Score Predictor")

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance (%): "))
previous = float(input("Enter previous marks: "))

score = predict_score(hours, attendance, previous)

print(f" Predicted Final Score: {score:.2f}")
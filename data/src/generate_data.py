import pandas as pd
import numpy as np
import os

def generate_dataset():
    np.random.seed(42)
    size = 100

    hours = np.random.uniform(1, 10, size)
    attendance = np.random.uniform(50, 100, size)
    previous = np.random.uniform(40, 100, size)

    score = (
        0.5 * hours +
        0.3 * (attendance / 10) +
        0.2 * (previous / 10) +
        np.random.normal(0, 2, size)
    )

    df = pd.DataFrame({
        "hours": hours,
        "attendance": attendance,
        "previous": previous,
        "score": score
    })

    os.makedirs("../data", exist_ok=True)
    df.to_csv("../data/dataset.csv", index=False)

    print(" Dataset generated!")

if __name__ == "__main__":
    generate_dataset()
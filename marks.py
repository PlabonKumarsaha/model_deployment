import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def marks_prediction(marks):
    marks = int(marks)
    print(marks)
    x = pd.read_csv('LinearX.csv')
    # print(x)
    y = pd.read_csv('LinearY.csv')
    X = x.values
    Y = y.values

    model = LinearRegression()
    model.fit(X, y)

    x_test = np.array(marks)
    x_test = x_test.reshape((1, -1))
    print("OK"+model.predict(x_test))

    return model.predict(x_test)



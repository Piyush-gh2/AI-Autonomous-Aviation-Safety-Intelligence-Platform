from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_aviation_risk(df):

    df["t"] = range(1, len(df)+1)

    X = df[["t"]]
    y = df["engine_temp"]

    model = LinearRegression()
    model.fit(X, y)

    next_flight = np.array([[len(df)+1]])

    prediction = model.predict(next_flight)

    return prediction[0]
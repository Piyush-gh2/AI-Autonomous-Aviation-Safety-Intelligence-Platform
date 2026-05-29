from src.loader import load_data
from src.forecasting import forecast_aviation_risk
from src.aviation_engine import detect_aviation_risk
from src.explainable_ai import explain_risk

def run_aviation_ai():

    df = load_data()

    prediction = forecast_aviation_risk(df)

    latest_engine = df["engine_temp"].iloc[-1]
    latest_weather = df["weather_severity"].iloc[-1]
    latest_delay = df["delay_minutes"].iloc[-1]

    risk = detect_aviation_risk(
        latest_engine,
        latest_weather,
        latest_delay
    )

    explanation = explain_risk(
        latest_engine,
        latest_weather
    )

    return df, prediction, risk, explanation
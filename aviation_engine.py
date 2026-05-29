def detect_aviation_risk(engine_temp, weather, delay):

    if engine_temp > 90:
        return "High Aviation Risk"

    elif weather > 85:
        return "Severe Weather Warning"

    elif delay > 100:
        return "Operational Disruption Alert"

    else:
        return "Flight Operations Stable"
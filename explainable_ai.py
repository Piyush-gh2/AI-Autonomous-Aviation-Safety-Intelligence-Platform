def explain_risk(engine_temp, weather):

    if engine_temp > 90:
        return "Safety alert generated due to abnormal engine temperature."

    elif weather > 85:
        return "Safety alert generated due to severe weather conditions."

    else:
        return "Aviation operational conditions remain stable."
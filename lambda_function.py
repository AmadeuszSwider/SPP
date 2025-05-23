import math
import json

def lambda_handler(event, context):
    sensor_id = event.get("sensor_id")
    R = event.get("value")
    
    if R < 1 or R > 20000:
        return {"error": "VALUE OUT OF RANGE"}

    a = 1.40e-3
    b = 2.37e-4
    c = 9.90e-8

    lnR = math.log(R)
    inv_T = a + b * lnR + c * (lnR ** 3)
    T = 1 / inv_T - 273.15  # Kelviny -> Celsjusze

    return {
        "sensor_id": sensor_id,
        "temperature": round(T, 2)
    }

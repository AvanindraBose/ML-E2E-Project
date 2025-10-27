import joblib
import pandas as pd
from app.cache.redis_cache import set_cached_prediction,get_cached_prediction
from app.core.config import settings

model = joblib.load(settings.MODEL_PATH)

def predict_car_price(data:dict):
    cached_key = " ".join([str(val) for val in data.values()])
    cached_value = get_cached_prediction(cached_key)
    if cached_value:
        return cached_value
    
    converted_data = pd.DataFrame([data])
    prediction = model.predict(converted_data)[0]
    set_cached_prediction(cached_key,prediction)
    return prediction
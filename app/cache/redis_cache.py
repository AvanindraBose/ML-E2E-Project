import json
from redis import Redis
from app.core.config import settings

redis_client = Redis.from_url(settings.REDIS_URL)

def get_cached_prediction(key:str):
    value = redis_client.get(key)
    if value :
        return json.loads(value)
    return None

def set_cached_prediction(key:str,data:dict,exp:int=3600):
    redis_client.setex(key,exp,json.dumps(data))

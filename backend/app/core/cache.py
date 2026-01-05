import json
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def get_cache(key: str):
    value = redis_client.get(key)
    return json.loads(value) if value else None


def set_cache(key: str, value, ttl: int = 60):
    redis_client.setex(key, ttl, json.dumps(value))

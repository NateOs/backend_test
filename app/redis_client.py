import redis
import os

REDIS_URL = os.getenv("REDIS_URL")

# Create a Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
import redis

# Create a Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
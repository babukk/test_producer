import redis

redis_url = 'redis://localhost:6379/1'
conn = redis.from_url(redis_url)

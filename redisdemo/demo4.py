import redis

pool = redis.ConnectionPool(host='localhost', port=6380, db=0)
# (decode_responses=True)

redis = redis.Redis(connection_pool=pool)

pipe = redis.pipeline(transaction=True)
pipe.multi()

pipe.set('name', 'xxxxiaoming')
# error
pipe.set('role', 'st')

pipe.execute()

print(redis.get('role'))
print(redis.get('name'))

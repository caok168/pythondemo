import redis

pool = redis.ConnectionPool(host='localhost', port=6380, db=0)
# (decode_responses=True)

redis = redis.Redis(connection_pool=pool, health_check_interval=30)

redis.set('age', 2)  # set:有则覆盖
print(redis.get('age'))

redis.set('name', 'hehe', 10)

redis.setnx('name', 'lala')
print(redis.get('name'))

# redis.mset(k1='v2', k2='v3')
# print(redis.get('k1'))

redis.incr('age', 3)
print(redis.get('age'))

print(type(redis.get('age').decode()))

redis.delete('age')
redis.flushall()

ret = redis.getset('k1', 'vvv2')
print(ret)
print(redis.get('k1'))

print(redis.getrange('name', 1, 3))

redis.setrange('name', 2, 'll')
print(redis.get('name'))

redis.append('name', 'aaaa')
print(redis.get('name'))

# get
ret = redis.get('name')
print(ret)

print(redis.mget('k1', 'k2', 'name'))

print(redis.strlen('name'))

print(redis.get('name').decode('utf-8'))

print(redis.keys())

print(redis.keys('shoppingcar_1*'))
print(redis.mget('k1', 'k2', 'name', 'age'))

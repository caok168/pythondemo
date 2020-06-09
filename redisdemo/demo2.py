from datetime import time

import redis

pool = redis.ConnectionPool(host='localhost', port=6380, db=0)
# (decode_responses=True)

redis = redis.Redis(connection_pool=pool)

redis.hset('info', 'tel', '120')
redis.hmset('zhangsan', {'tel':110, 'addr':'beijing'})
redis.hmset('zhangsan', {'hobby': 'nicai', 'sex': 'men', 'addr': 'hebei'})

# delete
print(redis.hdel('zhangsan', 'tel'))
redis.delete('aaaa')
redis.delete('k1', 'k2')

# change
redis.hmset('zhangsan', {'hobby': 'nicai', 'sex': 'men', 'addr': 'hebei'})

# get
print(redis.hget('info', 'tel'))
print(redis.hmget('zhangsan', ['tel', 'sex', 'addr']))
print(redis.hgetall('shopping_car_1_3'))
print(redis.hlen('zhangsan'))
print(redis.hkeys('zhangsan'))
print(redis.hvals('zhangsan'))
print(redis.hexists('zhangsan', 'tel'))
print(redis.exists('zhangsan'))
for item in redis.hscan_iter('zhangsan'):
    print(item)

redis.hmset('k3', {'tel': 110, 'addr': 'beijing'})
print(redis.hgetall('k3'))

redis.expire('k3', 5)

time.sleep(3)
print(redis.hgetall('k3'))
time.sleep(3)
print(redis.hgetall('k3'))

import redis

pool = redis.ConnectionPool(host='localhost', port=6380, db=0)
# (decode_responses=True)

redis = redis.Redis(connection_pool=pool)

# add
redis.lpush('students', 'zhangsan', 'lisi', 'wangmazi')
redis.rpush('class', '1ban', '2ban', '3ban')
redis.linsert('students', 'BEFORE', 'lisi', 'hehe')
redis.lpush('class', '1ban', '1ban')
print(redis.lrange('class', 0, redis.llen('class')))

# delete
# redis.lrem('class', '1ban', num=2)
print(redis.lpop('class'))
redis.ltrim('class', 1, 4)

# change
redis.lset('students', 1, 'xiaoming')
print(redis.lrange('students', 0, 3))

# get
print(redis.llen('students'))
print(redis.lrange('students', 0, 4))
print(redis.lrange('class', 0, redis.llen('class')-1))
print(redis.lindex('class', 1))
from redis.cluster import RedisCluster as Redis
import json
import time
from redis.commands.json.path import Path
from redis.cluster import ClusterNode
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

# Подключение к Redis
redis = Redis(host='localhost', port=7000, decode_responses=True)

start_time = time.time()

keys = redis.keys('*')
for key in keys:
    type = redis.type(key)
    if type == "string":
        print("error")
        val = redis.get(key)
    if type == "hash":
        vals = redis.hgetall(key)
    if type == "zset":
        print("error")
        vals = redis.zrange(key, 0, -1)
    if type == "list":
        print("error")
        vals = redis.lrange(key, 0, -1)
        

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения чтения для типа {redis.type(key)}: {execution_time} секунд")

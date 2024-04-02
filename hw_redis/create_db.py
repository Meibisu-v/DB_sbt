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
rc = Redis(host='localhost', port=7000, decode_responses=True)



# Функция для импорта данных из файла в Redis
def import_data_from_file(filename, data_type):
    with open(filename, 'r') as file:
        data = json.load(file)
        if data_type == 'string':
            for key, value in data.items():
                rc.set(key, json.dumps(value))
        elif data_type == 'hash':
            for key, value in data.items():
                rc.hset(key, mapping=value)
            
        elif data_type == 'zset':
            for key, value in data.items():
                rc.zadd(key, value)
        elif data_type == 'list':
            for key, value in data.items():
                rc.lpush(key, *value)
        print(f"Данные из файла {filename} импортированы в Redis в структуру {data_type}")

import sys
arguments = sys.argv
rc.flushall()
# Импорт данных из каждого файла в Redis
start_time = time.time()
if arguments[1] == "string":
    import_data_from_file('large_string_data.json', 'string')
elif arguments[1] == "hash":
    import_data_from_file('large_mset_data.json', 'hash')
elif arguments[1] == "zset":
    import_data_from_file('large_zset_data.json', 'zset')
elif arguments[1] == "list":
    import_data_from_file('large_list_data.json', 'list')
else:
    print("error")  

end_time = time.time()
execution_time = end_time - start_time

print(f"Время выполнения кода: {execution_time} секунд")
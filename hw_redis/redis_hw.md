# Установка Redis
Вначале установим необходимые зависимости

```bash
sudo apt-get update
sudo apt install make gcc libc6-dev tcl build-essential
```

Скачиваем архив

![alt text](images_redis/image_2024-03-26_11-22-51.png)

Скомпилируем скачанные файлы:

```
tar -xzvf redis-stable.tar.gz
cd redis-stable
```

Установка зависимостей для сборки Redis.

```
cd redis-stable/deps
make hiredis lua jemalloc linenoise
```

![alt text](images_redis/image_2024-03-26_11-23-22.png)

Запустим тесты

```bash
cd ~/redis-stable
make
```

![alt text](images_redis/image_2024-03-26_11-32-49.png)

### Создание кластера

```bash
mkdir cluster-test
cd cluster-test
mkdir 7000 7001 7002 7003 7004 7005 
```

В каждой папке создадим конфигурационный файл вида:

```bash
port <port number>
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
```

В каждой папке запустим `redis-server ./redis.conf`

![alt text](images_redis/image-2.png)

После того, как все ноды запущены создадим кластер:

 `redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 \
127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 \
--cluster-replicas 1`

![alt text](images_redis/image-3.png)

Проверим ноды:

![alt text](images_redis/image-8.png)

### Заполнение БД

4 json файла для заполнения БД:

![alt text](images_redis/image-4.png)

Для заполнения бд я использовала скрипт create_db.py и read_from_db.py для чтения.
Скорость заполнения/чтения для разных сруктур:

#### строка

![alt text](images_redis/image-5.png)

![alt text](images_redis/image-6.png)

Перед заполнением бд очистим ее: `rc.flushall()`

#### hset 

![alt text](images_redis/image-13.png)

#### zset

![alt text](images_redis/image-11.png)

#### list

![alt text](images_redis/image-12.png)
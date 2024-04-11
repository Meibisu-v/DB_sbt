## Установка CouchDB
Задание выполнено в ОС Windows 

Установка выполнена как указано на оф. сайте:
![alt text](images/image.png)

## Создание БД

![alt text](images/image_2024-04-08_19-59-29.png)

![alt text](images/image-1.png)

Создаем БД в CouchDB`test-db`

![alt text](images/image-2.png)

Добавляем в БД один документ в котором должно быть поле «name».

![alt text](images/image_2024-04-11_16-16-29-1.png)

Прописываем в ДЗ_2.html путь к инсталляции CouchDB:
`Remote: new PouchDB('http://localhost:5984/test-db')`

Настраиваем CORS:

![alt text](images/image_2024-04-08_20-42-44.png)

Настраиваем permissions:

![alt text](images/image-3.png)

Запускаем PouchDB_hw.html и нажимаем кнопку «sync». 

![alt text](images/image-4.png)

Останавливаем CouchDB: `net.exe stop "apache couchdb"`

![alt text](images/image-5.png)

Обновляем PouchDB_hw.html и в нем по прежнему отображается фамилия.
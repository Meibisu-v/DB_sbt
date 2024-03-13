# Отчет по выполнению ДЗ 1: Работа с MongoDB 

## Шаги выполнения
 
### Установка
Установка происходила в WSL Ubuntu 22.
```bash
sudo apt update
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt-get update
```
Проверяем установленную версию
![alt text](img/image_2024-03-10_21-50-44.png)
Запускаем монго и проверяем, что он запущен
```bash
ps -e | grep 'mongod'
```
![alt text](img/image_2024-03-10_21-50-28.png)

### Создание бд
Я выбрала датасет: [Titanic dataset](https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html).

Импортирую файл в базу данных
![alt text](img/image-4.png)

### Выполнение CRUD запросов
Вставка и проверка наличия нового элемента в бд
![alt text](img/image_2024-03-12_13-11-01.png)
![alt text](img/image_2024-03-12_13-17-55.png)
Update запрос и проверка результатов
![alt text](img/image_2024-03-12_13-19-29.png)
Delete запрос и проверка, что элемент удален.

![alt text](img/image_2024-03-12_13-19-59.png)

### Запросы с агрегацией 
Выяснить средний возраст выживших пассажиров по каждому классу:
![alt text](img/image_2024-03-12_13-29-08.png)

Найти количество пассажиров мужского и женского пола в каждом классе:
![alt text](img/image_2024-03-12_13-29-42.png)

### Сравнение производительности запросов выборки

Т.к. датасет титаника оказался слишком маленьким для наглядных результатов по времени выполнения запроса я скачала [Fake News Detection Dataset](https://www.kaggle.com/c/fake-news/data)
![alt text](img/image.png)
Производительность при find запросе без индексов
![alt text](img/image-1.png)
Создаем индекс по полю "label" и снова делаем find запрос:
![alt text](img/image-2.png)
Производительность при find запросе с индексами
![alt text](img/image-3.png)

Получили, что время выполнения запроса (ExecutionTimeMillis) уменьшилось с 51 до 13, mongodb просканировал почти в два раза меньше документов 
# Questions Collector

---
## Зависимости и используемые библиотеки:

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker / docker-compose

### Запуск
Перед запуском скопировать и при необходимости отредактировать настройки базы данных:

```
cp sample.env .env
```

#### Запуск образа
```
docker-compose up --build
```

**Сервис работает по адресу: [127.0.0.1:80](http://127.0.0.1:80)**

### Запросы к сервису
1. С помощью Swagger по адресу [127.0.0.1/docs](http://127.0.0.1/docs)
2. В терминале:<br>
```
curl -X 'POST' \
  'http://localhost/questions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 3
}'
```
3. Python код для работы с API:
```python
import requests
import json


url = 'http://localhost/questions'

payload = json.dumps({
  'questions_num': 3
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)

print(response.json())

```

---
1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.
2. Реализовать на Python3 веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:
   - В сервисе должно быть реализован POST REST метод, принимающий на
   вход запросы с содержимым вида {"questions_num": integer}.
   - После получения запроса сервис, в свою очередь, запрашивает с
   публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
   - Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
   - Ответом на запрос из п.2 должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.
  
3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.
4. Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAalchemy, пользоваться аннотацией типов.
---
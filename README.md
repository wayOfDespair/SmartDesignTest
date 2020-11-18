# SmartDesignTest

Написано с помощью FastApi, используется один эндпоинт для гет и пост запроса. Запускается с помощью uvicorn

# Установка и запуск
```
pip3 install -r requirements.txt
python app.py
```

# Запустить тесты
```cmd
pip3 install pytest
pytest
```

# Curl команды для тестовых сценариев

###### 1. Создать товар
```
curl --location --request POST 'http://127.0.0.1:8080/items' --header 'Content-Type: application/json' \
--data-raw '{
    "name": "iPhone 12",
    "description": "Brand new iPhone",
    "params": [
        {"price": "$999"},
        {"color": "black"}
    ]
}'
```
###### 2. Получить список товаров
```
curl --location --request GET 'http://127.0.0.1:8080/items' --header 'Content-Type: application/json' \
--data-raw '{}'
```
###### 3. Найти товар по параметру

```
curl --location --request GET 'http://127.0.0.1:8080/items' \
--header 'Content-Type: application/json' \
--data-raw '{
    "params.имя_параметра": значение
}'
```


###### 4. Получить информацию о товаре по `item_id`
```
curl --location --request GET 'http://127.0.0.1:8080/items'  --header 'Content-Type: application/json' \
--data-raw '{
    "item_id": значение
}'
```

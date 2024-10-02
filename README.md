# Flask Healthcheck App

Цей проект є базовим Flask-застосунком з ендпоінтом `/healthcheck`, який повертає JSON-відповідь з поточною датою та статусом сервісу.

## Вимоги

Перед тим як почати, переконайтеся, що у вас встановлені:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Запуск застосунку

```bash
flask --app app run --host 0.0.0.0 --port 5000
```

## Запуск за допомогою Docker

1. Створення Docker-образу
    ```bash
    docker build . -t flask-app:latest
    ```

2. Запуск контейнера
    ```bash
    docker run -it --rm -p 5000:5000 -e PORT=5000 flask-app:latest
    ```
   
## Запуск за допомогою Docker Compose

```bash
docker-compose up --build
```

## Перевірка роботи застосунку

Перейдіть за посиланням
[http://localhost:5000/healthcheck](http://localhost:5000/healthcheck) 
для перевірки роботи застосунку.

Або ж через команду `curl`:
```bash
curl http://localhost:5000/healthcheck
```
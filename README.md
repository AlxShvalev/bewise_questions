# Bewise questions

Сервис для получения и хранения вопросов для викторины.
По запросу клиента сервис отправляет запрос на удаленный сервер 
и возвращает клиенту случайные вопросы для викторины в количестве, 
запрошенном клиентом.

Все полученные вопросы сервис сохраняет в собственную базу данных.
Дубликаты вопросов исключаются сервисом. 
___
## Установка и запуск
- Скачать и установить [Docker](https://docs.docker.com/get-docker/)
- Клонировать репозиторий 
```bash
git clone git@github.com:AlxShvalev/bewise_questions.git
```
- В директории проекта заполнить файл `.env.example` необходимыми данными и переименовать в `.env`
- Из директории проекта выполнить команду 
```bash
docker-compose up -d --build
```
- Для остановки сервиса из директории проекта выполнить команду
```bash
docker-compose down
```
___
## Документация
Сервис реализует единствнный эндпоинт
- `POST /questions` - запрос необходимого количества вопросов для викторины

В теле запроса необходимо передать требуемое количество вопросов следующим способом:
```json
{
  "questions_num": 5
}
```
___
## Использованные технологии
- Python 3.10
- FastAPI 0.95
- Pydantic 1.10
- SQLalchemy 2.0.9
- PostgreSQL
- Docker
___
### Автор
Алексей Швалев
# 🚀 Sempai Anime

Этот проект представляет собой мой аналог [Anime GO](https://animego.club/) (сайт на котором можно посмотреть аниме и почитать мангу).

## 🤔 Как пользоваться?

1. Клонируем репозиторий
```
git clone https://github.com/DaniilZubkov/Sempai_anime.git
```
3. Создаем миграции
```
python manage.py makemigrations
```
4. Применяем миграции
```
python manage.py migrate
```
5. Регистрируем себя как superuser
```
python manage.py createsuperuser
```
6. Заходим в админ-панель и добавляем нужные модели
```
127.0.0.1:8000/admin/
```
7. Готово! Можно пользоваться проектом и смотреть аниме или читать мангу.

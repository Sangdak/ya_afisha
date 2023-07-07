# ya_afisha

Развлекательный сайт представляющий всем желающим возможность ознакомиться с интересными местами в г. Москва.

## Алгоритм запуска и использования проекта

[python3.10, git, pyenv и poetry должны быть предварительно установлены на компьютере]
- Скопируйте код проекта из репозитория:
```shell
git clone <ссылка на репозиторий>
```
- В скачанной директории с помощью командной строки запустите (установка зависимостей):
```shell
poetry install
. . .
poetry shell
```
- В директории 'where_to_go/where_to_go' рядом с файлом 'settings.py' создайте файл '.env' со следующим содержимым:
```
SECRET_KEY=<Секретный ключ проекта Django>
DEBUG=<True, если есть необходимость получать более подробную информацию по отладке>
ALLOWED_HOSTS=<разрешённые адреса, см. подробнее в фициальной документации Django: https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts>
```
- Создайте файлы миграции для базы данных, примените их и, следуя подсказкам, создайте супер-юзера: 
```shell
python manage.py makemigrations
. . .
python manage.py migrate
. . .
python manage.py createsuperuser
```
- Запустите проект на локальном сервере:
```
python manage.py runserver
```
- По адресу http://127.0.0.1:8000/ в вашем браузере откроется страница проекта
- Вносить изменения и добавлять новые объекты можно через адми-панель по адресу: http://127.0.0.1:8000/admin , для входа используйте данные супер-юзера, созданного ранее.

## Цели проекта

Данный код написан в обучающих целях - это урок в курсе по Python и веб-разработке от [Devman](https://dvmn.org/).

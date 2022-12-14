# Сервис уведомлений

Cервис управления рассылками API администрирования и получения статистики.

Разработан на python совместно с:
* Django REST framefork для построения Web Api.
* Celery и Redis для асинхронной отправки сообщений и статистики. 

## Установка и запуск

1. Клонировать репозиторий с Github.com:
````
git clone https://github.com/Povarenskiy/notification_service.git
````
2. В файле .evn заполнить необходимые данные
```
TOKEN = 'your token' - для авторизации на внешнем сервисе 
EMAIL= ['email1', 'email2',] - почтовые ящики для ежедневной отправки статистики 
```
3. Запуск docker-compose
````
docker-compose up -d
````
4. Создание администратора
````
docker-compose run web python manage.py createsuperuser
````
## Панель администратора
````
http://127.0.0.1:8000/admin/
````
## Тесты
````
docker-compose run web python manage.py test mailing_app
````
## Api

````http://127.0.0.1:8000/api/```` - api проекта

````http://127.0.0.1:8000/api/client/```` - клиенты

````http://127.0.0.1:8000/api/mailing/```` - рассылки 

````http://127.0.0.1:8000/api/mailing/<pk>/stat/```` - детальная статистика по конкретной рассылке  

````http://127.0.0.1:8000/api/mailing/fullstat/```` - общая статистика по созданным рассылкам с группировкой по статусам

````http://127.0.0.1:8000/api/message/```` - сообщения 

## Описание функционала

### Реализована следующая логика рассылки:

- После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания - должны быть выбраны из справочника все клиенты, которые подходят под значения фильтра, указанного в этой рассылке и запущена отправка для всех этих клиентов.
- Если создаётся рассылка с временем старта в будущем - отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.
- По ходу отправки сообщений должна собираться статистика (см. описание сущности "сообщение" выше) по каждому сообщению для последующего формирования отчётов.
- Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Необходимо реализовать корректную обработку подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.

### Дополнительно 

1.	Организованно тестирование кода;
2.	Подготовлен docker-compose для запуска всех сервисов проекта одной командой;
3.	Организована обработка ошибок и откладывание запросов при неуспехе для последующей повторной отправки; 
4.	Обеспечено подробное логирование на всех этапах обработки запросов, создания/редактирования сущностей таблиц;
5.	Сервис раз в сутки отправляет статистику по обработанным рассылкам на email.


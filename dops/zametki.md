# 3_django_bank

### Quit the server with CTRL-BREAK.

    python manage.py runserver

### START
    python -m venv venv
    .\venv\Scripts\activate
    pip install django
    cd .\maze_bank\
    python manage.py runserver

### venv !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    .\venv\Scripts\activate
    cd .\maze_bank\
    python manage.py runserver

### Различные команды
    python -m venv venv
    .\venv\Scripts\activate
    
    pip list
    django-admin list

### Работа с БД

    python3 manage.py makemigrations
    python3 manage.py migrate

###### Необходимо выполнять команды выше каждый раз, когда вы меняете модели таким образом, что структура таблицы изменится(включая добавления и удаления как отдельных полей, так и целых моделей).
#### CRUD - основы работы с моделями
* Create - создание;
* Read - чтение;
* Update - изменение;
* Delete - удаление;
##### У нас ORM фреймворка DJANGO

    python manage.py sqlmigrate mazebank 0001
    python manage.py migrate

##### импорт в бд
    python manage.py shell
    from mazebank.models import Bank 
новая запись в бд

    Bank(title='Павел Тестер', money_balance='10000')
    Bank(title='Павел Тестер')
    b1 = _ 
    b1
    b1.save()
    b1
всякое

    b1.id
    b1.title
    b1.pk  

pk - индификатор записи 
# objects

    Bank.objects

# починка
    
    python manage.py makemigrations
    python manage.py migrate
# python-test-Generect

## Частина перша.

Використовувався python версії 3.10.0

### Запуск

Перейти в папку проекту (з консолі чи терміналу), далі

```bash
python test_data_parser.py
```

В результаті виконається парсинг тестових даних (з методу _get_test_json)

![alt text](https://github.com/loievskyi/python-test-Generect/blob/master/screens/test-data-parser-result.png)

## Частина друга.

Використовувався Python 3.10.0, Django версії 3.2.9 та djangorestframework 3.12.4.
Перед початком рекомендується встановити та запустити віртуальне середовище.

```bash
python -m pip install virtualenv
python -m virtualenv venv

# для Windows:
venv\Script\activate


# для Linux:
source venv/bin/activate
```

Далі потрібно перейти з терміналу (чи консолі) в папку проекту.
Далі встановити всі необхідні пакети:

```bash
python -m pip install -r requirements.txt
```

Перейти в папку generect_api та зробити базові налаштування:

```bash
cd generect_api
python manage.py migrate
python manage.py compilemessages # має бути встановлений gnu_gettext
```

Створення облікового запису адміну:

```bash
python manage.py createsuperuser
```

Для запуску сервера:

```bash
python manage.py runserver
```

Далі за допомогою веб-браузеру перейти за адресою http://localhost:8000/admin,
да за допомогою інтерфейсу адміністратора заповнити базу тестовими даними.

![alt text](https://github.com/loievskyi/python-test-Generect/blob/master/screens/admin_1.png)

![alt text](https://github.com/loievskyi/python-test-Generect/blob/master/screens/admin_2.png)

### Команда для генерації тестових даних

Також для генерації тестових даних можна використати management-команду:

```bash
python manage.py generate_test_data
```

![alt text](https://github.com/loievskyi/python-test-Generect/blob/master/screens/generate-test-data.png)

При виконанні цієї команди має створитися 10 об'єктів Company та 100 об'єктів Person

## Перегляд даних

### Список компаній

Список компаній доступний за адресою http://localhost:8000/api/companies/

![alt text](https://github.com/loievskyi/python-test-Generect/blob/master/screens/company-list.png)

### Детальна інформація про компанію

Детальна інформація про компанію доступна за адресою http://localhost:8000/api/companies/\<id\>/

![alt text](https://github.com/loievskyi/python-test-Generect/blob/master/screens/company-detail.png)

### Список працівників компанії

Список працівників компанії доступний за адресою http://localhost:8000/api/v1/persons/?company_id=<company_id>

![alt text](https://github.com/loievskyi/python-test-Generect/blob/master/screens/person-list-for-company.png)

### Детальна інформація про співробітника

Детальна інформація про співробітника доступна за адресою http://localhost:8000/api/v1/persons/\<id\>/

![alt text](https://github.com/loievskyi/python-test-Generect/blob/master/screens/person-detail.png)

### Парсинг даних з API

Перейти в папку проекту (з консолі чи терміналу), далі

```bash
python api_data_parser.py
```

Команду необхідно виконувати при запущеному сервері, що "віддає" API
В результаті виконається парсинг тестових даних (з API)

![alt text](https://github.com/loievskyi/python-test-Generect/blob/master/screens/api-data-parser-result.png)

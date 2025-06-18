# Port_checker
Скрипт для отображения занятых портов 


Требования:

- Python 3.10+
- Библиотека psutil.

1.  Установить библиотеку:

    ```bash
    pip install psutil
    ```

2. Запуск:

    ```bash
    python portchecker.py
    ```


## Пример вывода

```
Занятые порты и информация о процессах:
Порт: 80, PID: 1234, Процесс: httpd, Статус: running
Порт: 443, PID: 1235, Процесс: httpd, Статус: running
Порт: 3306, PID: 4567, Процесс: mysqld, Статус: sleeping
Порт: 5432, PID: 5678, Процесс: postgres, Статус: sleeping
Порт: 8000, PID: 9101, Процесс: python, Статус: running
Порт: 6379, PID: 1112, Процесс: redis-server, Статус: sleeping
```

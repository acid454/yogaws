### commands
python3 manage.py runserver
http://127.0.0.1:8000/


### ToDo: реализовать дескрипторы
  https://realpython.com/python-getter-setter/
  https://docs.python.org/3/howto/descriptor.html

### MVT

-- Model: данные для асан, сетов и ** тренировок **.
          Тут лежат трениеровки со всеми значениями (последовательность асан/сетов, время фиксации etc). Для каждого пользователя своя. json-файлы.


-- View: представление
          python-классы, выстраивающие тренировку на базе модели

----------------------------------------
Base asana:
- caption
- tasks
- properties

Property:
- type ("int", "string")
- caption
- default
- value
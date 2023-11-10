### commands
python3 manage.py runserver
http://127.0.0.1:8000/


### ToDo: aftermath callback, чтобы отработать озвучку {% if not glob.get('last_before_shavasana') %}

### ToDo: реализовать дескрипторы
  https://realpython.com/python-getter-setter/
  https://docs.python.org/3/howto/descriptor.html

### MVT

-- Model: данные для асан, сетов и ** тренировок **.
          Тут лежат трениеровки со всеми значениями (последовательность асан/сетов, время фиксации etc). Для каждого пользователя своя. json-файлы.


-- View: представление
          python-классы, выстраивающие тренировку на базе модели

--------------------------------------------
VSCode:
**- Shift+Tab - unintend multiple lines -**

Python:
-- https://tproger.ru/translations/asterisks-in-python-what-they-are-and-how-to-use-them
--  # Singleton class for speech manager, see
    #  https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
    #  The new method is a static method that belongs to the class itself.
    #  It's responsible for creating and returning a new instance of the class.


-- List generators + f-strings:
images=[f"most{x}" for x in range(7)]

-- Slice list to copy:
name_pool = self.tasks[0].pool("name")[:]

JavaScript:
=== - оператор строгого равенства
let - Variables declared by let are only available inside the block where they're defined

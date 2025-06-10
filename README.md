### commands
python3 manage.py runserver
http://127.0.0.1:8000/

sessionStorage.removeItem('background_img_id')

!!! нет подъема вверх в медленной сурье
!!! увеличить шрифт на успешном завершении
!!! капотасана и горка после - звук паузы
!!! не передавать can_be_empty, или вообще весь snd_pools
!!! скорпион смена ног
!!! использовать переход навасана-стол
!!! переход стол-планка на боку
!!! убрать properties из active.html


!!! как это работает?:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ToDo: aftermath callback, чтобы отработать озвучку {% if not glob.get('last_before_shavasana') %}
### ToDo: async io для загрузки mp3

### ToDo: реализовать дескрипторы
  https://realpython.com/python-getter-setter/
  https://docs.python.org/3/howto/descriptor.html

### MVT

-- Model: данные для асан, сетов и ** тренировок **.
          Тут лежат трениеровки со всеми значениями (последовательность асан/сетов, время фиксации etc). Для каждого пользователя своя. json-файлы.


-- View: представление
          python-классы, выстраивающие тренировку на базе модели



### added new field (migration):
python manage.py makemigrations  
python manage.py migrate

acid454@yoga7:~/workspace/yogaws$ rm ./db.sqlite3 
acid454@yoga7:~/workspace/yogaws$ python3 manage.py migrate  --run-syncdb

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



-- Bootstrap is a web framework built to help you design responsive websites faster. It contains a ton of custom css/javascript and jquery code that you can use to style and layout your website.


-----------------------------------------------------------
INSTALL on Debian:
PiP: sudo apt install python3-pip
sudo apt install python3-django
sudo apt install python3-django-crispy-forms
sudo apt-get install python3-mutagen

--------------------------------------------------------------------
https://timeweb.com/ru/services/hosting/

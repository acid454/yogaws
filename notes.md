### commands
python3 manage.py runserver
http://127.0.0.1:8000/



sessionStorage.removeItem('background_img_id')


*** нет озвученного имени для джатхара паривартанасаны
*** добавить скрины капотасаны вниз
*** нет изображений для планки с поднятой ногой

!!! нет подъема вверх в медленной сурье
!!! увеличить шрифт на успешном завершении
!!! капотасана и горка после - звук паузы
!!! не передавать can_be_empty, или вообще весь snd_pools
!!! скорпион смена ног
!!! использовать переход навасана-стол
!!! переход стол-планка на боку
!!! убрать properties из active.html



!!! проверить установку свойств
class MarkatasanaWithLegs(Markatasana):
     def __init__(self, **kwargs):
-        super().__init__(*kwargs)
+        super().__init__()
         self.cycles_count.caption = "циклов коленей"
         self.properties.append(IntProperty(caption="ноги перед собой", short="tm_legs", default=5))
         self.properties.append(IntProperty(caption="циклов скруток", short="cycles_twist", default=3))

!!! как это работает?:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

!!! красивый код (@login_required):
https://stackoverflow.com/questions/48949022/django-filewrapper-memory-error-serving-big-files-how-to-stream

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


### wav conversion:
ffmpeg -i ./tick2.wav -ar 44100 -ac 1 ./tick2-44100.wav


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

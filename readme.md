# **ШАГ 1**

Клонируем себе репозиторий.
Открываем docker, заходим в папку python_web_service.

Запускаем команду в терминале:
$ docker-compose up --build

Построили и открыли контейнер. Должен был образоваться локальный хост: http://localhost:5000/

Далее работаем с моим веб-сервисом.

# **ШАГ 2**

В файле app.py под #GET request прописан шаблон функции общего вида "action". Пример его использования находится ниже. 
Там я привел простой пример возведения в квадрат некого числа.

Чтобы посмотреть на работу GET запроса  действии, нужно у себя в браузере вбить: http://localhost:5000/square/num, где num - любое число.
Возвратится ответ, текущее время и статус код (200 - ОК).

# **ШАГ 3**

Далее в файле app.py находится функция post для #POST request.
Есть два способа отправить запрос:
1. Используя curl
 
Для этого в терминале нужно вбить следующее:
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{'key': 'values'}' \
  http://localhost:5000/post
  
Здесь data - данные, которые мы хотим, чтобы наш сервис обработал.
на выходе мы получим эти данные в json + uuid (случайное число).

2. С помощью Postman

В этой программе нужно сделать POST запрос через адрес http://localhost:5000/post.
В Headers в Key добавить Content-Type, а в Value - application/json. Далее в Body нужно поставить галочку в поле "raw", 
в поле ниже вбить нужные данные.


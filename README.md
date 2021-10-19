Запуск проекта.
 - Скопировать проект с помощью ``` git clone https://github.com/iNgredie/flights.git ```
 - ```docker-compose up --build ```  собрать приложение и сделать его первоначальный запуск
 - ```docker-compose down -v``` – остановить работу приложения
 - ```docker-compose run web python manage.py migrate``` – сделать необходимые миграции
 - ```docker-compose up``` – окончательно запустить приложение.


Создать файл .env
Скопировать туда содержимое из .env.example.  
Добавить из https://opensky-network.org/  
USERNAME=   
PASSWORD=


 - ```docker-compose run web python manage.py parse_flights``` – спарсить полеты за последний месяц
 - ``` http://localhost:8000/flights``` Получение всех рейсов за последний месяц    

## Программа для учета количества кликов по ссылке


#### Программа предназначена для учета количества перехода по сокращенным ссылкам. Использует API bit.ly
В зависимости от полученной на вход ссылки может или вывести ее укороченную версию, или вывести количество переходов по укороченной версии ссылки

Для работы необходимо: python3.9, git, файл .env c содержанием:  

*BITLY_TOKEN = "Your_bitly_token"* в папке со скриптом main.py

Как получить токен bitly? 

- https://app.bitly.com - зарегистрироваться
- https://dev.bitly.com - прочитать

1) Для запуска необходимо клонировать этот репозиторий себе на компьютер, используя команду  
*git clone git@github.com:IlyaG96/Dewman_API_2_BITLY.git*

2) Измените директорию на рабочую *"cd Dewman_API_2_BITLY"*

3) Создайте новое виртуальное окружение *"python3.9 -m venv env" в папке 'env'*

4) Активируйте виртуальное окружение *"source env/bin/activate"*

5) Установите все необходимые пакеты командой *"pip install -r requirements.txt"* 

6) Создайте файл .env командой *vim .env*, пример его содержания приведен выше

7) По умолчанию программа принимает аргументы из терминала. Попробуйте, например:
*"python main.py https://google.com"*  
скрипт вернет: Here is your shorten link: bit.ly/3mFwWQ2  
*"python main.py bit.ly/3mFwWQ2"*  
скрипт вернет: Number of clicks: 1  

8) Улыбнитесь. Вас снимает веб-камера вашего ноутбука. Или не снимает. Но это еще больший повод для улыбки :)

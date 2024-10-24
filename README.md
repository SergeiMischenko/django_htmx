<h1 align="center">Django_HTMX</h1>

В рамках данного проекта было создано простое CRUD-приложение на Django с использованием HTMX. Приложение демонстрирует, как можно интегрировать HTMX в Django для работы с серверной частью, предоставляя интерактивный пользовательский интерфейс без необходимости писать JavaScript.

Цель проекта — продемонстрировать базовые возможности работы с HTMX и показать, как создавать функциональные и отзывчивые веб-страницы, используя автономные шаблоны и обработку запросов через Django.
___

<h2 align="center">Установка</h2>

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/SergeiMischenko/django_htmx.git
    ```

2. **Перейдите в папку проекта:**
    ```bash
    cd django_htmx
    ```

3. **Установите виртуальное окружение и активируйте его:**
    ```bash
    python -m venv env
    source env/bin/activate   # Для Linux и macOS
    env\Scripts\activate      # Для Windows
    ```

4. **Установите необходимые зависимости:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Откройте файл .env и заполнить его своими данными**
    ```env
    SECRET_KEY = 'your-secret-key'
    ```

6. **Выполните миграции базы данных:**
    ```bash
    python manage.py migrate
    ```

7. **Запустите сервер разработки:**
    ```bash
    python manage.py runserver
    ```
   
8. **Установка с помощью Docker**
    ```bash
    docker build --tag django_books:latest .
    docker run --name django_books -d -p 8000:8000 django_books:latest
    ```

9. **Доступ к приложению:**

   После завершения всех вышеуказанных шагов, приложение будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

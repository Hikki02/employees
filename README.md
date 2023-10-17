# Проект "Employees" с использованием Docker Compose

## Установка и Запуск

1. Клонируйте репозиторий с проектом:

    ```
    git clone https://github.com/ваш_проект.git
    ```

2. Перейдите в директорию проекта:

    ```
    cd employees
    ```

3. В файле `.env_prod` и установите необходимые переменные окружения, например:

    ```
    DB_USER=myuser
    DB_PASSWORD=mypassword
    SECRET_KEY=mysecretkey
    ```

4. Запустите Docker Compose:

    ```
    docker-compose -f docker-compose.yml up --build -d
    ```

   Это запустит все контейнеры, включая веб-приложение, базу данных и другие сервисы.

5. Откройте ваш браузер и перейдите по адресу:

    ```
    http://localhost:8000/departments
    ```

   Здесь вы найдете список departments.

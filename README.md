# Comandos Flask
    - flask run --debug
    - flask shell

## Localizando API
    - MAC
        - export FLASK_APP=api
        - export FLASK_ENV=development
    - WINDOWS
        - POWERSHELL
            - $env:FLASK_APP="api"
            - $env:FLASK_ENV="development"
        - PROMPT
            - set FLASK_APP=api
            - set FLASK_ENV=development

## Migrate
    - flask db init
    - flask db migrate
    - flask db upgrade

## Passo-a-passo
    1. criar models
    2. criar entities
    3. criar schemas
    4. criar services
    5. criar views
    6. criar decorators

## Heroku
    - install git
    - install heroku cli
    - install gunicorn

## Tipos de dados FLASK
    - Integer
    - String(size)
    - Text
    - DateTime
    - Date
    - Time
    - Interval {time delta}
    - Numeric {decimal}
    - Float
    - Boolean
    - Uuid
    - LargeBinary

## Argumentos de dados FLASK
    - nullable = True or False
    - primary_key = True or False
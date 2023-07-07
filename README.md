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
    - viewonly = Se definido como True, o relacionamento é usado para carregar objetos, mas quaisquer alterações no estado do   atributo não serão mantidas em uma operação de limpeza do banco de dados. Isso significa que você não pode usar esse relacionamento para adicionar novos objetos ou alterar a chave estrangeira relacionada. Isso geralmente é usado para junções complexas nas quais você deseja carregar objetos relacionados para operações de leitura, mas não deseja que as alterações nesse relacionamento afetem o banco de dados. O padrão é False, o que significa que as alterações afetarão o banco de dados.
    - uselist = Este é um booleano que determina como o lado "muitos" de um relacionamento um-para-muitos ou muitos-para-muitos deve ser acessado. Se for definido como True(que é o padrão), o atributo será tratado como uma lista mutável de itens. Se for definido como False, o atributo será tratado como escalar (valor único). Isso é usado para controlar se você obtém uma lista ou um único objeto ao acessar o relacionamento.
    Por exemplo, se você tiver uma Userclasse e cada usuário puder ter muitos Emailobjetos, se uselistfor definido como Truepara o emailsrelacionamento, user.emailsfornecerá uma lista de Emailobjetos. Se uselistfosse False, user.emailsdaria a você um único Emailobjeto (o mais recente, de acordo com a ordem do relacionamento).
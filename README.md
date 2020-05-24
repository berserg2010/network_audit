## Клиентская часть

### Windows Client

Winrm работате только с частной сетью.
Слеющие команды меняют меняют сеть только до перезагрузки.

    Get-NetConnectionProfile
    Set-NetConnectionProfile -Name "Неопознанная сеть" -NetworkCategory Private
>

Переключить сеть можно в "Локальная политика безопасности" (secpol.msc):

    Поитика диспетчера списка сетей/
        Неопознанная сеть
            
            Тип расположения -> Личное
>

    winrm qc
    winrm get winrm/config
>

    winrm set winrm/config/client '@{AllowUnencrypted="true"}'
    winrm set winrm/config/client '@{TrustedHosts="*"}'
    winrm set winrm/config/service '@{AllowUnencrypted="true"}'
    winrm set winrm/config/service/auth '@{Basic="true"}'
>

Так же winrm можно настроить через групповые политики (gpedit.msc):

    Административные шаблоны/
        Компоненты Windows/
            Удаленная оболочка Windows/
            Удаленное управление Windows/

Внести изменения в Брандмауер защитника Windows:

    Дополнительные параметры ->
        Правила для входящего подключения ->
            Удаленное управление Windows (HTTP - входящий трафик)


Также учетная запись должна быть с правами administrator.


## Серверная часть

### Установка Docker

https://docs.docker.com/engine/install/

### Создание миграции, регистрация суперпользователя

    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
>
    docker-compose run web python manage.py createsuperuser

Потребуется ввести `Username` и `Password`.


### Запуск контейнеров

При первом запуске:

    docker-compose up --build

В дальнейшем:

    docker-compose up

### Запуск unit тестов
    docker-compose run web pytest

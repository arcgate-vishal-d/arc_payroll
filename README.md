# arcgate-payroll

**Note** -

Install python 3.10 version

Install Docker 24.0.5 version

## Create virtual enviorment 
    
    python -m venv env
        
## Activate virtual enviorment

    source env/bin/activate

## Python management commands 

    - make run = python manage.py runserver
    - make migrations = python manage.py makemigrations
    - make migrate = pyhton manage.py migrate
    - make superuper = pyhton manage.py createsuperuser

    **NOTE** - All the commands should use from root folder

## environment variable setup

    Keep all non sharable information in .env
    pip install django-environ
    or 
    pip install -r requirement.txt

##### Create .env.example 
    
    Create a .env.example file in the root directory where requirement.txt resides and add the following key-value pair inside the file.
        
## Sentry setup
    
    pip install sentry-sdk
    or 
    pip install -r requirement.txt

## formatted the code using Black code formatter

## Docker setup

    Create the Dockerfile at the root level
    create .dockerignore file (for hiding the .env configurations)

### create the docker Image and run container

    docker build --tag python-django .
    docker run --publish 8000:8000 python-django

## Swagger 

    pip install -U drf-yasg

## Create Database

    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=yourdbname
    DB_USER=yourdbuser
    DB_PASSWORD=yourdbpassword
    DB_HOST=db
    DB_PORT=5432



## Unit Testing
        
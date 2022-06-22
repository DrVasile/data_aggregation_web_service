# Data Aggregation Web Service

## Installing Dependencies
- First, cd to the root directory where the requirements file is. 
- Activate virtual environment (if it applies): __*source ./venv/bin/activate*__
- pip install -r requirements.txt

## Preparing the database
- Generate migrations: python manage.py makemigrations
- Migrate: python manage.py migrate

## Run the project
- python manage.py runserver
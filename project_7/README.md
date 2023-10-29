### step 1: create virtual environment
```bash
python -m venv venv
```

### step 2: activate virtual environment
```bash
.\venv\Scripts\activate
```

### step 3: install requirements if exist file requirements.txt
```bash

pip install -r requirements.txt
```

### step 4: run the project
```bash 
# linux

cd ./apps && python manage.py runserver
# windows
cd ./apps; python manage.py runserver
```


### description
1. create project
```bash
django-admin startproject apps
```
2. cd to myapp
```bash
cd ./apps
```
3. create news app
```bash
python manage.py startapp news
```
4. To run server
```bash
python manage.py runserver
```
5. to make migrations
```bash
python manage.py makemigrations
```
6. to apply migrations
```bash
python manage.py migrate
```
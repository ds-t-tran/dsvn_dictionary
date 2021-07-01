# dsvn_dictionary
- if not install lib mysql:
run command: 
pip install pymysql

- after open settings.py and change declaration of DATABASES:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbname',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
- install the django-cors-headers library:
pip install django-cors-headers

- run command:
python manage.py makemigrations 
python manage.py migrate

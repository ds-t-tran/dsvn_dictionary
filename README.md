# dsvn_dictionary
- if not install lib mysql:
run command: 
1.pip install pymysql

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
1.pip install django-cors-headers

- run command:
1.python manage.py makemigrations 
2.python manage.py migrate

- authentication jwt in django:
1.pip install djangorestframework-simplejwt

- create superuser:
1.python manage.py createsuperuser

- Google API Speech-to-Text:
1.pip install SpeechRecognition
2.pip install pipwin
3.pipwin install pyaudio

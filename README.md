# test-django

# creation d'environment virtuels
python -m venv env

# activation de virtualenv
env\Scripts\activate

# installation de django et djangoRestFrameworks, django-cors-headers, psycopg2

pip install django djangorestframework psycopg2-binary django-cors-headers

# Utilisation de database postgresql 
voici une partie de configuration dans setting.py

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbblogs',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Creer un projet django
django admin startproject

# creer un app blogs
python manage.py startapp blog

# Demarrer le serveur python
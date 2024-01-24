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
python manage.py runserver 


# Demarrer de la migration
python manage.py makemigrations 
python manage.py migrate

# code pour les migrations
(env) C:\test-django\blog\blogs>python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Article

    Operations to perform:
  Apply all migrations: admin, auth, authtoken, blog, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK    
  Applying contenttypes.0002_remove_content_type_name... OK     
  Applying auth.0002_alter_permission_name_max_length... OK     
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK  
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK     
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying authtoken.0003_tokenproxy... OK
  Applying blog.0001_initial... OK
  Applying sessions.0001_initial... OK


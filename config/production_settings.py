from settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'okk^$ig)_qzqc_d5cj-e5hz9b1($0czi8v8jy%xqu#e6aqxd3j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ballers',
        'USER': 'baller',
        'PASSWORD': 'woshinibaba',
        'HOST': 'baller-server.clnyfmixjdit.us-west-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

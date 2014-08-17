# =================
# = External Urls =
# =================
#STORAGE_URL = 'ballerscourt.s3-website-us-west-1.amazonaws.com'
DATABASE_URL = 'baller-server.clnyfmixjdit.us-west-1.rds.amazonaws.com'

# ===========================
# = Directory Declaractions =
# ===========================

#MEDIA_ROOT = os.path.join(STORAGE_URL, 'ballerscourt/media')

# ===================
# = Global Settings =
# ===================

DEBUG = True
TEMPLATE_DEBUG = True

#database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ballers',
        'USER': 'baller',
        'PASSWORD': 'woshinibaba',
         #'HOST': 'baller-server.clnyfmixjdit.us-west-1.rds.amazonaws.com',
        'HOST': DATABASE_URL,
        'PORT': '5432',
    }
}

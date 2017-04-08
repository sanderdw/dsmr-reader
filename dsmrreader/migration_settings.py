from dsmrreader.config.production import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dsmrreader',
        'USER': 'dsmrreader',
        'PASSWORD': 'dsmrreader',
        'HOST': 'localhost',
        'CONN_MAX_AGE': 60,
    },
    'source': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dsmrreader',
        'USER': 'dsmrreader',
        'PASSWORD': 'dsmrreader',
        'HOST': 'localhost',
        'CONN_MAX_AGE': 60,
    },
}

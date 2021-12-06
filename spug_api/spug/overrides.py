
DEBUG = True

SPUG_VERSION = "v3.0.2-dev"

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": True,
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'db_spug',
        'USER': 'dba',
        'PASSWORD': 'pass',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
            'charset': 'utf8mb4',
        },
    }
}

from .settings import *


DATABASES = {
    'default': env.db('DATABASE_URL', default='psql://vagrant:dbpass@127.0.0.1:5432/test_db'),
}

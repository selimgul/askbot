import sys, os
sys.path.append('/data/override')
sys.path.append('/data/contrib')

from settingsoverride import *

# selim gul
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.postgresql_psycopg2',
        'NAME'    : os.getenv('DB_NAME', 'postgres'),                      
        'USER'    : os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'pwd'),
        'HOST'    : os.getenv('DB_HOST', 'postgres-server'),          
        'PORT'    : os.getenv('DB_PORT', '5432'),
        'TEST_CHARSET'  : 'utf8',              
        'TEST_COLLATION': 'utf8_general_ci', 
    }
}

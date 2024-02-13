import os
import dotenv

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

TEMP_PATH = "D:\KDT_Lecture\Lecture\day3\\temporary_storage"

DB_SETTINGS = {
    "POSTGRES" : {
        'engine': 'postgresql',
        'orm_engine': 'postgresql',
        'host' : os.environ.get('POSTGRES_HOST'),
        'db_name' : os.environ.get('POSTGRES_DB_NAME1'),
        'user' : os.environ.get('POSTGRES_USER'),
        'password' : os.environ.get('POSTGRES_PASSWORD'),
        'port' : os.environ.get('POSTGRES_PORT')
    },
    "KDT" : {
        'engine': 'postgresql',
        'orm_engine': 'postgresql',
        'host' : os.environ.get('POSTGRES_HOST'),
        'db_name' : os.environ.get('POSTGRES_DB_NAME2'),
        'user' : os.environ.get('POSTGRES_USER'),
        'password' : os.environ.get('POSTGRES_PASSWORD'),
        'port' : os.environ.get('POSTGRES_PORT')
    }
}
import os
import dotenv

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

TEMP_PATH = "d:\data_engineering\DataEngineering-Lecture\day-test\\temporary_storage"
TABLE_ORIGIN="fake"
TABLE_DESTINATION="fake_datamart"

DB_SETTINGS = {
    "POSTGRES" : {
        'engine' : 'postgresql',
        'host' : os.environ.get("POSTGRES_HOST"),
        'database' : os.environ.get("POSTGRES_DB_1"),
        'user' : os.environ.get("POSTGRES_USER"),
        'password' : os.environ.get("POSTGRES_PASSWORD"),
        'port' : os.environ.get("POSTGRES_PORT")
    },
    "DVDRENTAL" : {
        'engine' : 'postgresql',
        'host' : os.environ.get("POSTGRES_HOST"),
        'database' : os.environ.get("POSTGRES_DB_2"),
        'user' : os.environ.get("POSTGRES_USER"),
        'password' : os.environ.get("POSTGRES_PASSWORD"),
        'port' : os.environ.get("POSTGRES_PORT")
    },
    "MYSQL" : {
        'engine' : 'mysql',
        'host' : os.environ.get("MYSQL_HOST"),
        'database' : os.environ.get("MYSQL_DB"),
        'user' : os.environ.get("MYSQL_USER"),
        'password' : os.environ.get("MYSQL_PASSWORD"),
        'port' : os.environ.get("MYSQL_PORT")
    },
}
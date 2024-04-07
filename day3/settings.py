import os
import dotenv

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

TEMP_PATH = 'c:\\Users\\user\\Downloads\\DataEngineering_Draft\\day3\\temp_storage'

DB_SETTINGS = {
    "POSTGRESQL" : dict(
        engine = os.environ.get("POSTGRES_ENGINE", ""),
        host = os.environ.get('POSTGRES_HOST', ""),
        database = os.environ.get('POSTGRES_DATABASE', ""),
        user = os.environ.get('POSTGRES_USER', ""),
        password = os.environ.get('POSTGRES_PASSWORD', ""),
        port = os.environ.get('POSTGRES_PORT', "")
    ),
    "MYSQL" : dict(
        engine = os.environ.get("MYSQL_ENGINE", ""),
        host = os.environ.get('MYSQL_HOST', ""),
        database = os.environ.get('MYSQL_DATABASE', ""),
        user = os.environ.get('MYSQL_USER', ""),
        password = os.environ.get('MYSQL_PASSWORD', ""),
        port = os.environ.get('MYSQL_PORT', "")
    )
}
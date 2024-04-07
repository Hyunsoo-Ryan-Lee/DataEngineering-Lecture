import psycopg2, pymysql
from sqlalchemy import create_engine
from db import postgresql_query

class DBconnector:
    def __init__(self, engine: str, host: str, database: str, user: str, password: str, port: str):
        self.engine = engine
        if engine == "postgresql":
            self.conn_params = dict(
                                    host = host,
                                    dbname = database,
                                    user = user,
                                    password = password,
                                    port = port
                                )
            self.sqlalchemy_param = f'postgresql://{user}:{password}@{host}:{port}/{database}'
            self.postgres_connect()
            
        elif engine == "mysql":
            self.conn_params = dict(
                                    host = host,
                                    database = database,
                                    user = user,
                                    password = password,
                                    port = int(port),
                                    charset = 'utf8'
                                )
            self.sqlalchemy_param = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
            self.mysql_connect()
            
        self.sqlalchemy_connect()

    def __enter__(self):
        print("enter 접속")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.engine == 'postgresql':
            self.connect.close()
        elif self.engine == 'mysql':
            self.pymysql_connect.close()
        print("exit 종료")

    def postgres_connect(self):
        self.connect = psycopg2.connect(**self.conn_params)
        
    def mysql_connect(self):
        self.pymysql_connect = pymysql.connect(**self.conn_params)

    def sqlalchemy_connect(self):
        self.sqlalchemy_connect = create_engine(self.sqlalchemy_param)

    def get_query(self, table_name: str, batch_date: str) -> str:
        _query = postgresql_query.queries[table_name] # SELECT * FROM study_his WHERE proc_ymd = '{batch_date}'
        _query = _query.format(batch_date = batch_date) # SELECT * FROM study_his WHERE proc_ymd = '20230505'
        return _query

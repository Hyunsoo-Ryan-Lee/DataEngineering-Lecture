import psycopg2, pymysql
from sqlalchemy import create_engine
from db import postgresql_query
from db import mysql_query

class   DBconnector:
    def __init__(self, engine, host, database, user, password, port):
        self.conn_params = {
            'password' : password,
            'host' : host,
            'user' : user,
            'dbname' : database,
            'port' : port
        }
        self.mysql_conn_params = {
            'passwd' : password,
            'host' : host,
            'user' : user,
            'db' : database,
            'port' : int(port),
            'charset' : 'utf8'
        }

        # DB 엔진별로 분기;
        if engine == "postgresql":
            self.postgres_connect()
            self.orm_conn_params = f'postgresql://{user}:{password}@{host}:{port}/{database}'
            self.queries = postgresql_query.queries

        elif engine == 'mysql':
            self.mysql_connect()
            self.orm_conn_params = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
            self.queries = mysql_query.queries

        # sqlalchemy connection 생성
        self.sqlalchemy_connect()


    def __enter__(self):
        print("접속")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("종료")
        self.conn.close()

    ## psycopg2 라이브러리를 사용한 connection
    def postgres_connect(self):
        self.conn = psycopg2.connect(**self.conn_params)
        return self

    def mysql_connect(self):
        self.conn = pymysql.connect(**self.mysql_conn_params)
        return self
    
    ## sqlalchemy 라이브러리를 사용한 connection
    def sqlalchemy_connect(self):
        self.orm_conn = create_engine(self.orm_conn_params)
        return self

    def get_query(self, table_name, batch_date):
        query = self.queries[table_name]
        return query.format(batch_date = batch_date)
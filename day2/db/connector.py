import psycopg2, pymysql
from db import postgresql_query, mysql_query
from sqlalchemy import create_engine

class DBconnector:
    def __init__(self, engine, orm_engine, host, database, user, password, port):
        self.engine = engine
        self.orm_engine = orm_engine
        self.conn_params = dict(
            host = host,
            dbname = database,
            user = user,
            password = password,
            port = port
        )
        self.mysql_conn_params = dict(
            host = host,
            db = database,
            user = user,
            passwd = password,
            port = int(port),
            charset ='utf8'
        )
        self.orm_conn_params = f"{orm_engine}://{user}:{password}@{host}:{port}/{database}"
        self.orm_connect()
        
        if self.engine == 'postgresql':
            self.connect = self.postgres_connect()
            self.queries = postgresql_query.queries
        
        elif self.engine == 'mysql':
            self.connect = self.mysql_connect()
            self.queries = mysql_query.queries

    def __enter__(self):
        print("접속")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        print("종료")

    def postgres_connect(self):
        self.conn = psycopg2.connect(**self.conn_params)

    def mysql_connect(self):
        self.conn = pymysql.connect(**self.mysql_conn_params)

    def orm_connect(self):
        self.orm_conn = create_engine(self.orm_conn_params)
    
    def get_query(self, table_name, batch_date=None): 
        _query = self.queries[table_name]
        if batch_date:
            return _query.format(batch_date = batch_date)
        else:
            return _query
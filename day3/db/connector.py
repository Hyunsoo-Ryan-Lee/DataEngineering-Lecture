# import psycopg2, pymysql
# from db import postgresql_query
# from db import mysql_query

# class DBconnector:
#     def __init__(self, engine, host, db_name, user, passwd, port):
#         self.engine = engine
#         self.conn_params = dict(
#             host = host,
#             dbname = db_name,
#             user = user,
#             password = passwd,
#             port = int(port)
#         )
#         self.conn = None
        
#         if self.engine == 'postgresql':
#             self.connect = self.postgres_connect
#             self.queries = postgresql_query.queries
#         elif self.engine == 'mysql':
#             self.conn_params['db'] = db_name
#             self.conn_params.pop('dbname', None)
#             self.connect = self.mysql_connect
#             self.queries = mysql_query.queries
            
    
#     # with 구문에 진입되는 시점에 자동으로 호출
#     def __enter__(self):
#         print("DB에 접속합니다.")
#         self.connect()
#         return self
    
#     # with 구문에서 빠져나오기 직전에 자동으로 호출. 
#     # 인자들은 예외 발생시의 정보를 담고 있기 때문에 예외가 없다면 None값
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("DB 연결을 끊습니다.")
#         self.conn.close()
        
#     def postgres_connect(self):
#         self.conn = psycopg2.connect(**self.conn_params)
        
#     def mysql_connect(self):
#         self.conn = pymysql.connect(**self.conn_params)
        
#     def get_query(self, table_name, batch_date=None):
#         _query = self.queries[table_name]
#         if batch_date:
#             return _query.format(batch_date= batch_date)
#         return _query

import psycopg2, pymysql
from db import postgresql_query, mysql_query
from sqlalchemy import create_engine

class DBconnector:
    def __init__(self, engine, orm_engine, host, db_name, user, password, port):
        self.engine = engine
        self.orm_engine = orm_engine
        self.conn_params = dict(
            host = host,
            dbname = db_name,
            user = user,
            password = password,
            port = port
        )
        self.mysql_conn_params = dict(
            host = host,
            db = db_name,
            user = user,
            passwd = password,
            port = int(port),
            charset ='utf8'
        )
        self.orm_conn_params = f"{orm_engine}://{user}:{password}@{host}:{port}/{db_name}"
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
from db.connector import DBconnector
from settings import DB_SETTINGS
from fake_data.create import create_fake_user

from psycopg2.extras import execute_values
import random

def insert_data():
    
    db_connector = DBconnector(**DB_SETTINGS['POSTGRES'])

    with db_connector as connected:
        
        cursor=connected.conn.cursor()
        userkey_list = ['uuid', 'name', 'job', 'residence', 'blood_group', 'sex', 'birthdate']
        row_add = random.randint(5,15)
        
        insert_list = [tuple([create_fake_user()[key] for key in userkey_list]) for _ in range(row_add)]
        
        sql = f"INSERT INTO fake_user2 VALUES %s;"
        execute_values(cursor, sql, insert_list)
            
        connected.conn.commit() 
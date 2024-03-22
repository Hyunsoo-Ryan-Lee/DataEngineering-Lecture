from db.connector import DBconnector
from settings import DB_SETTINGS, TABLE_ORIGIN
from fake_user.create import create_fake_dataframe
from random import randint

def insert_fake_dataframe():
    num = randint(5,15)
    print(f"{num} ROWS WILL BE ADDED")
    db_connector = DBconnector(**DB_SETTINGS['POSTGRES'])

    fake_df = create_fake_dataframe(num)
    with db_connector as connected:
        orm_con = connected.orm_conn
        fake_df.to_sql(TABLE_ORIGIN, con=orm_con, if_exists='append', index=False)
import pandas as pd
from db.connector import DBconnector
from settings import DB_SETTINGS

def insert_fakedataframe(df: pd.DataFrame) -> bool:
    
    db_connector = DBconnector(**DB_SETTINGS["POSTGRESQL"])
    
    with db_connector as connected:
        try:
            sqlalchemy_conn = connected.sqlalchemy_connect
            df.to_sql(name="fake_data", con=sqlalchemy_conn, if_exists="append", index=False)
            return True
        
        except Exception as e:
            print(e)
            return False
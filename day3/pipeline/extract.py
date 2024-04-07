import pandas as pd
from db.connector import DBconnector

def extractor(db_connector: DBconnector, table_name: str, batch_date:str) -> pd.DataFrame|list:
    print("extractor 시작")
    with db_connector as connected:
        try:
            db = connected.connect
            query = connected.get_query(table_name, batch_date)
            print(query)
            df = pd.read_sql(query, db)
            return df
        
        except Exception as e:
            print(e)
            return []
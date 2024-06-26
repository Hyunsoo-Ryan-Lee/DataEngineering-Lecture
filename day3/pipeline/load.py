import pandas as pd
from db.connector import DBconnector

# loader 함수 생성
def loader(df: pd.DataFrame, db_connector: DBconnector, table_name: str) -> bool:
    print("loader 시작")
    with db_connector as connected:
        try:
            sqlalchemy_conn = connected.sqlalchemy_connect
            df.to_sql(name=f"fake_datamart", con=sqlalchemy_conn, if_exists="replace", index=False)
            return True
        except Exception as e:
            print(e)
            return False
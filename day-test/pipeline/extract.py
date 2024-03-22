import pandas as pd

def extractor(db_connector, table_name, batch_date):
    print("EXTRACTOR START")
    with db_connector as connected:
        con = connected.conn
        _query = connected.get_query(table_name, batch_date)
        try:
            pandas_df = pd.read_sql(_query, con)
            return pandas_df
        except:
            return False
            
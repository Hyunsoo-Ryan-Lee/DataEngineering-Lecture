import pandas as pd


def extractor(db_connector, table_name, batch_date=None):
    
    print("EXTRACTOR")
    
    with db_connector as connected:
    
        _query = connected.get_query(table_name = table_name, batch_date = batch_date)
        
        try:
            df = pd.read_sql(_query, connected.conn)
            
        except Exception as e:
            print(e)
        
    return df
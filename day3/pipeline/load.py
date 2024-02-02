
def loader(db_connector, df, table_name):
    
    print("LOADER!")
    
    with db_connector as connected:
        orm_conn = connected.orm_conn
        df.to_sql(name=table_name, con=orm_conn, if_exists='replace')
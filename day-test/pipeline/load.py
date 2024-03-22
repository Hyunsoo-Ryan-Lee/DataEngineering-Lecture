
def loader(db_connector, pandas_df, table_name):
    print("LOADER START")
    with db_connector as connected:
        orm_con = connected.orm_conn # sqlalchemy connection
        try:
            pandas_df.to_sql(f"{table_name}", con=orm_con, if_exists="replace", index=False)
            return True
        except:
            return False
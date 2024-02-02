from db.connector import DBconnector
from db.postgresql_query import queries
from pipeline.extract import extractor
from pipeline.transform import transformer
from pipeline.load import loader
from pipeline.remove import remover
from settings import DB_SETTINGS, TEMP_PATH


def main(batch_date):
    
    db_connector = DBconnector(**DB_SETTINGS['POSTGRES'])
    
    for table_name in queries:
        print(table_name)
        pandas_df = extractor(db_connector, table_name, batch_date)
        
        res, df = transformer(batch_date, pandas_df, table_name)
        
        if res:
            
            db_connector = DBconnector(**DB_SETTINGS['POSTGRES'])
            
            loader(db_connector, df, table_name)
            
    remover(TEMP_PATH)
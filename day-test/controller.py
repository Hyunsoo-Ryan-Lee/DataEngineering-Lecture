from db.connector import DBconnector
from settings import (
    DB_SETTINGS,
    TEMP_PATH,
    TABLE_ORIGIN,
    TABLE_DESTINATION
    )
from pipeline.extract import extractor
from pipeline.transform import transformer
from pipeline.load import loader
from pipeline.remove import remover

def main(batch_date):
    print("CONTROLLER START")
    # postgresql db에 대한 객체 생성
    postgres_connector = DBconnector(**DB_SETTINGS['POSTGRES'])
    # mysql db에 대한 객체 생성
    mysql_connector = DBconnector(**DB_SETTINGS['MYSQL'])

    pandas_df = extractor(postgres_connector, TABLE_ORIGIN, batch_date)
    
    if len(pandas_df) > 0:
    
        fake_datamart_df = transformer(TEMP_PATH, batch_date, pandas_df, TABLE_DESTINATION)

        loader_res = loader(mysql_connector, fake_datamart_df, TABLE_DESTINATION)

        if loader_res:
            remover(TEMP_PATH)
    
    else:
        print("EMPTY DATAFRAME")
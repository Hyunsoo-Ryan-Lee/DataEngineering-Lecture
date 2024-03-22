from db.connector import DBconnector
from settings import DB_SETTINGS, TEMP_PATH, DB_LIST
from db import postgresql_query
from db import mysql_query
from pipeline.extract import extractor
from pipeline.transform import transformer
from pipeline.load import loader
from pipeline.remove import remover
from datetime import datetime

def main(batch_date):
    print("CONTROLLER START")

    db_connector = DBconnector(**DB_SETTINGS['POSTGRES'])

    pandas_df = extractor(db_connector, "fake_temp", batch_date)

    transformer_res, fake_datamart_df = transformer(TEMP_PATH, batch_date, pandas_df, "fake_temp")

    if transformer_res:
        db_connector = DBconnector(**DB_SETTINGS['MYSQL'])
        loader_res = loader(db_connector, fake_datamart_df, "fake_datamart")

    if loader_res:
        remover(TEMP_PATH)

if __name__ == "__main__":
    batch_date = datetime.now().strftime('%Y%m%d')
    main(batch_date)
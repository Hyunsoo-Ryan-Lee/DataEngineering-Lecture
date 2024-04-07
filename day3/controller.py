from db import postgresql_query
from db.connector import DBconnector
from settings import DB_SETTINGS, TEMP_PATH
from datetime import datetime

from pipeline.extract import extractor
from pipeline.transform import transformer
from pipeline.load import loader
from pipeline.remove import remover
from fakedata.process import create_fakedatamart

def main(batch_date: str) -> None:
    
    table_list = list(postgresql_query.queries.keys())

    for table_name in table_list:
        ### 객체 생성 ###
        db_obj = DBconnector(**DB_SETTINGS["POSTGRESQL"])

        ### extract -> postgresql fake_data table에 대한 dataframe ###
        pandas_df = extractor(db_obj, table_name, batch_date)
        
        if len(pandas_df) > 0:
            
            ### create_fakedatamart -> pandas_df 테이블을 가공
            processed_df = create_fakedatamart(pandas_df)

            ### transform -> processed_df 테이블을 temp_storage 경로에 저장 ###
            transform_res =  transformer(
                                        processed_df,
                                        TEMP_PATH,
                                        "postgresql",
                                        table_name,
                                        batch_date
                                    )
            ### load -> mysql table로 저장###
            if transform_res:
                db_obj = DBconnector(**DB_SETTINGS["MYSQL"])
                load_res = loader(processed_df, db_obj, table_name)
    ## remove ###
    # remover(TEMP_PATH)

if __name__ == "__main__":
    _date = datetime.now()
    batch_date = _date.strftime("%Y%m%d")
    main(batch_date)
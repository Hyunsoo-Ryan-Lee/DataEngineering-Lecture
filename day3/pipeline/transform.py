import os
import pandas as pd

def transformer(
        df: pd.DataFrame,
        temp_storage_path: str,
        database_name: str,
        table_name: str,
        batch_date: str
        ) -> bool:
    
    print("transformer 시작")
    
    path = create_path(temp_storage_path, database_name, table_name, batch_date)

    save_result = save_to_file(df, path, table_name) # True / False
    
    return save_result


def create_path(temp_storage_path: str, database_name: str, table_name: str, batch_date:str) -> str:
    _year = batch_date[:4]
    _month = batch_date[4:6]
    _day = batch_date[6:]
    
    _path = os.path.join(temp_storage_path, database_name, table_name, f"yyyy={_year}", f"mm={_month}", f"dd={_day}")
    
    return _path


def save_to_file(df: pd.DataFrame, path:str, table_name:str) -> bool:
    try:
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, f"{table_name}.csv")
        df.to_csv(file_path)
        return True        
    except Exception as e:
        print(e)
        return False
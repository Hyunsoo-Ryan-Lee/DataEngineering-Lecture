import os
from settings import TEMP_PATH

def transformer(batch_date, df, table_name):
    
    print("TRANSFORMER")
    
    _path = create_path(batch_date, table_name)
    
    res = save_to_file(df, _path, table_name)
    
    return res   


def create_path(batch_date, table_name):
    
    _y = batch_date[:4]
    _m = batch_date[4:6]
    _d = batch_date[6:]
    
    final_path = os.path.join(TEMP_PATH, table_name, f'yyyy={_y}', f'mm={_m}', f'dd={_d}')
    
    return final_path


def save_to_file(df, save_path, table_name):
    
    if len(df) > 0:
        os.makedirs(save_path, mode=777)
        file_path = os.path.join(save_path, f'{table_name}.csv')
        
        df.to_csv(file_path, index=False)
        # df.to_parquet(file_path, engine = 'pyarrow', compression = 'gzip', index=False)
        return True
    else:
        print("file is empty.")
        return False
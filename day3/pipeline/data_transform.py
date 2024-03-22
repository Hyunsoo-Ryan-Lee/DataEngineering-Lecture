import os
import pandas as pd
from settings import TEMP_PATH

def transformer(batch_date, pandas_df, table_name):
    
    df = transform_data(pandas_df)
    
    # _path = create_path(batch_date, table_name)
    
    # res = save_to_file(df, _path, table_name)
    
    return df

def transform_data(pandas_df):
    current_year = 2024
    
    # 도시 컬럼 생성
    pandas_df['city'] = pandas_df['residence'].str.split().str[0]
    
    # 혈액형 컬럼 생성
    pandas_df['blood'] = pandas_df['blood_group'].str.slice(0, -1)
    
    # 출생년도 컬럼 생성
    pandas_df['birthdate'] = pandas_df['birthdate'].astype(str)
    pandas_df['birthyear'] = pandas_df['birthdate'].str.slice(0,4)
    
    # 나이 컬럼 생성
    pandas_df['age'] = current_year - pandas_df['birthyear'].astype(int)

    # 연령대 컬럼 생성
    pandas_df['age_category'] = pandas_df['age'].apply(categorize_age)
    
    # 필요한 컬럼만 선택
    df = pandas_df[['uuid', 'name', 'job', 'sex', 'city', 'birthyear', 'age', 'age_category', 'blood']]

    return df
    
    
def categorize_age(age):
    if 0 <= age < 10:
        return '0대'
    else:
        if age >= 100:
            return "90대 이상"
        else:
            age_group = (age) // 10 * 10
            return f'{age_group}대'

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
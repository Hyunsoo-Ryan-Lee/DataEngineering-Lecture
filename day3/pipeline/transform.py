import os
from fake_user.process import transform_data

def transformer(temp_path, batch_date, pandas_df, table_name):
    print("TRANSFORMER START")

    fake_datamart_df = transform_data(pandas_df)

    path = create_path(temp_path, batch_date, table_name)
    response = save_to_file(fake_datamart_df, path, table_name)
    # True / False
    
    return response, fake_datamart_df

def create_path(temp_path, batch_date, table_name):
    
    _year = batch_date[:4]
    _month = batch_date[4:6]
    _day = batch_date[6:]

    _path = os.path.join(
        temp_path,
        "database",
        table_name,
        f"yyyy={_year}",
        f"mm={_month}",
        f"dd={_day}" 
        )

    return _path

def save_to_file(pandas_df, path, table_name):

    if len(pandas_df) > 0:
    # pandas_df가 저장될 경로 생성
        os.makedirs(path, exist_ok=True)
        
        save_path = os.path.join(path, f"{table_name}.csv")
        pandas_df.to_csv(save_path, index=False)
        return True
    else:
        print("EMPTY DATAFRAME")
        return False
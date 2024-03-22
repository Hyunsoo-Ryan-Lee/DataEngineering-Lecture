import os
from fake_user.datamart import transform_data

def transformer(temp_path, batch_date, pandas_df, table_name):
    """
    pandas_df를 datamart 형태로 가공하여 특정 경로 아래에 csv 파일로 저장하는 함수
    """
    print("TRANSFORMER START")

    fake_datamart_df = transform_data(pandas_df)

    path = create_path(temp_path, batch_date, table_name)
    save_to_file(fake_datamart_df, path, table_name)
    # True / False
    
    return fake_datamart_df


def create_path(temp_path, batch_date, table_name):
    """
    batch_date와 table_name을 이용하여 temp_path 아래에 특정 경로를 생성하는 함수
    """
    
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
    """
    pandas_df를 path 경로 아래에 csv 파일 형태로 저장하는 함수
    """

    os.makedirs(path, exist_ok=True)
    save_path = os.path.join(path, f"{table_name}.csv")
    pandas_df.to_csv(save_path, index=False)

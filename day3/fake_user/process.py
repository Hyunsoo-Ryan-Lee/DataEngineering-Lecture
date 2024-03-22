import pandas as pd

def transform_data(pandas_df):
    current_year = 2024

    # 도시 이름 컬럼 생성
    pandas_df["city"] = pandas_df["residence"].str.split().str[0]

    # 출생년도 컬럼 생성
    pandas_df["birthyear"] = pandas_df["birthdate"].str.slice(0, 4)

    # 혈액형 컬럼 생성
    pandas_df["blood"] = pandas_df["blood_group"].str.slice(0, -1)

    # 나이 컬럼 생성
    pandas_df["age"] = current_year - pandas_df["birthyear"].astype(int)

    # 나이대 컬럼 생성
    pandas_df["age_category"] = pandas_df["age"].apply(categorize_age)

    df = pandas_df[["uuid", "name", 'job', "sex", "city", "birthyear", "age", "blood", "age_category"]]

    return df


def categorize_age(age):

    if age >= 100:
        return "90대 이상"
    else:
        return str(age // 10 * 10) + "대"
import pandas as pd

def create_fakedatamart(df: pd.DataFrame) -> pd.DataFrame:
    
    # 도시 컬럼 생성
    df["city"] = df["residence"].str.split().str[0]
    # 생년월일 컬럼 생성
    df["birth_year"] = df["birthdate"].str.slice(0,4)
    # 나이 컬럼 생성
    df["age"] = 2024 - df["birth_year"].astype(int)
    # 혈액형 컬럼 생성
    df["blood"] = df["blood_group"].str.slice(0,-1)
    # 나이대 컬럼 생성
    df["age_category"] = df["age"].apply(categorize_age)
    
    column_list = ["uuid", "name", "job", "sex", "blood", "city", "birth_year", "age", "age_category"]

    df_datamart = df[column_list]
    
    return df_datamart
    
def categorize_age(age: int) -> str:
    if age >= 90:
        return "90대 이상"
    
    else:
        return str(age // 10 * 10) + "대"
import streamlit as st
import pandas as pd

from db.connector import DBconnector
from settings import DB_SETTINGS

## MYSQL DB에서 DataMart 데이터 읽기
db_connector = DBconnector(**DB_SETTINGS['MYSQL'])
with db_connector as connected:
    
    df = pd.read_sql("SELECT * FROM fake_datamart;", connected.conn)

## 차트에 사용할 데이터 생성
df_sex = df.groupby('sex').size().reset_index(name='count')
df_blood = df.groupby('blood').size().reset_index(name='count')
df_city = df.groupby('city').size().reset_index(name='count')
df_age = df.groupby('age_category').size().reset_index(name='count')

## 차트 그리기
# Row Count
st.title(f'TOTAL DATA : {len(df)}')
st.dataframe(df.head())

# 성별
st.header('SEX GROUP BY')
st.bar_chart(df_sex, x='sex', y='count')

# 혈액형
st.header('BLOOD TYPE GROUP BY')
st.bar_chart(df_blood, x='blood', y='count')

# 거주 도시
st.header('CITY GROUP BY')
st.bar_chart(df_city, x='city', y='count')

# 나이
st.header('AGE GROUP BY')
st.line_chart(df_age, x='age_category', y='count')
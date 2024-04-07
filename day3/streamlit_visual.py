import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
from db.connector import DBconnector
from settings import DB_SETTINGS

st_autorefresh(interval=1000, key="fake_datamart")

mysql_obj = DBconnector(**DB_SETTINGS["MYSQL"])

with mysql_obj as connected:
    conn = mysql_obj.pymysql_connect
    _query = "SELECT * FROM fake_datamart"
    datamart = pd.read_sql(_query, conn)

st.title("FAKE USER DASHBOARD")
## 1. 총 ROW 수
st.header(f"FAKE DATA 수 : {len(datamart)}")
st.dataframe(datamart)

## 2. 성비 - BAR 그래프
st.header("성별 비율")
df_sex = datamart.groupby("sex").size().reset_index(name="count")
st.bar_chart(df_sex, x='sex', y='count')

## 3. 혈액형 - BAR 그래프
st.header("혈액형 비율")
df_blood = datamart.groupby("blood").size().reset_index(name="count")
st.bar_chart(df_blood, x='blood', y='count')

## 4. 거주도시 - BAR 그래프
st.header("도시별 비율")
df_city = datamart.groupby("city").size().reset_index(name="count")
st.bar_chart(df_city, x="city", y="count")

## 5. 나이 - LINE 그래프
st.header("나이별 비율")
df_age = datamart.groupby("age_category").size().reset_index(name="count")
st.line_chart(df_age, x="age_category", y="count")




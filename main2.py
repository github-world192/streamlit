import pandas as pd
import streamlit as st

# 讀取數據
df = pd.read_csv("table_data.csv")

# 標題
st.title("表格搜索工具")

# 自定義樣式
st.markdown("""
    <style>
    table {
        width: 100% !important;
    }
    th {
        text-align: left !important;
        padding: 10px;
    }
    td {
        padding: 10px;
        text-align: left;
        word-wrap: break-word;
    }
    </style>
""", unsafe_allow_html=True)

# 搜索框
search_query = st.text_input("輸入關鍵字進行搜索:")

# 搜索結果
if search_query:
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
    st.write(filtered_df.to_html(escape=False, index=False), unsafe_allow_html=True)  # 使用 HTML
else:
    st.write("請輸入關鍵字進行搜索")

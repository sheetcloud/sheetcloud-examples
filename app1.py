import pandas as pd
import streamlit as st
import sheetcloud as sc

from datetime import datetime, timezone


def update():
    df = pd.DataFrame(['=IMPORTFEED("https://news.bitcoin.com/feed/",,False)'], columns=['feed'])
    sc.sheets.append('https://docs.google.com/spreadsheets/d/1VeLIJNw69pGmCY6GRkfabBUUYb5oh1rKA6jX5rPdpZs/edit#gid=1505618093', 'bitcoin_news_feed', df)


# update()
df = sc.sheets.read('https://docs.google.com/spreadsheets/d/1VeLIJNw69pGmCY6GRkfabBUUYb5oh1rKA6jX5rPdpZs/edit#gid=1505618093', 'bitcoin_news_feed')
# df.drop_duplicates(inplace=True)
print(df)
st.data_editor(df)
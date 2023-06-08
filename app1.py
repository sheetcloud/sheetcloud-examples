import pandas as pd
import streamlit as st
import sheetcloud as sc

SHEET_URL = 'https://docs.google.com/spreadsheets/d/1VeLIJNw69pGmCY6GRkfabBUUYb5oh1rKA6jX5rPdpZs/edit#gid=1505618093'
RSS_FEEDS = [('https://news.bitcoin.com/feed/', 'bitcoin_news_feed'), 
             ('https://cointelegraph.com/rss/category/top-10-cryptocurrencies', 'coin_telegraph_top10')]

def update():
    for url, sheet in RSS_FEEDS:
        df = pd.DataFrame([f'=IMPORTFEED("{url}",,False)'], columns=['feed'])
        sc.sheets.append(SHEET_URL, sheet, df)


if st.experimental_get_query_params().get('update', 'False').lower() == 'true':
    update()
else:
    st.title('Crypto News Feed Collector')
    st.markdown('Collect and store RSS feeds in Google Spreadsheets via Sheetcloud.')
    df = sc.sheets.read(SHEET_URL, 'bitcoin_news_feed')
    print(df.info())
    df.drop_duplicates(inplace=True)
    print(df.info())
    st.data_editor(df, use_container_width=True)
import pandas as pd
import streamlit as st
import sheetcloud as sc
from datetime import datetime

DEBUG = True
SHEET_URL = 'https://docs.google.com/spreadsheets/d/1VeLIJNw69pGmCY6GRkfabBUUYb5oh1rKA6jX5rPdpZs/edit#gid=1505618093'


def update(update_token: str):
    config = sc.env.read(SHEET_URL, 'settings', False, False)
    if config['update_token'] == update_token or DEBUG:
        for k, v in config.items():
            if k.lower().startswith('data_'):
                items = config[f'values_{k[5:]}'].split(', ')
                df = pd.DataFrame([[datetime.now(), v.replace('{}', item)] for item in items], columns=['timestamp', 'data'])
                sc.sheets.append(SHEET_URL, k[5:], df, cache=False)


update(st.experimental_get_query_params().get('update', [''])[0])

# if st.experimental_get_query_params().get('update', ['False'])[0].lower() == 'true':
#     update()
# else:
#     st.title('Crypto News Feed Collector')
#     st.markdown('Collect and store RSS feeds in Google Spreadsheets via Sheetcloud.')
#     df = sc.sheets.read(SHEET_URL, 'bitcoin_news_feed')
#     print(df.info())
#     df.drop_duplicates(inplace=True)
#     print(df.info())
#     st.data_editor(df, use_container_width=True)
#     # sc.env.write(SHEET_URL, 'settings', {'token': '$1$xxabc$sp0653/HLmnBo0eb1V6q40', ''})
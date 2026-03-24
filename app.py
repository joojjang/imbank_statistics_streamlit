import streamlit as st

from config import viz_config
from constants.menu_items import menu_items
# from data.dataframe import get_data

if "data" not in st.session_state:
    st.session_state.data = None

# st.session_state.data = get_data()

st.set_page_config(layout="wide")

chart_pages = [
    st.Page(
        page["path"], 
        title=page["label"], 
        icon=page["icon"]
    ) for page in menu_items
]

pg = st.navigation({
    "홈": [
        st.Page("./pages/home.py", title="홈", icon="🏠", default=True)
    ],
    "차트": chart_pages, 
})

pg.run()

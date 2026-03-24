import streamlit as st

from constants.menu_items import menu_items

st.title("iM뱅크 법인 고객 데이터 분석")
st.subheader("메뉴 버튼을 클릭해 이동하세요.")

cols_per_row = 2

for i, item in enumerate(menu_items):
    if i % cols_per_row == 0:
        cols = st.columns(cols_per_row) # 새로운 행(cols)을 만드는 식

    with cols[i % cols_per_row]:
        if st.button(f"{item['icon']} {item['label']}", use_container_width=True):
            st.switch_page(item["path"])
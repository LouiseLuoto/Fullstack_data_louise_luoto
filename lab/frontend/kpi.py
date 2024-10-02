import streamlit as st
from utils.query_database import QueryDatabase


class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;")

    def display_content(self):
        df = self._content.df

        st.dataframe(df)
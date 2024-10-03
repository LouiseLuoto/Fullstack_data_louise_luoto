import streamlit as st
from frontend.kpi import Content
from frontend.kpi import Gender
from frontend.kpi import Age
from frontend.graphs import ViewsTrend


content = Content()
views_trend = ViewsTrend()
gender = Gender()
age = Age()


def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i Kokchuns youtubekanal")

    content.display_content()
    gender.display_gender()
    age.display_age()
    views_trend.display_plot()


if __name__ == "__main__":
    layout()
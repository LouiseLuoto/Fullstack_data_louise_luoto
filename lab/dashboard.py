import streamlit as st
from frontend.kpi import Content, Gender, Age, ViewsPerVideo
from frontend.graphs import ViewsTrend, TrafficSource


content = Content()
gender = Gender()
age = Age()
views_per_video = ViewsPerVideo()
views_trend = ViewsTrend()
traffic_source = TrafficSource()


def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i Kokchuns youtubekanal")    

    content.display_content()
    views_trend.display_plot()
    views_per_video.display_top_10()
    gender.display_gender()
    age.display_age()
    traffic_source.display_plot()

if __name__ == "__main__":
    layout()
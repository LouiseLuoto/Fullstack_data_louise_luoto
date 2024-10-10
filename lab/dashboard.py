import streamlit as st
from frontend.kpi import Content, Gender, Age, ViewsPerVideo
from frontend.graphs import ViewsTrend, TrafficSource, ViewsByDevice
from backend.constants import CSS_PATH


content = Content()
gender = Gender()
age = Age()
views_per_video = ViewsPerVideo()
views_trend = ViewsTrend()
traffic_source = TrafficSource()
views_by_device = ViewsByDevice()


def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i Kokchuns youtubekanal")    

    st.markdown('<div class="section">', unsafe_allow_html=True)
    content.display_content()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    views_trend.display_plot()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    views_per_video.display_top_10()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    gender.display_gender()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section">', unsafe_allow_html=True)
    age.display_age()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    traffic_source.display_plot()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    views_by_device.display_plot()
    st.markdown('</div>', unsafe_allow_html=True)

    read_css()


def read_css():
    with open(CSS_PATH) as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


if __name__ == "__main__":
    layout()
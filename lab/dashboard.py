import streamlit as st
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend


content_kpi = ContentKPI()
views_trend = ViewsTrend()


def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska data i min youtubekanal")


    content_kpi.display_content()
    views_trend.display_plot()


if __name__ == '__main__':
    layout()
import streamlit as st
from frontend.kpi import ContentKPI


content_kpi = ContentKPI()


def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska data i min youtubekanal")


    content_kpi.display_content()


if __name__ == '__main__':
    layout()
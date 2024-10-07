from utils.query_database import QueryDatabase
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st


class ViewsTrend:
    def __init__(self) -> None:
        self._views_trend = QueryDatabase("SELECT * FROM marts.views_per_date")

    def display_plot(self):
        df_views_trend = self._views_trend.df

        fig = px.line(df_views_trend, x="Datum", y="Visningar")

        fig.update_layout(
            margin=dict(t=20, b=50),
        )

        st.subheader("Antal visningar under senaste månaden")
        st.plotly_chart(fig)


class TrafficSource:
    def __init__(self) -> None:
        self._traffic_source = QueryDatabase("SELECT * FROM marts.traffic_source")

    def display_plot(self):
        df_traffic_source = self._traffic_source.df

        fig = make_subplots(
            rows=1, 
            cols=2, 
            subplot_titles=("Visningar per Trafikkälla", 
                            "Visningar (timmar) per Trafikkälla")
        )

        fig.add_trace(
            go.Bar(x=df_traffic_source["Trafikkälla"], y=df_traffic_source["Visningar"], showlegend=False),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(x=df_traffic_source["Trafikkälla"], y=df_traffic_source["Visningstid (timmar)"], showlegend=False),
            row=1, col=2
        )

        fig.update_layout(
            title_text="", 
            height=400, 
            width=1200,
            margin=dict(t=30, b=50),
            title_x=0.5
        )

        st.subheader("Trafikkälla")
        st.plotly_chart(fig)
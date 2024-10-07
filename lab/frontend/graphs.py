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
            rows=2, 
            cols=2, 
            subplot_titles=("Visningar per Trafikkälla", 
                            "Visningar (timmar) per Trafikkälla", 
                            "Genomsnittlig visningslängd per Trafikkälla")
        )

        fig.add_trace(
            go.Bar(x=df_traffic_source["Trafikkälla"], y=df_traffic_source["Visningar"], showlegend=False),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(x=df_traffic_source["Trafikkälla"], y=df_traffic_source["Visningstid (timmar)"], showlegend=False),
            row=1, col=2
        )

        fig.add_trace(
            go.Bar(x=df_traffic_source["Trafikkälla"], y=df_traffic_source["Genomsnittlig visningslängd"], showlegend=False),
            row=2, col=1
        )

        fig.update_layout(
            title_text="", 
            height=600, 
            width=1500,
            font=dict(size=12),  # Minskar textstorleken
            margin=dict(t=0, b=50),  # Ökar utrymmet ovanför och under subplots
            title_x=0.5,  # Centrerar huvudrubriken
        )

        # Justera titlarna för subplots
        for annotation in fig['layout']['annotations']:
            annotation['font'] = dict(size=10)  # Minska storleken på subplot-titlarna
            annotation['yanchor'] = 'bottom'  # Flytta titlarna lite högre över subplots

        st.subheader("Trafikkälla")
        st.plotly_chart(fig)
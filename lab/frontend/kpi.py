import streamlit as st
from utils.query_database import QueryDatabase

class Content:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;")
        
    def display_content(self):
        df = self._content.df
        
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")
        
        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum()
        }  
       
        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col:
                st.metric(kpi, round(kpis[kpi]))
              

class Gender:
    def __init__(self) -> None:
        self._gender = QueryDatabase("SELECT * FROM marts.viewers_gender;")       
        
    def display_gender(self):  
        df_gender = self._gender.df

        st.subheader("Tittarnas kön och ålder")
        selected_gender = st.selectbox("Välj kön", df_gender["Tittarnas kön"])
        selected_data = df_gender[df_gender["Tittarnas kön"] == selected_gender]
        st.write(f"Total andel visningar: {round(selected_data['Visningar (%)'].values[0])}%")

class Age:
    def __init__(self) -> None:
        self._age = QueryDatabase("SELECT * FROM marts.viewers_age;")
       
    def display_age(self):
        df_age = self._age.df

        selected_age = st.selectbox("Välj åldersspann", df_age["Tittarnas ålder"])
        selected_data = df_age[df_age["Tittarnas ålder"] == selected_age]
        st.write(f"Total andel visningar: {round(selected_data['Visningar (%)'].values[0])}%")
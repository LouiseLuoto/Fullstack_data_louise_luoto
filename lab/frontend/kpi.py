import streamlit as st
from utils.query_database import QueryDatabase

class Content:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;")
        
    def display_content(self):
        df_content = self._content.df
        
        st.subheader("KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")
        
        kpis = {
            "videor": len(df_content),
            "visade timmar": df_content["Visningstid_timmar"].sum(),
            "prenumeranter": df_content["Prenumeranter"].sum(),
            "exponeringar": df_content["Exponeringar"].sum()
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


class ViewsPerVideo:
    def __init__(self) -> None:
         self._views_per_video = QueryDatabase("SELECT * FROM marts.views_per_video")

    def display_top_10(self):
        df_views_per_video = self._views_per_video.df

        top_10_videos = df_views_per_video.sort_values(by="Visningar", ascending=False).head(10)
        st.subheader("Top 10 mest tittade videor")

        video_urls = [
            "https://www.youtube.com/watch?v=i454nHjdMAc",
            "https://www.youtube.com/watch?v=IUMdhf_vsMs",
            "https://www.youtube.com/watch?v=u4map_3j9LA",
            "https://www.youtube.com/watch?v=KOn6XRDrT8s",
            "https://www.youtube.com/watch?v=TrLrobmqzKQ",
            "https://www.youtube.com/watch?v=PEmcikWd93o",
            "https://www.youtube.com/watch?v=x9AyMOVAtV4",
            "https://www.youtube.com/watch?v=KkmrVSbMap8",
            "https://www.youtube.com/watch?v=NdM4iYw37B8",
            "https://www.youtube.com/watch?v=V2CEc9tCHxM",
        ]

        top_10_videos["Video URL"] = video_urls

        for index, row in top_10_videos.iterrows():
            col1, col2 = st.columns([2, 1]) 
            
            with col1:
                st.write(f"**{index + 1}.**")
                st.write(f"**Videotitel:** {row['Videotitel']}")
                st.write(f"**Visningar:** {row['Visningar']}")

            with col2:
                video_id = row["Video URL"].split("=")[-1]  # Hämta video-ID från URL:en
                video_embed = f"<iframe width='250' height='150' src='https://www.youtube.com/embed/{video_id}' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"
                st.markdown(video_embed, unsafe_allow_html=True)  # Visa videon med HTML
                
                st.markdown("---")  
import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# print("\n"*10)
# # Alltid utgå från vart scriptet befinner sig
# print(Path(__file__).parents[2] /"data")
# print("\n"*10)

# df = pd.read_csv("../../data/cleaned_yh_region.csv")
# print(df)

def read_data():
    data_path = Path(__file__).parents[2] /"data"
    df = pd.read_csv(data_path / "cleaned_yh_region.csv", index_col=0, parse_dates=[0])
    df.index = df.index.year 
    return(df)

def layout():
    df = read_data()
    st.markdown("# YH dashboard")
    st.markdown("This is a simple dashboard about yrkehögskola")
    
    st.markdown("## Raw data")
    st.markdown("Data shows started educations per region per year")
    st.dataframe(df)

    st.markdown("## Trends per region")
    region = st.selectbox("Choose region", df.columns)

    # st.markdown(region)
    # st.markdown(type(region))
    # st.dataframe(df[region])
    fig = px.line(data_frame=df, x=df.index, y=df[region])
    st.plotly_chart(fig)



# __name__ is a special variable, which is equal to __main__ when we run the script
# when we import this script from elsewhere, __name__ is the scripts name
if __name__ == "__main__":
    layout()
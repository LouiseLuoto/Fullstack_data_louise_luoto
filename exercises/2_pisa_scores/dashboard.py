import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px


def read_data():
    data_path = Path(__file__).parents[2] / "data"
    df = pd.read_csv(data_path / "cleaned_pisa_data.csv", index_col=0, parse_dates=[0])
    return df


def layout():
    df = read_data()
    

    # basic statistics of the data (number of records, number of locations, subjects, and time periods)
    st.subheader("Basic statistics")
    st.write(f"Number of records: {df.shape[0]}")

    st.write(f"Number of locations: {df['Country'].unique().shape[0]}")

    st.write(f"Subjects: {', '.join(df['Gender'].unique())}")

    st.write(f"Time period: {df['Year'].min()} - {df['Year'].max()}")


    # show a table with sample data
    st.subheader("Sample data of the 10 first")
    st.dataframe(df.head(10))


    # bar chart showing average PISA scores by location
    st.subheader("Average PISA scores by location")
    tot_subject = df[df["Gender"] == "BOY & GIRL"]
    avg_tot = tot_subject.groupby("Country")["Value"].mean().sort_values()
    st.bar_chart(avg_tot)


    # plot trends that can be filtered for each country
    st.subheader("Trends for each country")
    country = st.selectbox("Choose country", options=df["Country"].unique())
    filtered_country = df[df["Country"] == country]

    subject = st.selectbox("Choose subject", options=filtered_country["Subject"].unique())
    filtered_subject = filtered_country[filtered_country["Subject"] == subject]

    gender = st.selectbox("Choose the gender", options=filtered_subject["Gender"].unique())
    filtered_gender = filtered_subject[filtered_subject["Gender"] == gender]

    fig = px.line(filtered_gender,
                  x="Year", 
                  y="Value", 
                  title=f"Value over time for {country}, {subject}, {gender}")

    st.plotly_chart(fig)


if __name__ == "__main__":
    layout()
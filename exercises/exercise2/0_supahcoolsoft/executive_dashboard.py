import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# 0. Supahcoolsoft employee executive dashboard
def layout():
    df = pd.read_csv("../../data/cleaned_supahcoolsoft.csv", index_col=0)

    st.header("Table of employee details")
    st.dataframe(df)

    st.header("Basic statistics on employees")
    total_employees = df.shape[0]
    average_age = df["Age"].mean()
    average_salary = df["Salary_SEK"].mean()
    st.write(f"Total number of employees: {total_employees}")
    st.write(f"Average age: {average_age:.0f}")
    st.write(f"Average salary: {average_salary:.0f}")


    st.header("Employees across departments")
    department_counts = df["Department"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(department_counts.index, department_counts.values)
    ax.set_xlabel("Department")
    ax.set_ylabel("Number of employees")
    plt.xticks(rotation=45)
    st.pyplot(fig)


    st.header("Salary distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["Salary_SEK"], bins=18)
    ax.set_xlabel("Salary")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)


    st.header("Salaries by Department")
    fig, ax = plt.subplots()
    sns.boxplot(x="Department", y="Salary_SEK", data=df, ax=ax)
    ax.set_xlabel("Department")
    ax.set_ylabel("Salary")
    plt.xticks(rotation=45)
    st.pyplot(fig)


    st.header("Age distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["Age"], bins=18)
    ax.set_xlabel("Age")
    ax.set_ylabel("Freqency")
    st.pyplot(fig)

layout()
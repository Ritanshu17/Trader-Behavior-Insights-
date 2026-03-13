import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bitcoin Sentiment vs Trader Performance Dashboard")

@st.cache_data
def load_data():

    return pd.read_csv("data/processed/merged_dataset.csv")

df = load_data()

sentiments = st.sidebar.multiselect(
    "Sentiment",
    options=df["classification"].unique(),
    default=df["classification"].unique()
)

df = df[df["classification"].isin(sentiments)]

col1,col2,col3 = st.columns(3)

col1.metric("Total Trades",len(df))

col2.metric("Total Profit",round(df["Closed PnL"].sum(),2))

col3.metric("Average Profit",round(df["Closed PnL"].mean(),2))

fig,ax = plt.subplots()

sns.boxplot(data=df,x="classification",y="Closed PnL",ax=ax)

plt.xticks(rotation=45)

st.pyplot(fig)

fig2,ax2 = plt.subplots()

sns.histplot(df["Closed PnL"],bins=40,kde=True,ax=ax2)

st.pyplot(fig2)

top = df.groupby("Account")["Closed PnL"].sum().sort_values(ascending=False).head(10)

st.dataframe(top)
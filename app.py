import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Campaign Best Practices Portal",
    layout="wide"
)

st.title("📊 Sales Campaign Best Practices Sharing Portal")

df = pd.read_csv("campaigns.csv")

st.dataframe(df, use_container_width=True)

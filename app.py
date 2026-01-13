import streamlit as st
import pandas as pd

# ----------------------------
# Page setup
# ----------------------------
st.set_page_config(
    page_title="Sales Campaign Best Practices Portal",
    layout="wide"
)

st.title("📊 Sales Campaign Best Practices Sharing Portal")

# ----------------------------
# Load data
# ----------------------------
df = pd.read_csv("campaigns.csv")

# ----------------------------
# Campaign table
# ----------------------------
st.subheader("📋 Campaign Overview")
st.dataframe(df, use_container_width=True, hide_index=True)

# ----------------------------
# Voting section
# ----------------------------
st.subheader("👍 Vote for Best Practices")

st.info("Click 👍 to upvote a campaign. Votes are saved automatically.")

for index, row in df.iterrows():
    col1, col2, col3 = st.columns([5, 3, 1])

    with col1:
        st.write(f"**{row['Campaign Name']}** ({row['Country']})")

    with col2:
        st.write(row["Result / Impact"])

    with col3:
        if st.button(f"👍 {row['Votes']}", key=f"vote_{index}"):
            df.loc[index, "Votes"] += 1
            df.to_csv("campaigns.csv", index=False)
            st.experimental_rerun()


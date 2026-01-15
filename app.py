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

# Sort by votes (highest first)
df = df.sort_values("Votes", ascending=False).reset_index(drop=True)

# ----------------------------
# Campaign overview (merged with voting)
# ----------------------------
st.subheader("📋 Campaign Overview & Voting")

# Table header
h1, h2, h3, h4, h5 = st.columns([2, 3, 3, 3, 1])
h1.markdown("**Country**")
h2.markdown("**Campaign Name**")
h3.markdown("**Channel**")
h4.markdown("**Result / Impact**")
h5.markdown("**Vote**")

st.divider()

# Table rows
for index, row in df.iterrows():
    c1, c2, c3, c4, c5 = st.columns([2, 3, 3, 3, 1])

    with c1:
        st.write(row["Country"])

    with c2:
        st.write(row["Campaign Name"])

    with c3:
        st.write(row["Channel"])

    with c4:
        st.write(row["Result / Impact"])

    with c5:
        if st.button(f"👍 {row['Votes']}", key=f"vote_{index}"):
            df.loc[index, "Votes"] += 1
            df.to_csv("campaigns.csv", index=False)
            st.experimental_rerun()

# ----------------------------
# Add new campaign form
# ----------------------------
st.divider()
st.subheader("➕ Submit a New Best Practice")

with st.form("add_campaign_form"):
    country = st.text_input("Country (e.g. TH, TR, IN)")
    campaign_name = st.text_input("Campaign Name")
    channel = st.selectbox(
        "Channel",
        ["D2C Online", "Marketplace", "Offline", "Hybrid"]
    )
    period = st.selectbox(
        "Campaign Period",
        ["Q1", "Q2", "Q3", "Q4"]
    )
    objective = st.text_input("Objective")
    description = st.text_area("Campaign Description")
    result = st.text_area("Result / Impact")
    filled_by = st.text_input("Filled By (Name / Team)")

    submitted = st.form_submit_button("Submit Campaign")

# ----------------------------
# Save new campaign
# ----------------------------
if submitted:
    new_row = {
        "Country": country,
        "Campaign Name": campaign_name,
        "Channel": channel,
        "Campaign Period": period,
        "Objective": objective,
        "Description": description,
        "Result / Impact": result,
        "Filled By": filled_by,
        "Votes": 0
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv("campaigns.csv", index=False)

    st.success("✅ Campaign submitted successfully!")
    st.experimental_rerun()

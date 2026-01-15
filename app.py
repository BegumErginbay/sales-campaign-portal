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

# Sort by votes (best practices on top)
df = df.sort_values("Votes", ascending=False)

# ----------------------------
# Campaign table
# ----------------------------
st.subheader("📋 Campaign Overview")
st.dataframe(df, use_container_width=True, hide_index=True)

# ----------------------------
# Voting section
# ----------------------------
st.subheader("👍 Vote for Best Practices")
st.info("Click 👍 to upvote a campaign.")

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
# Save submitted campaign
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

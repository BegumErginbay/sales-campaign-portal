import streamlit as st
import pandas as pd

COUNTRIES = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
    "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
    "Cameroon", "Canada", "Central African Republic", "Chad", "Chile",
    "China", "Colombia", "Comoros", "Congo", "Costa Rica",
    "Côte d’Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
    "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
    "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Honduras", "Hungary", "Iceland",
    "India", "Indonesia", "Iran", "Iraq", "Ireland",
    "Israel", "Italy", "Jamaica", "Japan", "Jordan",
    "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan",
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
    "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
    "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal",
    "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
    "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan",
    "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania",
    "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino",
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
    "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
    "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain",
    "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
    "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
    "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States",
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

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
h1, h2, h3, h4, h5, h6 = st.columns([2, 3, 3, 3, 2, 1])
h1.markdown("**Country**")
h2.markdown("**Campaign Name**")
h3.markdown("**Channel**")
h4.markdown("**Period**")
h5.markdown("**Focus Product**")
h6.markdown("**Vote**")

st.divider()

for index, row in df.iterrows():
    c1, c2, c3, c4, c5, c6 = st.columns([2, 3, 3, 3, 2, 1])

    c1.write(row["Country"])
    c2.write(row["Campaign Name"])
    c3.write(row["Channel"])
    c4.write(row["Campaign Period"])
    c5.write(row["Focus Product (Category)"])

    if c6.button(f"👍 {row['Votes']}", key=f"vote_{index}"):
        df.loc[index, "Votes"] += 1
        df.to_csv("campaigns.csv", index=False)
        st.rerun()

    # Expandable details
    with st.expander("View details"):
        st.write("**Campaign Objective:**", row["Campaign Objective"])
        st.write("**Campaign Description:**", row["Campaign Description"])
        st.write("**Result / Impact:**", row["Result / Impact"])
        st.write("**Filled By:**", row["Filled By"])

# ----------------------------
# Add new campaign form
# ----------------------------
st.divider()
st.subheader("➕ Submit a New Best Practice")

with st.form("add_campaign_form"):

    country = st.multiselect(
    "Country",
    options=COUNTRIES
   )

    campaign_name = st.text_input("Campaign Name")

    channel = st.multiselect(
        "Channel",
        options=[
            "D2C",
            "Partner Operated D2C",
            "KRT",
            "ERT",
            "Project Business B2B",
            "Wholesale / Internal Distributor",
            "Export Distributor"
        ]
    )

    campaign_period = st.text_input(
        "Campaign Period (e.g. Ramadan, Mother's Day, Q1, Summer, May)"
    )

    focus_product = st.text_input("Focus Product (Category)")

    campaign_objective = st.text_area("Campaign Objective")

    campaign_description = st.text_area("Campaign Description")

    result_impact = st.text_area("Result / Impact")

    filled_by = st.text_input("Filled By (Name / Team)")

    submitted = st.form_submit_button("Submit Campaign")


# ----------------------------
# Save new campaign
# ----------------------------
if submitted:
    new_row = {
        "Country": ", ".join(country),
        "Campaign Name": campaign_name,
        "Channel": ", ".join(channel),
        "Campaign Period": campaign_period,
        "Focus Product (Category)": focus_product,
        "Campaign Objective": campaign_objective,
        "Campaign Description": campaign_description,
        "Result / Impact": result_impact,
        "Filled By": filled_by,
        "Votes": 0
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv("campaigns.csv", index=False)

    st.success("✅ Campaign submitted successfully!")
    st.rerun()

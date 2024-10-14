import streamlit as st

# Combined Welcome and About Us page
st.title("Welcome to the Land-Based Farm Setup Guide in Singapore")

# --- Welcome Section ---
st.subheader("Introduction")
st.write("This application aims to provide users with essential information about starting a land-based farm in Singapore. "
         "It covers eligibility requirements, available grants, licensing conditions, and agency requirements.")

# --- About Us Section ---
st.subheader("About Us")

st.write("Our goal is to support aspiring farmers by simplifying access to information and resources needed to start a farm. "
         "We aim to empower individuals with the knowledge and tools to successfully navigate the farming landscape in Singapore.")

st.header("Scope and Objectives")
st.write("""
    - Provide comprehensive information on eligibility requirements for starting a land-based farm.
    - List available funds and grants for aspiring farmers.
    - Offer insights into the licensing conditions and requirements from various agencies.
    - Enable users to interact with a chatbot for additional queries related to licensing conditions.
""")

# Data Sources
st.subheader("Data Source")
st.write("""
- Grants and funding data are retrieved from various government websites and public resources.
- Licensing conditions are obtained from the Singapore Food Agency (SFA) documentation.
- For more information on starting a farm, check the official [SFA Industry Guide on Starting a Farm PDF](https://www.sfa.gov.sg/docs/default-source/food-farming/sfa-farming-guide_fa-spread-high-res.pdf).
""")

# Features
st.header("Features")
st.write("""
    - Interactive chatbot for user inquiries.
    - Detailed information on grants and funds.
    - Licensing conditions for different types of farming.
""")

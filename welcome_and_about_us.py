import streamlit as st

# Combined Welcome and About Us page
st.title("Welcome to the Farm Setup Guide in Singapore")

# --- Welcome Section ---
st.subheader("Introduction")
st.write("""
This guide will help you understand the requirements and process of starting a farm in Singapore. 
Explore the available grants, funding opportunities, and learn about the licensing conditions required for different types of farming. 
Use the navigation on the left to explore more sections.
""")

# --- About Us Section ---
st.subheader("About Us")

st.write("""
Our project is aimed at providing an interactive tool for individuals interested in starting a farm in Singapore. The tool integrates funding options and licensing conditions to make the process easier.
""")

# Project Scope
st.subheader("Project Scope")
st.write("""
This project aims to assist aspiring farmers in understanding the requirements for starting a farm, 
identifying the funds and grants available, and providing detailed information on licensing conditions for different types of farms (e.g., general, poultry, and cattle).
""")

# Project Objectives
st.subheader("Objectives")
st.write("""
- Help users determine the eligibility requirements to start a farm.
- Provide an up-to-date list of available grants and funds for new farms.
- Clarify the licensing conditions based on different types of farming operations.
- Allow users to query specific licensing conditions using a chatbot.
""")

# Data Sources
st.subheader("Data Source")
st.write("""
- Grants and funding data are retrieved from various government websites and public resources.
- Licensing conditions are obtained from the Singapore Food Agency (SFA) documentation.
- For more information on licensing, check the official [SFA Licensing PDF](https://example.com/sfa_licensing_pdf).
""")

# Features
st.subheader("Features")
st.write("""
- **Eligibility Requirements**: A section that lists the basic requirements for setting up a farm in Singapore.
- **Funds and Grants**: A detailed list of grants and funding options available for farm setup.
- **Licensing Conditions**: Chatbot functionality to answer questions about general, poultry, and cattle farm licensing requirements.
""")

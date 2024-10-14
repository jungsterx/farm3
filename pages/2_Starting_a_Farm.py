import streamlit as st
import openai  # Assuming you're using OpenAI API for chatbot responses
import pandas as pd
import os

# Set OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Load text files for conditions
def load_conditions(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Load Data for Funds and Grants
def load_funds_data():
    return pd.read_csv('funds_grants.csv')

# LLM Query Function for the chatbot
def query_llm(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or whichever model you're using
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Streamlit UI for the main app sections
st.title("Starting a Farm: Available Grants and Licence Conditions")

# --- Section 1: Eligibility Requirement ---
st.header("Eligibility Requirement")
st.write("""
1. You must be registered with the Accounting and Corporate Regulatory Authority (ACRA) and have a UEN issued by ACRA.
2. You must have secured a space for your farm, submitted your plan for farming at the premises to SFA for endorsement, obtained clearance from relevant agencies, and commenced small-scale production.
For more details, see the [Requirements to Start a Farm in Singapore](https://example.com/requirements).
""")

# --- Section 2: Funds and Grants ---
st.header("Available Funds and Grants")
if st.button("Show Available Funds and Grants"):
    funds_data = load_funds_data()
    st.write(funds_data)

# --- Section 3: Chatbot for Licensing Conditions ---
st.header("Chat with Licensing Information")

# Load the license conditions
license_conditions = load_conditions('license_conditions.txt')
poultry_conditions = load_conditions('poultry_conditions.txt')
cattle_conditions = load_conditions('cattle_conditions.txt')

# Combine all conditions for LLM to access
all_conditions = f"""
License Conditions:
{license_conditions}

Poultry-Specific Conditions:
{poultry_conditions}

Cattle-Specific Conditions:
{cattle_conditions}
"""

# Chatbot UI
user_query = st.text_input("Ask a question about licensing conditions:")
if user_query:
    prompt = f"The following are licensing conditions:\n{all_conditions}\n\nUser question: {user_query}\nAnswer:"
    llm_response = query_llm(prompt)
    st.write("Response:", llm_response)

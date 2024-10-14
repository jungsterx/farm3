import streamlit as st
import openai  # Ensure you have the OpenAI package installed
import pandas as pd

# Set OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Password protection logic
def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter the password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter the password", type="password", on_change=password_entered, key="password")
        st.error("Password is incorrect")
        return False
    else:
        return True

# Show the page content only if the password is correct
if check_password():
    # Load text files for conditions
    def load_conditions(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    # Load Data
    def load_funds_data():
        return pd.read_csv('funds_grants.csv')

    def load_license_conditions():
        with open('license_conditions.txt', 'r') as file:
            return file.read()

    # LLM Query Function
    def query_llm(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or whichever model you are using
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()

    # Streamlit UI
    st.title("Starting a Land-based Farm: Available Grants, Licence Conditions and Requirements")

    # Section 1: Eligibility Requirement
    st.header("Eligibility Requirement")
    st.write("""
    1. You must be registered with the Accounting and Corporate Regulatory Authority (ACRA) and have a UEN issued by ACRA.
    2. You must have secured a space for your farm, submitted your plan for farming at the premises to SFA for endorsement, obtained clearance from relevant agencies, and commenced small-scale production.
    """)

    # Section 2: Available Funds and Grants
    st.header("Available Funds and Grants")
    if st.button("Show Available Funds and Grants"):
        funds_data = load_funds_data()
        st.write(funds_data)

    # Section 3: License Conditions for Land-based Farms
    st.header("License Conditions")
    if st.button("Show License Conditions"):
        license_conditions = load_license_conditions()
        st.write(license_conditions)

    # Section 4: Requirements to Start a Land-based Farm
    st.header("Requirements to Start a Land-based Farm")
    image_url = "https://raw.githubusercontent.com/jungsterx/farm3/refs/heads/main/Screenshot%202024-10-14%20120536.png?token=GHSAT0AAAAAACY3ZIE3U2D2L6RXSMKHNRBGZYMUSDQ"  # Update with your direct image URL
    st.image(image_url, use_column_width=True)

    # Define the links for each agency
    links = {
        "PUB": "https://www.sfa.gov.sg/docs/default-source/food-farming/industry-guide/pub.pdf",  # Singapore's National Water Agency
        "SCDF": "https://www.sfa.gov.sg/docs/default-source/food-farming/industry-guide/scdf.pdf",  # Singapore Civil Defence Force
        "URA": "https://www.sfa.gov.sg/docs/default-source/food-farming/industry-guide/ura.pdf",  # Urban Redevelopment Authority
        "BCA": "https://www.sfa.gov.sg/docs/default-source/food-farming/industry-guide/bca.pdf",  # Building and Construction Authority
        "NEA": "https://www.sfa.gov.sg/docs/default-source/food-farming/industry-guide/nea.pdf",  # National Environment Agency
        "LTA": "https://www.sfa.gov.sg/docs/default-source/food-farming/industry-guide/lta.pdf",  # Land Transport Authority
        "NParks": "https://www.sfa.gov.sg/docs/default-source/food-farming/industry-guide/nparks.pdf"  # National Parks Board
    }

    # Display buttons or links for each agency horizontally
    cols = st.columns(len(links))  # Create a number of columns equal to the number of agencies

    for col, (agency, url) in zip(cols, links.items()):
        with col:
            if st.button(agency):
                st.markdown(f"[{agency}]({url})")

    # Optional: Add some styling for clarity
    st.markdown(
        """
        <style>
        .stButton > button {
            border: 2px solid black; /* Adds a black border around buttons */
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Section 4: Requirements to Start a Land-based Farm: LLM Query Section (for additional user queries)
    st.header("Ask a question")
    user_query = st.text_input("Type your question here")
    if user_query:
        llm_response = query_llm(f"Q: {user_query}\nA:")
        st.write(llm_response)
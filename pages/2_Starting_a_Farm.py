import streamlit as st 
import openai
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

# Load Data for Grants
def load_funds_data():
    return pd.read_csv('funds_grants.csv')

# Load License Conditions Files
def load_license_conditions(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Predefined Eligibility Conditions
eligibility_criteria = {
    "UEN_registration": "You must be registered with ACRA.",
    "secured_farm_space": "You must have secured a space for your farm.",
    "submitted_plan": "You must have submitted your plan to SFA for approval.",
}

# Function to check eligibility based on user inputs
def check_eligibility(uen, farm_space, plan_submitted):
    if not uen:
        return "You must provide a valid UEN number. You can check your UEN [here](https://www.uen.gov.sg/)."
    
    if not farm_space:
        return eligibility_criteria["secured_farm_space"]
    
    if not plan_submitted:
        return eligibility_criteria["submitted_plan"]
    
    return "Congratulations! You meet the eligibility requirements."

# Streamlit UI
st.title("Starting a Land-based Farm: Available Grants, Licence Conditions and Requirements")

# Section 1: Eligibility Requirement
st.header("Eligibility Requirement")

# User inputs for eligibility check
uen = st.text_input("Enter your UEN number")
st.markdown("Don't know your UEN? You can check it [here](https://www.uen.gov.sg/).")

farm_space = st.checkbox("I have secured a farm space")
plan_submitted = st.checkbox("I have submitted my farming plan to SFA")

if st.button("Check Eligibility"):
    result = check_eligibility(uen, farm_space, plan_submitted)
    st.write(result)

# Section 2: Available Funds and Grants
st.header("Available Funds and Grants")
if st.button("Show Available Funds and Grants"):
    funds_data = load_funds_data()
    st.write(funds_data)

# Section 3: License Conditions
st.header("License Conditions")

# Load general, poultry, or cattle conditions
if st.button("Show General License Conditions"):
    license_conditions = load_license_conditions('license_conditions.txt')
    st.write(license_conditions)

if st.button("Show Poultry License Conditions"):
    poultry_conditions = load_license_conditions('poultry_conditions.txt')
    st.write(poultry_conditions)

if st.button("Show Cattle License Conditions"):
    cattle_conditions = load_license_conditions('cattle_conditions.txt')
    st.write(cattle_conditions)

# Section 4: Requirements to Start a Land-based Farm
st.header("Requirements to Start a Land-based Farm")
image_path = "path_to_local_image.png"  # Update with your local image path
st.image(image_path, use_column_width=True)

# Section 5: Ask a Question (LLM-powered)
st.header("Ask a question")
user_query = st.text_input("Type your question here")
if user_query:
    def query_llm(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()

    llm_response = query_llm(f"Q: {user_query}\nA:")
    st.write(llm_response)

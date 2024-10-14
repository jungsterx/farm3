import streamlit as st
import openai
import pandas as pd

# Set OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Custom CSS for styling
st.markdown("""
    <style>
    .password-box input {
        border: 2px solid black;
        padding: 10px;
        border-radius: 5px;
    }
    .chatbox input {
        border: 2px solid black;
        padding: 10px;
        border-radius: 5px;
    }
    .chat-response {
        border: 2px solid black;
        padding: 10px;
        border-radius: 5px;
        background-color: #f0f0f0;
    }
    </style>
    """, unsafe_allow_html=True)

# Password protection logic
def check_password():
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown('<div class="password-box">', unsafe_allow_html=True)
        st.text_input("Enter the password", type="password", on_change=password_entered, key="password")
        st.markdown('</div>', unsafe_allow_html=True)
        return False
    elif not st.session_state["password_correct"]:
        st.markdown('<div class="password-box">', unsafe_allow_html=True)
        st.text_input("Enter the password", type="password", on_change=password_entered, key="password")
        st.markdown('</div>', unsafe_allow_html=True)
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

    # Load Data for Funds and Grants
    def load_funds_data():
        return pd.read_csv('funds_grants.csv')

    # LLM Query Function for Chatbot using new OpenAI API (ChatCompletion)
    def query_llm(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the GPT-3.5 turbo or any newer chat model
            messages=[{"role": "system", "content": "You are an assistant for farm licensing in Singapore."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()

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

    # Chatbot UI with styled input box
    st.markdown('<div class="chatbox">', unsafe_allow_html=True)
    user_query = st.text_input("Ask a question about licensing conditions:")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if user_query:
        prompt = f"The following are licensing conditions:\n{all_conditions}\n\nUser question: {user_query}\nAnswer:"
        llm_response = query_llm(prompt)
        
        # Styled chat response box
        st.markdown('<div class="chat-response">', unsafe_allow_html=True)
        st.write("Response:", llm_response)
        st.markdown('</div>', unsafe_allow_html=True)

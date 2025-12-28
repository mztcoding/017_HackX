import streamlit as st
import os
from google import genai
from home import show_home
from dashboard import show_dashboard
from dotenv import load_dotenv
load_dotenv()

## set up the environment
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

def setup_page():
    st.set_page_config(
    page_title="Mera Challan - Traffic AI Assistant",
    page_icon="🇵🇰",
    layout="wide",
    initial_sidebar_state="collapsed"
)
    
def main(client, MODEL_ID):
    # Initialize Routing State
    if 'current_view' not in st.session_state:
        st.session_state['current_view'] = 'landing'

    # Handle URL parameters (the code you provided earlier)
    if "page" in st.query_params and st.query_params["page"] == "main":
        st.session_state['current_view'] = 'main_app'
        if "nav" in st.query_params:
            st.session_state['nav_target'] = int(st.query_params["nav"])
        st.query_params.clear()

    # Routing
    if st.session_state['current_view'] == 'landing':
        show_home()
    else:
        # Pass the API client and Model ID to the dashboard
        show_dashboard(client, MODEL_ID)

if __name__ == '__main__':
    setup_page()
    
    # API Initialization
    api_key = os.environ.get('GOOGLE_API_KEY')
    client = genai.Client(api_key=api_key)
    MODEL_ID = "gemini-2.5-flash-lite" # Use current stable version
    
    main(client, MODEL_ID)




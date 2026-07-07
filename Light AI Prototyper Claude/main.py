import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Load API key from the .env file
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

st.title("🤝 CommunityLink: Nonprofit Request Router")
st.write("An AI-powered tool to categorize incoming community requests and draft responses.")

# Input text box
user_input = st.text_area("Paste the incoming email or request text here:", height=200)


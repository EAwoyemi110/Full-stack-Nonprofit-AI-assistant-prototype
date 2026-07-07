import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Load API key from the .env file
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
import streamlit as st
import anthropic
import os

# Load API key from the .env file

st.title("CommunityLink: Nonprofit Request Router")
st.write("An AI-powered tool to categorize incoming community requests and draft responses.")

api_key = st.secrets.get("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    st.error("🔑 **API Key Missing:** Please add your ANTHROPIC_API_KEY to the Streamlit Secrets dashboard.")
else:
    try:
        client = anthropic.Anthropic(api_key=api_key)
    except Exception as e:
        st.error(f"Initialization Error: {e}")

# Input text box
user_input = st.text_area("Paste the incoming email or request text here:", height=200)

if st.button("Process & Route Request"):
    if user_input:
        with st.spinner("Claude is analyzing and routing..."):
            # Constructing the structured system prompt
            system_instruction = (
                "You are an expert administrative assistant for a community nonprofit. "
                "Analyze the provided text and strictly output the following sections:\n"
                "### 1. URGENCY & CATEGORY\n[Assign Category: Crisis, Funding, Volunteer, or General]\n\n"
                "### 2. KEY METRICS & CONTACTS\n[Extract Name, Email, Phone, and Core Need]\n\n"
                "### 3. EXECUTIVE SUMMARY\n[A 2-sentence summary of the request]\n\n"
                "### 4. DRAFT RESPONSE\n[Write a professional, empathetic initial email draft]"
            )

            try:
                # Call Claude API
                message = client.messages.create(
                    model="claude-3-5-sonnet-latest",
                    max_tokens=1000,
                    system=system_instruction,
                    messages=[{"role": "user", "content": user_input}]
                )


                # Display results
                st.success("Analysis Complete!")

                # Pull out the text content safely
                response_text = "".join([block.text for block in message.content if block.type == "text"])
                st.markdown(response_text)


            except Exception as e:
                st.error(f"An API error occured: {e}")
                st.info("If you see a 404, your API key is invalid or no credits")
    else:
        st.warning("Please paste some text first.")
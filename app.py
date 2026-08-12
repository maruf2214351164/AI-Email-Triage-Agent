import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
if api_key:
    client = Groq(api_key=api_key)
else:
    st.error("API Key not found! Please check your .env file.")

# Configure Streamlit page UI
st.set_page_config(page_title="AI Email Triage Agent", page_icon="✉️", layout="wide")

st.title("✉️ AI Email Inbox Triage Agent")
st.write("A professional AI Agent that automates corporate inbox sorting, intent classification, and immediate draft replies.")

# User Input Section
st.subheader("📥 Paste an incoming email to test:")
email_from = st.text_input("From (Sender Email):", "client@example.com")
email_subject = st.text_input("Subject:", "Urgent request regarding my account")
email_body = st.text_area("Email Body:", height=150)

# Run Agent Button
if st.button("Analyze Email With AI Agent 🚀"):
    if not email_body.strip():
        st.warning("Please do not leave the email body empty.")
    else:
        with st.spinner("AI Agent is analyzing the email structure..."):
            # Prompt Engineering for the AI Agent
            prompt = f"""
            You are an expert Email Inbox Triage Agent. Analyze the following email:
            From: {email_from}
            Subject: {email_subject}
            Body: {email_body}
            
            Provide your response strictly in the following structured format using clean Markdown:
            ### 📊 Analysis Result
            - **Intent/Category:** [Identify if it is Support, Sales, or Spam]
            - **Urgency Level:** [High, Medium, or Low]
            - **Reasoning:** [Briefly explain why you categorized it this way in 1 sentence]
            
            ### 📝 Drafted Reply
            [Write a highly professional, polite, and contextual response matching the intent. Sign off as 'AI Support Assistant']
            """
            
            try:
                # Call Groq API with Llama-3.3 model
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                )
                
                # Display output on UI with proper list index fixing
                st.success("Analysis Completed Successfully!")
                st.markdown(chat_completion.choices[0].message.content)
                
            except Exception as e:
                st.error(f"An error occurred during processing: {e}")

# Sidebar Portfolio Info
st.sidebar.title("About This Project")
st.sidebar.info(
    "This AI Agent leverages the Groq API and Streamlit to automatically categorize corporate emails, "
    "detect urgency, and auto-draft immediate responses to optimize business operations."
)
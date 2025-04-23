import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="MAIP - My AI Partner", page_icon="🤖", layout="centered")

st.title("🤖 MAIP — My AI Partner")
st.markdown("Your personal assistant for building smart, powerful tools right on your machine.")

# User input
user_input = st.text_input("What would you like MAIP to help you with today?", "")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are MAIP, an AI assistant helping Kenneth with projects and building tools."},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response.choices[0].message.content
            st.success("Here’s what MAIP suggests:")
            st.write(answer)
        except Exception as e:
            st.error(f"Something went wrong: {e}")

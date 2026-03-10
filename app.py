from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FIXED HERE
model = genai.GenerativeModel("gemini-2.5-flash")

def output(query):
    response = model.generate_content(query)
    return response.text

# UI
st.set_page_config(page_title="Query_Bot")
st.header("Query_Bot")

user_input = st.text_input("Input", key="input")
submit = st.button("Ask Your Query")

if submit:
    response = output(user_input)
    st.subheader("The Response is:")
    st.write(response)
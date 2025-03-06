import streamlit as st
import google.generativeai as genai

# Show title and description
st.markdown("""
    <style>
        body {
            background-color: black;
            color: white;
        }
        </style>
        """,unsafe_allow_html=True);
st.title("💬 Edurank ChatBot")
st.write(
    "Ask and Explore "
)

# Ask user for their Google API Key
gemini_api_key = st.text_input("Enter your Name", type="default")

if not gemini_api_key:
    st.info("Continue to Chat with Us")
else:
    try:
        # Set API Key
        genai.configure(api_key="AIzaSyBmDxl1NFY3Ic6FYTxsfS03aO6-oB8CwVQ")

        # Initialize chatbot model
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Updated Model Name

        # Session state for storing chat messages
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display existing messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat input field
        if prompt := st.chat_input("Ask me anything..."):
            # Store user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate a response using Gemini AI
            response = model.generate_content(prompt)

            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response.text)

            # Store response in session state
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Error: {e}")

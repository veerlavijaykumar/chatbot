import streamlit as st
import google.generativeai as genai

# Show title and description
st.title("💬 Gemini Chatbot")
st.write(
    "This is a simple chatbot that uses Google's Gemini AI to generate responses. "
    "To use this app, you need to provide a Google AI API key, which you can get [here](https://ai.google.dev/). "
)

# Ask user for their Google API Key
gemini_api_key = st.text_input("Enter your Name", type="default")

if not gemini_api_key:
    st.info("Please add your Google AI API key to continue.", icon="🗝️")
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

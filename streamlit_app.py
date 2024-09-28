import streamlit as st
import google.generativeai as genai

st.title("🎈 Cat Training App")

if st.button('Clear', type="primary"):
    st.session_state.chat_history.clear()

gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
model = None
if gemini_api_key:
    try:
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
        print('success')
    except Exception as e:
        print('error')
        st.error(f"An error occurred while setting up the Gemini model: {e}")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] 

for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

if user_input := st.chat_input("Type your message here..."):
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)

if model is not None:
    try:
        role = "your name is Mew, master of cat training"
        prompt = f"role = '{role}', user input: '{user_input}'"
        response = model.generate_content(prompt)
        bot_response = response.text
        st.write(bot_response)
        st.session_state.chat_history.append(("assistant", bot_response))
    except Exception as e:
        st.error(f"An error occurred while generating the response: {e}")

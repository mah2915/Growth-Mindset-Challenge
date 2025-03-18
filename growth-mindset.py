import streamlit as st
import requests
import re

st.sidebar.title("🌟 Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Daily Growth", "Daily Progress", "Create Account"])

st.sidebar.markdown("---")
st.sidebar.markdown("👩‍💻 Web Developer")
st.sidebar.markdown("👧 Created by: Maham Ali")


# Function to fetch a motivational quote from ZenQuotes API
def get_quote():
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return f"❝ {data[0]['q']} ❞\n\n— {data[0]['a']}"
        else:
            return "⚠️ Unable to fetch quote. Try again later!"
    except Exception as e:
        return f"⚠️ Error: {e}"

def is_string_valid(text):
    return bool(re.match("^[A-Za-z ]+$",text))

if menu == "Home":
    st.title("💡 Growth Mindset Challenge")
    st.subheader("Understanding a Growth Mindset")
    st.write("A growth mindset is about believing that skills and intelligence can improve with effort and practice. It helps in learning, overcoming obstacles, and staying motivated in a constantly evolving field like tech.")

elif menu == "Daily Growth":
    st.title("🌱 Daily Growth")
    st.subheader("Click the button below to get an inspirational quote.")

    if st.button("Motivate me!"):
        quote = get_quote()
        st.success(quote)

elif menu == "Daily Progress":
    st.title("📊 Daily Progress")
    st.subheader("Track how close you are to your goals!")

    goal = st.text_input("Enter your goal:")
    progress = st.slider("How much have you completed?", 0, 100, 0)

    st.progress(progress / 100)  # Display progress bar

    if progress == 100:
        st.success("🎉 Congratulations! You reached your goal!")
    else:
        st.success("🙌Keep Going!")

elif menu == "Create Account":
    st.title("Create Account")
    name = st.text_input("Enter your name")
    father_name = st.text_input("Enter your father name")
    message = st.text_input("Enter your message")
    if st.button("Done"):
        if not (is_string_valid(name) and is_string_valid(father_name) and is_string_valid(message)):
            st.error("⚠️ Please enter valid text (only alphabets & spaces allowed).")
        else:
            st.toast("✅Account created successfully!")
            st.success("✅Account created successfully!")
            st.write(f"**Name:** {name}")
            st.write(f"**Father's Name:** {father_name}")
            st.write(f"**Message:** {message}")
import streamlit as st
import pyttsx3
import tempfile
import os

# Initialize TTS engine
engine = pyttsx3.init()

# Streamlit UI
st.set_page_config(page_title="Text to Speech App", layout="centered")
st.title("🗣️ Text to Speech Converter (Offline, No API Key)")

# Text input
text = st.text_area("Enter text to convert to speech:", height=200)

# Optional voice settings
rate = st.slider("Speech rate", 100, 300, 150)
volume = st.slider("Volume", 0.0, 1.0, 1.0)

# Update engine properties
engine.setProperty('rate', rate)
engine.setProperty('volume', volume)

# Convert and speak
if st.button("🔊 Convert and Play"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name
        engine.save_to_file(text, filename)
        engine.runAndWait()
        st.success("Speech generated successfully!")

        # Play audio
        with open(filename, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")

        # Download button
        with open(filename, "rb") as f:
            st.download_button(
                label="⬇️ Download Audio",
                data=f,
                file_name="speech.mp3",
                mime="audio/mp3"
            )

        # Cleanup temp file
        os.remove(filename)

# text-to-speech
# 🗣️ Text to Speech Converter (Offline, No API Key)

This is a simple yet effective offline Text-to-Speech (TTS) converter built using Streamlit and `pyttsx3`. This application allows users to convert any entered text into spoken audio without needing an internet connection or any external API keys, ensuring privacy and accessibility.

## ✨ Features

* **Offline Conversion**: No internet connection required for text-to-speech conversion.
* **No API Key Needed**: Utilizes the `pyttsx3` library for local speech synthesis.
* **Adjustable Speech Rate**: Users can control how fast or slow the speech is.
* **Adjustable Volume**: Customize the output volume of the speech.
* **Instant Playback**: Listen to the generated speech directly within the app.
* **Download Audio**: Download the converted speech as an MP3 file.
* **User-Friendly Interface**: Built with Streamlit for a clean and intuitive user experience.

## 🛠️ Technologies Used

* **Python**: The core programming language.
* **Streamlit**: For creating the interactive web application.
* **`pyttsx3`**: An offline text-to-speech conversion library for Python.
* **`tempfile`**: For creating temporary files to store generated audio.
* **`os`**: For operating system interactions, specifically for cleaning up temporary files.

## 💡 Usage

1.  **Enter Text**: Type or paste the text you want to convert into speech in the provided text area.
2.  **Adjust Settings**: Use the "Speech rate" and "Volume" sliders to customize the speech output.
3.  **Convert and Play**: Click the "🔊 Convert and Play" button to generate the speech and play it.
4.  **Download**: After conversion, a "⬇️ Download Audio" button will appear, allowing you to save the `.mp3` file to your device.

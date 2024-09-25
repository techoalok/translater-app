import streamlit as st
from langdetect import detect
from googletrans import Translator, LANGUAGES

# Function to detect and translate text
def detect_and_translate(text, target_lang):
    try:
        # Detect language
        detected_lang = detect(text)
        
        # Translate language using googletrans Translator
        translator = Translator()
        translated_text = translator.translate(text, dest=target_lang).text

        return detected_lang, translated_text
    except Exception as e:
        return str(e), None

# Streamlit UI
st.title("Language Translator")

# Input Text Box
text = st.text_area("Enter text to translate", height=150)

# Language Selection Dropdown using googletrans supported languages
target_lang = st.selectbox("Select target language", options=list(LANGUAGES.keys()), format_func=lambda x: LANGUAGES[x])

# Translate Button
if st.button("Translate"):
    if text and target_lang:
        detected_lang, translation = detect_and_translate(text, target_lang)
        if translation:
            st.subheader("Detected Language:")
            st.write(LANGUAGES.get(detected_lang, "Unknown"))
            
            st.subheader("Translation:")
            st.write(translation)
        else:
            st.error("An error occurred during translation.")
    else:
        st.error("Please enter text and select a target language.")

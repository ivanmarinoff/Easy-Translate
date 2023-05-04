from easygoogletranslate import EasyGoogleTranslateOne
import streamlit as st

st.set_page_config(page_title="EasyGoogleTranslator", page_icon=":robot:")
st.header("Easy Google Translator")
col1, col2 = st.columns(2)

with col1:
    st.markdown("Unofficial Google Translate API. This library does not need an api key or something else to use, "
                "it's free and simple."
                "You can either use a string  to translate but the text must be equal to or less than 5000 "
                "character.Google Translate supports 108 "
                "different languages.In application you will detect just 12 of them"
                "You can use any of them as source and target language in this application."
                "The source language is not specified, it is language is automatic."                
                " \n\n View Source Code on [Github](https://github.com/ivanmarinoff/Easy-Translate)")

    option_language = st.selectbox(
        '## Which Language would you like translate?',
        ('bg', 'en', 'fr', 'nl', 'de', 'es', 'it', 'pt', 'ru', 'tr', 'zh', 'ja'))

    st.markdown("## Enter Your Text To Translate")


def get_text():
    input_text = st.text_area(label="Insert text:", label_visibility='collapsed', placeholder="Translated text...",
                              key="text_input")
    return input_text


text_input = get_text()

if len(text_input.split(" ")) > 700:
    st.write("Please enter a shorter text. The maximum length is 700 words.")
    st.stop()


def update_text_with_example():
    print("Translated...")
    # st.session_state.text_input = "Your translated text"


st.button("*See An Example*", type='secondary', help="Click to see an example of the text you will be translated.",
          on_click=update_text_with_example)
translator = EasyGoogleTranslateOne(
    source_language='auto',
    target_language=option_language,
    timeout=None
)

st.markdown("### Your translated text:")
result = translator.translate(text_input)
st.write(result)


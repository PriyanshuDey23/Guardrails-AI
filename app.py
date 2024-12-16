import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from guardrails import Guard, OnFailAction, Validator, register_validator
from profanity_check import predict

# Load API key from environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Custom profanity-free validator using profanity_check
@register_validator(name="is-profanity-free", data_type="string")
class IsProfanityFree(Validator):
    def validate(self, key, value, schema, context=None) -> dict:
        prediction = predict([value])
        if prediction[0] == 1:
            raise ValueError(f"Value '{value}' contains profanity language.")
        return schema

# Set up Guardrails with the profanity check validator
guard = Guard().use_many(
    IsProfanityFree()  # Adding the profanity-free validation
)

# Function to translate text without Guardrails
def without_guardrails(text: str, target_language: str = "en") -> str:
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    chat_session = model.start_chat(history=[])
    message = f"Translate the following text to {target_language}: {text}"
    response = chat_session.send_message(message)
    return response.text.strip()

# Function to translate text with Guardrails
def with_guardrails(text: str, target_language: str = "en") -> str:
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    chat_session = model.start_chat(history=[])

    # Generate translation
    message = f"Translate the following text to {target_language}: {text}"
    response = chat_session.send_message(message)
    translation = response.text.strip()

    # Validate translation using the Guardrails system
    try:
        guard.validate(translation)  # Validate the translation with Guardrails
        return translation
    except Exception as e:
        return f"Guardrails validation failed: {str(e)}"

# Streamlit app
def main():
    st.title("Guardrails Translation App")

    text_area = st.text_area("Enter the Text You Want to Translate")
    target_language = st.text_input("Target Language (e.g., en, es, fr, de)", "en")

    if st.button("Translate"):
        if len(text_area.strip()) > 0:
            st.info(f"Original Text: {text_area}")

            # Translation without Guardrails
            st.warning("Translation Without Guardrails")
            try:
                without_guardrails_result = without_guardrails(text_area, target_language)
                st.success(f"Without Guardrails: {without_guardrails_result}")
            except Exception as e:
                st.error(f"Translation failed (without Guardrails): {str(e)}")

            # Translation with Guardrails
            st.warning("Translation With Guardrails")
            try:
                with_guardrails_result = with_guardrails(text_area, target_language)
                st.success(f"With Guardrails: {with_guardrails_result}")
            except Exception as e:
                st.error(f"Translation failed (with Guardrails): {str(e)}")

if __name__ == "__main__":
    main()

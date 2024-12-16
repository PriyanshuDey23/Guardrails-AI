
# Guardrails Translation App

This is a Streamlit application that translates text from one language to another with and without the use of Guardrails. The app uses the Google Generative AI model for text translation, along with custom toxic language validation to ensure the quality and appropriateness of the translation.

## Features

- **Text Translation without Guardrails**: Translates text directly using the Google Generative AI model.
- **Text Translation with Guardrails**: Translates text while validating the translation for toxic language using a custom profanity-checking validator.
- **Custom Toxic Language Validator**: A profanity check is implemented to detect and reject translations with offensive or inappropriate language.
- **Interactive Web Interface**: The app allows users to input text and specify the target language for translation.

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.x
- An active Google API key for Generative AI access

### Step 1: Clone the repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/PriyanshuDey23/Guardrails-AI.git
```

### Step 2: Install Dependencies

Navigate to the project directory and install the required dependencies using `pip`:

```bash
cd guardrails-translation-app
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the project root directory and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### Step 4: Run the Application

To start the Streamlit app, run the following command:

```bash
streamlit run app.py
```

The application should now be live at `http://localhost:8501` in your web browser.

## Usage

1. **Enter the text** you want to translate in the "Enter the Text You Want to Translate" text area.
2. **Specify the target language** (e.g., `en`, `es`, `fr`, `de`) in the "Target Language" input field.
3. **Click "Translate"** to view two outputs:
   - **Without Guardrails**: A direct translation of the text.
   - **With Guardrails**: A translation with toxic language validation. If the translation contains inappropriate language, it will be rejected.

## Example Use Case

### Translation Without Guardrails

Original Text: `"I hate this!"`

- Translates directly without validation.

### Translation With Guardrails

Original Text: `"I hate this!"`

- The translation is checked for toxic language. If it exceeds the toxicity threshold, the app will display an error message: `"Guardrails validation failed: Toxic language detected in the text."`

## Development

To contribute to this project:

1. Fork the repository.
2. Create a new branch.
3. Make changes and test them.
4. Open a pull request with a clear description of your changes.

### Testing

- The app uses the `profanity-check` library to validate content. The translation is rejected if the predicted toxicity exceeds a specified threshold.

### Customizing the Toxicity Threshold

If you want to modify the sensitivity of the toxic language validator, adjust the threshold in the `ToxicLanguageValidator` class:

```python
class ToxicLanguageValidator:
    def __init__(self, threshold=0.5):
        self.threshold = threshold
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Google Generative AI** for providing the translation model.
- **Profanity Check** for the language validation functionality.
- **Streamlit** for providing the easy-to-use framework for building interactive web applications.


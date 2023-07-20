from marianmt import MarianMT
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

def translate_french_to_english_with_marianmt(text):
    # Inititalize the MarianMT model for translation
    nmt_model = ("opus-mt-fr-en")

    # Use  the NMT model to get the neural machine translation
    nmt_translation, confidence_scores = nmt_model.translate(text, return_scores=True)

    return nmt_translation, confidence_scores

def detect_language(text):
    try:
        language_code = detect(text)
        return language_code
    except LangDetectException

def main():
    print("Welcome to French to English Translator using MarianMT!")
    print("Type 'exit' to quit.\n") 

    while True:
        input_text = input("Enter the French text you want to translate: ")

        if input_text.lower() == "exit":
            break

        # Detect the input language
        detected_language = detect_language(input_text)

        if detected_language and detected_language == "fr":
            # Translate the input text
            nmt_translation, confidence_scores = translate_french_to_english_with_marianmt(input_text)

            print("\nDetected Language:", detected_language)
            print("Neural Machine Translation (French to English):", nmt_translation)
            print("Confidence Scores:", confidence_scores)
        else:
            print("\nError: Please enter a valid French text.")
if __name__ == "__main__":
    main()                 

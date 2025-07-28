import os
import language_tool_python #an open-source grammar checker that supports many languages
from langdetect import detect
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()
client = OpenAI() 

def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'
    
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# load the text file
text = read_file('example.txt')
detected_language = detect_language(text)
print(f'the language uesd in the text is {detected_language}')

LANG_MAP = {
    "en": "en-US",
    "fr": "fr",
    "de": "de",
    "ar": "ar",
    "es": "es",
    "it": "it",
    "pt": "pt",
    "nl": "nl"
}

lt_code = LANG_MAP.get(detected_language, 'en-US') #get the language
tool = language_tool_python.LanguageTool(lt_code) # create the grammar checker
print(f'Grammar detector set for: {lt_code}')

# find grammar issue 
matches = tool.check(text)

# show grammar issuees
print(f'\nFound {len(matches)} issues:\n')
for match in matches:
    print(f'problem: {match.message}')
    print(f'suggestion: {match.replacements}')
    print(f'sentence: {match.context}\n')

#auto-correct the text 
corrected_text = tool.correct(text)

def improved_text_with_openai(text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that rewrites text to sound more natural, clear, and professional without changing its meaning."},
                {"role": "user", "content": text}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f'[Warning] AI enhancement failed: {e}')
        return text  # Return original text as fallback

choice = input('do you want the AI to enhance the writing style? (yes/no): ').strip().lower()
if choice == 'yes':
    improved = improved_text_with_openai(corrected_text)
    with open('enhanced.txt', 'w', encoding='utf-8') as f:
        f.write(improved)
        print('\n AI-enhnanced saved to "enhanced.txt"')
else:
    with open('corrected.txt', 'w', encoding='utf-8') as f:
        f.write(corrected_text)
        print('\n corrected version saved to "corrected.txt"')
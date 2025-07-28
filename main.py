import language_tool_python #an open-source grammar checker that supports many languages
from langdetect import detect
def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'
    
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# load the text file
text = read_file('arabic.txt')
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

# create the grammar checker
lt_code = LANG_MAP.get(detected_language, 'en-US')
tool = language_tool_python.LanguageTool(lt_code)
print(f'Grammar detector set for: {lt_code}')

# find grammar issue 
matches = tool.check(text)

# show grammar issuees
print(f'\nFound {len(matches)} issues:\n')
for match in matches:
    print(f'problem: {match.message}')
    print(f'suggestion: {match.replacements}')
    print(f'sentence: {match.context}\n')

#auto-correct the the text 
corrected_text = tool.correct(text)

# save corrected version
with open('corrected.txt', 'w', encoding='utf-8') as f:
    f.write(corrected_text)

print(f"\n Grammar correction completed. saved to 'corrected.txt'")
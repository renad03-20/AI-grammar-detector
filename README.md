# GrammarFixAI 📝✨

GrammarFixAI is a simple Python-based tool that improves and corrects grammar in your text using OpenAI's GPT model. It loads text from a `.txt` file, enhances it using the GPT API, and saves the result in a new file.

---

## 🚀 Features

- Enhances grammar and clarity using OpenAI GPT
- Uses `.env` file to manage API keys securely
- Simple CLI interface
- Virtual environment setup included

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/renad03-20/AI-grammar-detector
cd GrammarFixAI
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ Never share your API key or commit the `.env` file to version control.

---

## 💻 How to Use

1. Prepare a text file called `example.txt` in the root directory with the content you want to enhance.

2. Run the script:

```bash
python main.py
```

3. The output will be saved in a file called `corrected.txt`.

---

## 📄 File Structure

```
GrammarFixAI/
│
├── .env # Stores your OpenAI API key (DO NOT SHARE)
├── .gitignore # Tells Git to ignore .env and venv
├── main.py # Main Python script
├── example.txt # Input text file for testing
├── corrected.txt # Output file with grammar fixes
├── enhanced.txt # Output file with AI enhancements
├── arabic.txt # Sample input in Arabic (optional)
├── requirements.txt # List of required Python packages
├── README.md # Project documentation (you are here 💁‍♀️)
└── venv/ # Python virtual environment (not tracked by Git)
```

---

## 🧠 Built With

- [Python 3.13+](https://www.python.org/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚠️ Troubleshooting

- **API Key Errors**: Ensure your `.env` file exists and `OPENAI_API_KEY` is set.
- **Quota Errors**: You may have exceeded your OpenAI API limit. Check usage at [OpenAI Usage Dashboard](https://platform.openai.com/account/usage).
- **Module Errors**: Be sure you're using the latest version of the OpenAI SDK (`pip install --upgrade openai`).

---

## 📜 License

This project is for personal and educational use.

---

## 🙋‍♀️ Author

Created by [Rinad](https://github.com/renad03-20)

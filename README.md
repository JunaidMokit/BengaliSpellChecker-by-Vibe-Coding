# Bengali Spell Checker by Vibe Coding

A powerful AI-powered Bengali Spell Checker web application built with Django. This tool helps users identify spelling errors in Bengali text and provides context-aware suggestions using accurate dictionary lookups and edit-distance algorithms.

## 🚀 Features

- **Real-time Spell Checking**: Instantly detects incorrect Bengali words.
- **Smart Suggestions**: Provides closest correct word suggestions using Levenshtein distance.
- **Comprehensive Dictionary**: Powered by a large database of over 450,000 Bengali words.
- **Clean UI**: A simple, user-friendly interface designed for ease of use.
- **REST API**: Includes an API endpoint for integrating spell checking into other applications.

## 🛠 Tech Stack

- **Backend**: Python, Django 6.0
- **Algorithm**: Levenshtein Distance (for suggestions)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Data**: Custom Bengali Word List

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/JunaidMokit/BengaliSpellChecker-by-Vibe-Coding.git
   cd BengaliSpellChecker-by-Vibe-Coding
   ```

2. **Create a virtual environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django python-Levenshtein
   ```

4. **Navigate to the Project Directory**
   ```bash
   cd BengaliSpellChecker
   ```

   *Note: Ensure `manage.py` is in the current directory.*

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the App**
   Open your browser and visit: `http://127.0.0.1:8000/`

## 📝 Usage

1. Enter or paste Bengali text into the text area.
2. Click the **Check Spelling** button.
3. Incorrect words will be underlined in red.
4. Hover over the red lines to see corrected spelling suggestions.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

[MIT](LICENSE)

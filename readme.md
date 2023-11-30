# Django Translator

Django Translator is a web application that allows users to translate words from one language to another using the Google Translate API. The application is built with Django and showcases the integration of Google Translate functionality.

## Features

- Translate words from one language to another.
- View translation history.
- Choose from a variety of supported languages.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Django
- googletrans==4.0.0-rc1 (Google Translate API)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arpanduari/DjangoTranslator.git
   ```

2. Nvaigate to the project directory:

   ```bash
   cd DjangoTranslator
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

The application should now be accessible at http://localhost:8000/

Or You can check [here](https://djangotranslator.onrender.com)

## Usage

1. Open the application in your web browser.
2. Enter a word in the "Input Word" field.
3. Choose the desired output language from the dropdown.
4. Click the "Translate" button to view the translation.
5. View translation history on the same page.

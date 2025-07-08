# Markdown to HTML Editor

A simple web application built with Flask that converts Markdown input into HTML with syntax highlighting and live preview.

---

## Features

- Live Markdown editing with instant HTML preview.
- Supports fenced code blocks, tables, smart lists, and other common Markdown extensions.
- Syntax highlighting for code blocks powered by Pygments.
- Clean, responsive, and minimalistic user interface.
- Easily extendable backend for additional Markdown extensions or custom rendering.

---

## Technologies Used

- **Backend:** Python, Flask
- **Markdown Parsing:** `markdown` Python library with extensions (`fenced_code`, `codehilite`, `tables`, etc.)
- **Syntax Highlighting:** Pygments via `codehilite` extension
- **Frontend:** HTML, CSS, and vanilla JavaScript (Fetch API for AJAX requests)
- **Styling:** Custom CSS with Google Fonts (Inter)

---

## Getting Started

1. Clone the repository
```bash
git clone https://github.com/DragonSenseiGuy/markdown-to-html.git
cd markdown-to-html
```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3.Install Requirements
```bash
pip install requirements.txt
```

4.Run the Flask application:

```bash
python main.py
```

3. Open your browser and navigate to:

```
http://127.0.0.1:5000/markdown
```

## Project Structure

```
.
├── main.py              # Flask backend server
├── templates/
│   └── markdown.html    # HTML template for the editor page
└── static/
    └── markdown.css     # Stylesheet for the editor UI
```

---

## Usage

* Enter any Markdown text in the left textarea.
* The application sends the Markdown content to the backend via AJAX.
* The backend converts the Markdown to HTML with syntax highlighting.
* The rendered HTML is displayed live on the right pane.

---

## License

This project is open source and available under the MIT [LICENSE](LICENSE).

---

## Acknowledgments

* [Flask](https://flask.palletsprojects.com/)
* [Python-Markdown](https://python-markdown.github.io/)
* [Pygments](https://pygments.org/)
* [Google Fonts](https://fonts.google.com/specimen/Inter)

---

Feel free to contribute or report issues!
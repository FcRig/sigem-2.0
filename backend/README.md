# Backend

Python backend using Flask for scraping with session management and authentication.

## Structure

- **app/main.py** – Flask application instance
- **app/auth/** – authentication routes and utilities
- **app/scraper/** – scraping logic using `requests`
- **requirements.txt** – Python package requirements

## Development

Create a virtual environment, install dependencies, and run the application:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app.main run
```

## API

- `POST /auth/register` – create a new user with `username` and `password`
- `POST /auth/login` – obtain a token using credentials

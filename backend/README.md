# Backend

Python backend using FastAPI for scraping with session management and authentication.

## Structure

- **app/main.py** – FastAPI application instance
- **app/auth/** – authentication routes and utilities
- **app/scraper/** – scraping logic using `requests`
- **requirements.txt** – Python package requirements

## Development

Create a virtual environment, install dependencies, and run the application.
The `setup.sh` script prepares the environment for you:

```bash
./setup.sh
uvicorn app.main:app --reload
```

## API

- `POST /auth/register` – create a new user with `username` and `password`
- `POST /auth/login` – obtain a token using credentials

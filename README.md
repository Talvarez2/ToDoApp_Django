# ToDoApp Django

A simple To Do application built with [Django](https://www.djangoproject.com/).

## Prerequisites

- Python 3.6+
- pip

## Setup

```sh
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

Visit http://localhost:8000 to use the app.

## Configuration

All settings are configurable via environment variables:

| Variable | Default | Description |
|---|---|---|
| `DJANGO_SECRET_KEY` | dev-only key | Secret key for cryptographic signing |
| `DJANGO_DEBUG` | `True` | Enable/disable debug mode |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated allowed hosts |
| `DB_ENGINE` | `django.db.backends.sqlite3` | Database backend |
| `DB_NAME` | `db.sqlite3` | Database name/path |
| `DB_USER` | _(empty)_ | Database user |
| `DB_PASSWORD` | _(empty)_ | Database password |
| `DB_HOST` | _(empty)_ | Database host |
| `DB_PORT` | _(empty)_ | Database port |

For production, set `DJANGO_SECRET_KEY` to a strong random value and `DJANGO_DEBUG=False`.

### Using PostgreSQL

```sh
export DB_ENGINE=django.db.backends.postgresql
export DB_NAME=todo_app
export DB_USER=your_user
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_PORT=5432
```

## Deployment

The app includes a `Procfile` for Heroku deployment with gunicorn and whitenoise for static files.

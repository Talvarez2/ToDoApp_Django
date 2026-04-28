# AGENTS.md

## Project Overview

Django-based To Do application. Users can add and delete to-do items via a web interface.

## Project Structure

```
ToDoApp/             # Django project settings
  settings.py        # Configuration (env-var driven)
  urls.py            # Root URL routing
  wsgi.py            # WSGI entry point
ToDo/                # Main app
  models.py          # Todo model
  views.py           # index, add_todo, delete_todo views
  urls.py            # App URL routing (namespace: 'todo')
  admin.py           # Admin registration
  templates/         # Django templates (Bootstrap 4)
    template.html    # Base template
    ToDo/index.html  # Main page
  static/css/        # Custom CSS
  migrations/        # Database migrations
```

## How to Run

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Key Conventions

- Settings are driven by environment variables (no hardcoded secrets)
- Database defaults to SQLite for development; set `DB_ENGINE` for PostgreSQL
- Views use `@require_POST` for state-changing endpoints
- URL namespace is `todo` (e.g., `{% url 'todo:index' %}`)
- Templates extend `template.html` as the base layout
- URLs use trailing slashes per Django convention

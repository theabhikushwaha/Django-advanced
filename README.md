# Django-advanced

A personal learning repository for practicing Django. It contains a small Django website alongside notes and reference material collected while learning Django and Python.

## Project contents

- `core/` — the Django project and website code. `manage.py` is inside this directory.
- `core/accounts/` — accounts app.
- `core/home/` — home app.
- `core/model/` — model/student app; its routes are mounted at `/student/`.
- `core/recipe/` — recipe app.
- `core/db.sqlite3` — the configured SQLite database file.
- `core/static/` and `core/media/` — static and uploaded media locations configured by the project.
- `notebook/` — learning notes grouped into folders such as `django`, `python`, `template`, and `command`.

The main URL configuration currently connects the home page at `/`, the admin at `/admin/`, accounts at `/accounts/`, student/model pages at `/student/`, and recipes at `/recipe/`.

## Run locally

You need Python and Django installed in the Python environment you use for this project. No dependency manifest (such as `requirements.txt`) is currently included.

From the repository root, run:

```powershell
cd core
python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000/> in a browser. To run the project’s Django tests, use `python manage.py test` from the `core/` directory.

## Development status

This repository is for learning and local development, not production deployment. The current Django settings have `DEBUG = True` and use a development secret key; review and replace development settings before deploying the project.

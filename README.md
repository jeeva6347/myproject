# myproject — Deploying to Render.com

This repository is prepared for deployment on Render.com. Below are the exact build and start commands, required environment variables, and quick troubleshooting notes.

## Recommended Render settings

- Build Command (recommended)
  ```bash
  ./build.sh
  ```
  This script installs requirements, runs `collectstatic` and `migrate`, and prints debug info.

- Start Command (recommended)
  ```bash
  gunicorn app:application --log-file -
  ```
  The repo includes a top-level `app.py` wrapper so Gunicorn can import the inner Django package regardless of working directory.

> Note: If you prefer to use the Procfile, leave the Start Command blank in Render — Render will use the `Procfile` which already contains `web: gunicorn app:application --log-file -`.

## Required environment variables

- `SECRET_KEY` — set a secure production secret key (do not use the hardcoded secret in `settings.py`).
- `DATABASE_URL` — provided automatically if you attach a Render PostgreSQL instance; otherwise set to your DB connection URL.
- `PYTHON_VERSION` — set to `3.13.4` to match the development environment (optional but recommended).
- `DJANGO_SETTINGS_MODULE` — `myproject.settings` (optional; the project sets this in `manage.py`/`build.sh`/`app.py`).

## Local development

Use `requirements.dev.txt` for local installs on Windows (it omits `psycopg2-binary`):

```powershell
.\env\Scripts\Activate.ps1
pip install -r requirements.dev.txt
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runserver
```

If you want full production dependencies locally (including `psycopg2-binary`) you'll need PostgreSQL development headers available (`pg_config`) for your platform.

## Troubleshooting

- ModuleNotFoundError: No module named `myproject.wsgi` — ensure the Start Command uses `app:application` or `--chdir myproject` so the inner package is importable.
- psycopg2 build errors on Windows — use `requirements.dev.txt` locally or install PostgreSQL dev tools so `pg_config` is on PATH.
- collectstatic warnings about missing `myproject/static` — create that directory if your project needs custom static files.

If you run into any build or deploy errors on Render, paste the build log here and I will help diagnose.

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Ensure the inner project package is on sys.path so
    # `myproject.settings` can be imported when manage.py is executed
    # from the repository root (Render runs commands from the repo root).
    repo_root = os.path.dirname(os.path.abspath(__file__))
    inner_project_path = os.path.join(repo_root, 'myproject')
    if inner_project_path not in sys.path:
        sys.path.insert(0, inner_project_path)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

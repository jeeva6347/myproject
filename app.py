import os
import sys

# Make sure the inner project folder is on sys.path so imports like
# `myproject.wsgi` and `myproject.settings` resolve when Gunicorn runs
# from the repo root.
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
INNER = os.path.join(REPO_ROOT, 'myproject')
if INNER not in sys.path:
    sys.path.insert(0, INNER)

# Ensure DJANGO_SETTINGS_MODULE is set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Expose the WSGI application
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

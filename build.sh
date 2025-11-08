#!/usr/bin/env bash

# Exit on error
set -o errexit

# Install Python dependencies
echo "Installing Python dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

# Set environment variables
export PYTHONPATH="/opt/render/project/src/myproject:${PYTHONPATH:-}"
export DJANGO_SETTINGS_MODULE=myproject.settings

echo "Current directory: $(pwd)"
echo "Python path: $PYTHONPATH"
echo "Settings module: $DJANGO_SETTINGS_MODULE"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run migrations
echo "Running database migrations..."
python manage.py migrate

echo "Build completed successfully!"
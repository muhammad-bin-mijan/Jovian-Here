# Jovian-Here

## Overview
A backend learning project built with Python and Flask. Started as an empty
imported repo; set up as a small REST API to practice backend web development
fundamentals (routing, JSON responses, request handling).

## Stack
- Python 3.11
- Flask (see `pyproject.toml` for dependencies)

## Structure
- `main.py` — Flask app with example routes:
  - `GET /` — welcome message and list of available endpoints
  - `GET /api/tasks` — list all tasks (in-memory sample data)
  - `GET /api/tasks/<id>` — get a single task
  - `POST /api/tasks` — create a task (JSON body: `{"title": "..."}`)

## Running
The "Start application" workflow runs `python main.py`, which starts the
Flask dev server on `0.0.0.0:5000` (visible in the Replit preview pane).

## User preferences
- Backend project in Python (confirmed by user on 2026-07-15).

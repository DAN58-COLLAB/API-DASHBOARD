# API Dashboard

A beginner-friendly FastAPI project that exposes a small service-status summary through JSON endpoints.

## Features
- `GET /` returns a welcome message.
- `GET /api/summary` reports total, online and offline services, plus a breakdown by protocol.
- Interactive API documentation is available through FastAPI's Swagger UI.

## Requirements
- Python 3.9+
- FastAPI
- Uvicorn

## Setup and run

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` to test the endpoints.

## Example response

`/api/summary` returns fields for `total_services`, `online`, `offline` and `protocols`.

## Project scope
The service list is hard-coded in memory. It is a learning project, not a live uptime monitor, and it does not store data between restarts.

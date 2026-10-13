# FastAPI Project Boilerplate

Reusable FastAPI starter with async SQLAlchemy/PostgreSQL, Alembic migrations, Docker Compose, environment-based settings, health endpoints, tests, and Ruff.

## Quick start

Requirements: Python 3.12+, uv, and Docker.

```bash
cp .env.example .env
uv sync --dev
docker compose up -d db
uv run alembic upgrade head
uv run uvicorn app.main:app --reload
```

API docs: http://127.0.0.1:8000/docs

Health endpoints: `GET /health/live` and `GET /health/ready`.

## Common commands

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run alembic revision --autogenerate -m "describe change"
uv run alembic upgrade head
```

Never commit `.env` or secrets. Authentication is not included; add auth, authorization, rate limiting, observability, TLS, and production-specific settings before deploying.

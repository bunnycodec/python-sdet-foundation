# Week 2 — Mini API Test Framework

## Overview

This folder contains a small, reusable API testing framework built for Week 2 of the course. It provides a lightweight API client, centralized configuration, and custom response assertions to make writing and running API tests with pytest simple and consistent.

## Tech / Requirements

- Python 3.8+
- pytest
- requests

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Project structure

- `assertions/` — custom response assertion helpers (response_assertions.py)
- `client/` — small HTTP client wrapper used by tests (api_client.py)
- `config/` — configuration loader for base URL and timeouts (config.py)
- `tests/` — pytest tests for the sample API (test_posts.py)
- `requirements.txt` — pinned dependencies for the framework

## Configuration

Default configuration lives in `config/config.py`. You can override the API base URL at runtime with the `API_BASE_URL` environment variable, for example:

```bash
export API_BASE_URL=https://jsonplaceholder.typicode.com
```

## How to run tests

Run the full test suite from this folder:

```bash
pytest -q
```

Run a single test file or test function:

```bash
pytest tests/test_posts.py
pytest tests/test_posts.py::test_get_posts -q
```

## Quick usage notes

- Use `client/api_client.py` to perform requests in tests via a simple wrapper (GET/POST helpers).
- Use `assertions/response_assertions.py` to assert response status codes and JSON shapes consistently.
- Keep configuration values in `config/config.py` and override with environment variables when running tests.

## Contributing

Keep tests small and focused. Add new assertion helpers to `assertions/` when a check is reused across tests.

## License

See project root LICENSE.

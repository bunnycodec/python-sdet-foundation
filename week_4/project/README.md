# Week 4 Project – Fake Store API Tests

## 📌 Project Overview

This repository contains a simple API testing project built during Week 4 of the Python SDET Foundation Learning. The tests interact with the Fake Store API, exercising endpoints for products, orders, and users. The aim of the project is to demonstrate API automation using **pytest** along with custom builders, fixtures and data handling utilities.

## 🚀 Installation & Running

1. **Clone the repo** and navigate to the `week_4/project` folder.
2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies (there is a small `requirements.txt` in the project root):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the test suite from the project directory:
   ```bash
   pytest -v
   ```
5. For coverage reports you can use:
   ```bash
   coverage run -m pytest && coverage html
   ```
   then open `htmlcov/index.html` in a browser.

## ✅ Test Coverage Summary

- The suite includes unit tests for builders and utility functions as well as end‑to‑end API tests against the Fake Store service.
- Typical coverage runs in the high‑80s to low‑90s percent range, depending on which modules are exercised.
- Coverage reports are generated with `coverage` and can be inspected with the HTML output above. Key areas covered:
  - Request/response assertions
  - Data builders for products and orders
  - Fixture behaviour for session management

## ⚠️ Known Limitations

The Fake Store API is a public mock service and exhibits some non‑production behaviour:

- **Unreliable data persistence** – POST/PUT operations may succeed but the data is not always retained.
- **Inconsistent ID generation** – resource IDs returned by the API can change or collide unexpectedly.
- **Rate limiting and downtime** – the service may throttle requests or be temporarily unavailable.

Because of these limitations, tests are designed to be resilient (e.g. not relying on long‑lived state) but occasional failures due to the API itself are expected.

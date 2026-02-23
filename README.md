# Python SDET Foundation

A comprehensive learning resource for building foundational skills in Software Development Engineer in Test (SDET) using Python.

## Overview

This repository contains structured problem statements and implementations covering core Python concepts essential for test automation and quality assurance engineering.

## Project Structure

```
src/
├── week_1/
│   ├── basics.py              # Log message parser
│   ├── functions.py           # API response validator
│   └── collections.py         # Test coverage comparator
│   └── problem_statements.md  # Week 1 challenges
```

## Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### Setup

```bash
# Clone the repository
git clone https://github.com/bunnycodec/python-sdet-foundation.git
cd python-sdet-foundation

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies (if any)
pip install -r requirements.txt
```

### Installation & Testing (macOS / Linux)

Follow these steps to create an isolated environment, install dependencies from `requirements.txt`, and run tests.

```bash
# create and activate virtualenv
python -m venv .venv
source .venv/bin/activate

# make sure pip is up-to-date
python -m pip install --upgrade pip

# install project dependencies
pip install -r requirements.txt

# run the test suite (uses pytest)
pytest -q
```

If you prefer pinned versions, update `requirements.txt` with exact versions (for example `requests==2.31.0`, `pytest==7.4.0`).

## Problem Statements

- **Log Parser** - Parse and categorize application log messages by severity level
- **API Response Validator** - Validate API responses based on status and response time
- **Test Coverage Comparator** - Compare and analyze UI/API test coverage

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## License

Licensed under MIT. See LICENSE file for details.

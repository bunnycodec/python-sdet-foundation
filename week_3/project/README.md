# API Testing Project

A comprehensive REST API testing suite using pytest, designed to validate CRUD operations and error handling for the GoRest API. This project demonstrates best practices in API automation testing, including fixtures, schema validation, and organized test structure.

## Overview

This project tests the [GoRest API](https://gorest.co.in/public/v2), a free fake REST API service that provides endpoints for managing users and posts. The test suite includes:

- **Users Management**: Create, read, update, and list users
- **Posts Management**: Create, read, update, and list posts
- **Negative Scenarios**: Authentication failures, validation errors, and 404 errors
- **Schema Validation**: JSON schema validation for API responses

## Project Structure

```
├── conftest.py              # Pytest configuration and fixtures
├── pytest.ini               # Pytest markers and settings
├── requirements.txt         # Python dependencies
├── schemas.py               # JSON schemas for validation
├── tests/
│   ├── test_users.py        # User CRUD operation tests
│   ├── test_posts.py        # Post CRUD operation tests
│   └── test_negative.py     # Negative scenario tests
└── README.md                # This file
```

## Technology Stack

- **Python 3.x**: Programming language
- **pytest**: Testing framework
- **requests**: HTTP client library
- **jsonschema**: JSON schema validation
- **Faker**: Fake data generation
- **pytest markers**: Test categorization (smoke, now)

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**:

   ```bash
   cd week_3/project
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up authentication token**:

   The project requires a valid GoRest API token for authenticated requests. Set it as an environment variable:

   ```bash
   export BEARER_TOKEN_GOREST="your_api_token_here"
   ```

   To get a token:
   - Visit [GoRest.co.in](https://gorest.co.in)
   - Sign up for a free account
   - Generate an API token from your profile

## Running Tests

### Run all tests:

```bash
pytest -v
```

### Run tests with detailed output:

```bash
pytest -v -s
```

### Run only smoke tests (quick sanity checks):

```bash
pytest -v -m smoke
```

### Run a single test file:

```bash
pytest tests/test_users.py -v
```

### Run a specific test:

```bash
pytest tests/test_users.py::test_create_user_201 -v
```

### Run tests and stop on first failure:

```bash
pytest -v -x
```

## Fixtures

The project includes the following pytest fixtures defined in `conftest.py`:

### Session-level Fixtures:

- **`base_url`**: The base URL of the GoRest API (`https://gorest.co.in/public/v2`)
- **`api_token`**: Bearer token from environment variable `BEARER_TOKEN_GOREST`
- **`auth_headers`**: Authorization headers with Bearer token

### Function-level Fixtures:

- **`api_client`**: A `requests.Session` object with authentication headers pre-configured
- **`created_user`**: Creates a test user and yields user data; automatically cleans up by deleting the user after test
- **`created_post`**: Creates a test post for a created user and yields post data; automatically cleans up

## Test Categories

### Test Markers

The project uses pytest markers to categorize tests:

- **`@pytest.mark.smoke`**: Quick sanity tests that validate core functionality
- **`@pytest.mark.now`**: Used when running or updating a single test

Run tests by marker:

```bash
pytest -m smoke -v  # Run only smoke tests
```

## Test Coverage

### Users Tests (`test_users.py`)

- `test_create_user_201`: Create a new user and verify response
- `test_read_user_200`: Retrieve a specific user and validate data
- `test_update_user_name_200`: Update user name
- `test_update_user_status_200`: Update user status
- `test_delete_user_204`: Delete a user and verify deletion with 404
- `test_user_schema`: Validate single user response against schema
- `test_user_list_schema`: Validate user list response against schema
- `test_create_user_schema`: Validate created user response against schema
- `test_pagination_validate_200`: Test pagination with page parameter
- `test_status_active_validate_200`: Filter users by active status
- `test_status_inactive_validate_200`: Filter users by inactive status
- `test_gender_validate_200`: Filter users by gender

### Posts Tests (`test_posts.py`)

- `test_create_post_201`: Create a new post
- `test_read_post_200`: Retrieve a specific post
- `test_update_post_title_200`: Update post title
- `test_update_post_body_200`: Update post body
- `test_delete_post_204`: Delete a post and verify deletion with 404
- `test_post_schema`: Validate single post response against schema
- `test_post_list_schema`: Validate post list response against schema
- `test_create_post_schema`: Validate created post response against schema
- `test_posts_specific_user_validate_200`: Get posts for a specific user
- `test_create_post_specific_user_200`: Create post using user-specific endpoint
- `test_missing_title_422`: Validate error when post title is missing
- `test_invalid_user_422`: Validate error when post user_id is invalid

### Negative Tests (`test_negative.py`)

- `test_no_auth_token_create_user`: Create user without authentication token (401)
- `test_create_user_invalid_token_401`: Create user with invalid token (401)
- `test_delete_user_no_auth_401`: Delete user without authentication token (401)
- `test_missing_email_422`: Validate error when email is missing (422)
- `test_missing_name_422`: Validate error when name is missing (422)
- `test_missing_user_id_422`: Validate error when user_id is missing from post (422)
- `test_invalid_email_422`: Validate error for invalid email format (422)
- `test_non_integer_user_id_422`: Validate error when user_id is not an integer (422)
- `test_get_non_existent_user_404`: Get non-existent user returns 404
- `test_update_non_existent_user_404`: Update non-existent user returns 404

## Schema Validation

The project includes JSON schemas for validating API responses:

### User Schema

- Required fields: `id`, `name`, `email`, `gender`, `status`
- All fields are strings except `id` which is an integer

### Post Schema

- Required fields: `id`, `user_id`, `title`, `body`
- Numeric fields: `id`, `user_id`
- String fields: `title`, `body`

Schemas are defined in `schemas.py` and used with `jsonschema.validate()` for response validation.

## Best Practices Implemented

1. **Fixture-based Setup/Teardown**: Uses pytest fixtures for test data creation and cleanup
2. **Reusable Clients**: Pre-configured `api_client` with authentication headers
3. **Schema Validation**: All responses validated against JSON schemas
4. **Unique Test Data**: Email addresses include UUID to ensure uniqueness
5. **Timeout Handling**: All requests include a 10-second timeout
6. **Proper HTTP Methods**: Uses correct REST methods (GET, POST, PATCH, DELETE)
7. **Error Response Testing**: Validates error codes and error messages
8. **Status Code Assertions**: Verifies exact HTTP status codes
9. **Response Data Validation**: Asserts returned data matches sent data
10. **Cleanup**: Automatic deletion of test resources after tests complete

## Troubleshooting

### Common Issues

**Issue**: `401 Unauthorized` errors

- **Solution**: Ensure `BEARER_TOKEN_GOREST` environment variable is set correctly
  ```bash
  export BEARER_TOKEN_GOREST="your_valid_token"
  pytest -v
  ```

**Issue**: `Connection timeout` errors

- **Solution**: Check internet connection and GoRest API availability
  ```bash
  curl https://gorest.co.in/public/v2/users
  ```

**Issue**: Tests fail with `ModuleNotFoundError`

- **Solution**: Ensure all dependencies are installed
  ```bash
  pip install -r requirements.txt
  ```

**Issue**: `AssertionError` in schema validation

- **Solution**: Check if the API response structure matches the schema definition in `schemas.py`

## Environment Variables

| Variable              | Description                     | Required |
| --------------------- | ------------------------------- | -------- |
| `BEARER_TOKEN_GOREST` | GoRest API authentication token | Yes      |

## API Endpoints

The tests validate the following endpoints:

### Users

- `POST /users` - Create new user
- `GET /users` - List users
- `GET /users/{id}` - Get specific user
- `PATCH /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

### Posts

- `POST /posts` - Create new post
- `GET /posts` - List posts
- `GET /posts/{id}` - Get specific post
- `PATCH /posts/{id}` - Update post
- `DELETE /posts/{id}` - Delete post

## Contributing

When adding new tests:

1. Follow existing naming conventions: `test_<action>_<expected_status_code>`
2. Use appropriate markers (`@pytest.mark.smoke`, etc.)
3. Add schema validation for POST/GET responses
4. Include docstrings explaining test purpose
5. Use fixtures for test data creation
6. Add assertions for both status code and response data

## License

This project is part of the python-sdet-foundation course.

## Additional Resources

- [GoRest API Documentation](https://gorest.co.in)
- [Pytest Documentation](https://docs.pytest.org)
- [Requests Library](https://requests.readthedocs.io)
- [JSON Schema Validation](https://python-jsonschema.readthedocs.io)

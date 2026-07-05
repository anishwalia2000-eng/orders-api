# Orders API

This is a sample backend service simulating discount qualifications. It serves as a test fixture codebase for pipeline validation.

## Business Rule

A customer qualifies for free shipping if:
- They are a **premium** member, **OR**
- They have placed **5 or more** orders.

## Tech Stack

- Python 3
- Flask (Minimal web API)
- Pytest (Unit testing)
- In-memory data store (no database setup required)

## Installation

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

Start the local Flask development server:
```bash
python app.py
```

### Endpoints

- `GET /customers`: Returns a list of all customers, their premium status, order count, and shipping discount qualification.
- `GET /customers/<id>`: Returns details for a single customer.
- `POST /customers/<id>/place-order`: Simulates placing a new order for a customer (increments their order count by 1) and returns their updated status.

## Running Tests

Run the test suite using pytest:
```bash
pytest
```
# orders-api

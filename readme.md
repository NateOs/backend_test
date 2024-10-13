# Fido Backend Engineer Home Assignment

## Objective
Develop a RESTful API using FastAPI, focusing on transactions and user interactions integral to Fido's services. This task will demonstrate your expertise in:
- Python
- Architectural decisions
- Asynchronous operations
- Testing

## Task Details

### API Development with FastAPI
- [x] Set up a FastAPI project.
- [x] Design endpoints to handle user financial records, specifically:
  - [x] Create a transaction record.
  - [x] Read a user's transaction history.
  - [x] Update a transaction record.
  - [x] Delete a transaction record.
- Each record should contain:
  - `user_id`
  - `full_name`
  - `transaction_date`
  - `transaction_amount`
  - `transaction_type` (credit/debit)
- [x] Gracefully handle errors and provide insightful feedback to the API user.

### Data Encryption
- [x] Ensure sensitive data like `full_name` is encrypted in the database.
- [x] Add a simple encryption mechanism using a Python library (e.g., Fernet or similar).

### Transaction Analytics Endpoint
- [x] Implement an endpoint where, given a `user_id`, the API returns:
  - [x] The user's average transaction value.
  - [x] The day they made the highest number of transactions.
  - (Optional) The total value of debit and credit transactions over a specific period.
- [x] Optimize this endpoint for performance.

### Asynchronous Processing
- [x] When a transaction is added, consider processing implications (e.g., updating user statistics, alerting relevant systems, or recalculating credit scores).
- [x] Strategize how to enhance system responsiveness and efficiency.

### Caching Mechanism
- [x] Implement caching (e.g., using Redis) for:
  - Frequent read operations like fetching transaction history.
  - Calculating transaction analytics.
- [x] Ensure that stale data is refreshed periodically.

### Testing with `pytest`
- [ ] Write unit tests for your endpoints using `pytest`.
- [ ] Ensure tests cover primary use cases and edge cases.

### Containerization
- [ ] Draft a `Dockerfile` to containerize your FastAPI application.
- [ ] Ensure the Docker container runs the application smoothly and integrates well with any database or external systems.

### Documentation
- [ ] Compile a `README` file detailing:
  - Setup and run instructions.
  - Your design and architectural decisions.
  - Potential strategies for scaling the solution for a large user base, and any trade-offs considered.

## Submission
- [ ] Initiate a new repository on GitHub.
- [ ] Commit your code, tests, and documentation.
import redis

# Create a Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
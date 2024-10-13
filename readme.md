Fido Backend Engineer Home Assignment
Objective
Develop a RESTful API using FastAPI, focusing on transactions and user interactions integral to Fido's services. This task will give us a glimpse into your expertise in Python, architectural decisions, asynchronous operations, and testing.
Task Details
API Development with FastAPI

Set up a FastAPI project.
Design endpoints that handle user financial records, specifically:

Creating a transaction record.
Reading a user's transaction history.
Updating a transaction record.
Deleting a transaction record.


Each record should contain: user_id, full_name, transaction_date, transaction_amount, and transaction_type (credit/debit).
Gracefully handle errors and provide insightful feedback to the API user.

Data Encryption

Ensure sensitive data like full_name is encrypted in the database.
Add a simple encryption mechanism using a Python library (e.g., Fernet or similar).

Transaction Analytics Endpoint

Implement an endpoint where, given a user_id, the API returns the user's average transaction value and the day they made the highest number of transactions.
The total value of debit and credit transactions over a specific period (optional).
Ensure that this endpoint is optimized for performance.

Asynchronous Processing

When a transaction is added, ponder over the processing implications (e.g., updating user statistics, alerting relevant systems, or recalculating credit scores).
Strategize about enhancing system responsiveness and efficiency.

Caching Mechanism

Implement caching (e.g., using Redis) for frequent read operations like fetching transaction history, or calculating transaction analytics.
Ensure that stale data is refreshed periodically.

Testing with pytest

Write unit tests for your endpoints using pytest.
Ensure tests cover primary use cases and edge cases.

Containerization

Draft a Dockerfile to containerize your FastAPI application.
Ensure the Docker container runs the application smoothly and integrates well with any database or external systems you opt for.

Documentation

Compile a README detailing:

Setup and run instructions.
Your design and architectural decisions.
Potential strategies for scaling this solution for a substantial user base, and any trade-offs that come to mind.



Submission

Initiate a new repository on GitHub.
Commit your code, tests, and documentation.
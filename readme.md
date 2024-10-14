# Fido Backend Engineer Home Assignment

## Objective
Develop a RESTful API using FastAPI, focusing on transactions and user interactions integral to Fido's services. This task will demonstrate your expertise in:
- Python
- Architectural decisions
- Asynchronous operations
- Testing

## Design and architectural decisions.
- The goal of the application was to build a basic transactions backend application that will accept, user with an id, and their login details, whilst anonymizing the user's name.
- I thought  perhaps creating a users table help with analytics, but realised that wouldn't be necessary.
- In terms, of folder structure, I considered what is common to me, but also referenced what FastAPI docs mentioned.Tends out its pretty neat.
- For the sake of scalability, docker is a good choice as it can be orchestrated with tooling like kubernetes to serve massive loads.

## Potential strategies for scaling the solution for a large user base, and any trade-offs considered.

## Setup and Run
## With docker

- Ensure Docker is Installed:
Make sure Docker is installed on your machine. You can download it from Docker's official website.

- Build the Docker Image:
Navigate to the project directory and build the Docker image using the Dockerfile.
docker build -t fido-backend .

- Run the Docker Container:
Use Docker Compose to run the application. This will start the FastAPI application along with any other services defined in the docker-compose.yml file, such as the database and Redis.
docker-compose up

- Access the API:
Once the container is running, open your web browser and navigate to http://localhost:8000 to access the API. You can also view the interactive API documentation at http://localhost:8000/docs.

- Run Tests (Optional):
If you want to run tests inside the Docker container, you can execute a command in the running container. First, find the container ID or name using docker ps, then run:
docker exec -it <container_id_or_name> pytest

## To run test:
`docker exec -it <containername or id> pytest`


## Without docker

- Clone the Repository:
First, clone the repository to your local machine using Git.
git clone <repository-url>
cd <repository-directory>

- Set Up a Virtual Environment:
Create and activate a virtual environment to manage your project's dependencies.
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

- Install Dependencies:
Install the required Python packages using pip.
pip install -r requirements.txt

- Configure Environment Variables:
Ensure you have a .env file in the project root directory with the necessary environment variables. For example:
DATABASE_URL=postgresql://user:password@localhost/dbname
REDIS_URL=redis://localhost:6379/0

- Run Database Migrations:
Use Alembic to apply database migrations.
alembic upgrade head

- Start the FastAPI Application:
Use Uvicorn to run the FastAPI application.
uvicorn app.main:app --reload

- Access the API:
Open your web browser and navigate to http://localhost:8000 to access the API. You can also view the interactive API documentation at http://localhost:8000/docs.

- Run Tests (Optional):
To ensure everything is working correctly, run the tests using pytest.
pytest


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
- [x] Write unit tests for your endpoints using `pytest`.
- [x] Ensure tests cover primary use cases and edge cases.

### Containerization
- [x] Draft a `Dockerfile` to containerize your FastAPI application.
- [ ] Ensure the Docker container runs the application smoothly and integrates well with any database or external systems.

### Documentation
- [x] Compile a `README` file detailing:
  - Setup and run instructions.
  - Your design and architectural decisions.
  - Potential strategies for scaling the solution for a large user base, and any trade-offs considered.

## Submission
- [x] Initiate a new repository on GitHub.
- [x] Commit your code, tests, and documentation.
import redis

# Create a Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
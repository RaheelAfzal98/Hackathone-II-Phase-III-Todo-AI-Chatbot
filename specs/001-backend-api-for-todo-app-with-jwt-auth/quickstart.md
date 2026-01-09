# Quickstart Guide: Backend API for Todo App with JWT Auth

## Prerequisites

- Python 3.11 or higher
- pip package manager
- Git version control
- Access to Neon Serverless PostgreSQL database
- Better Auth configured for frontend (to generate JWT tokens)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone [repository-url]
cd [repository-directory]
```

### 2. Navigate to Backend Directory
```bash
cd backend
```

### 3. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Environment Configuration
Create a `.env` file in the backend directory:
```env
BETTER_AUTH_SECRET=your_secret_key_here
BETTER_AUTH_URL=http://localhost:3000
DATABASE_URL=postgresql://neondb_owner:your_password@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require
SECRET_KEY=your_app_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6. Run Database Migrations
```bash
# If using Alembic for migrations
alembic upgrade head
```

### 7. Start Development Server
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Key Scripts

- `uvicorn src.main:app --reload` - Start development server with hot reloading
- `pytest` - Run all tests
- `pytest tests/test_api/` - Run API-specific tests
- `black .` - Format code with Black
- `flake8 .` - Check code style
- `mypy .` - Run type checks

## Project Structure Overview

```
backend/
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variable template
├── src/
│   ├── config/               # Configuration and settings
│   ├── models/               # SQLModel data models
│   ├── schemas/              # Pydantic schemas for API validation
│   ├── database/             # Database connection and session management
│   ├── auth/                 # Authentication and authorization utilities
│   ├── api/                  # API routes and endpoints
│   ├── services/             # Business logic services
│   └── utils/                # Utility functions
├── tests/                    # Test files
└── alembic/                  # Database migration scripts
```

## Development Workflow

### Creating a New Endpoint
1. Create the endpoint function in the appropriate file in `src/api/v1/endpoints/`
2. Add the route to the APIRouter in `src/api/v1/__init__.py`
3. Define request/response schemas in `src/schemas/`
4. Implement business logic in `src/services/`
5. Write tests in `tests/test_api/`

### Adding a New Model
1. Define the model in `src/models/` using SQLModel
2. Create Pydantic schemas for API validation in `src/schemas/`
3. Write model tests in `tests/test_models/`
4. Update database migrations if needed

### Authentication Flow
1. Frontend receives JWT token from Better Auth
2. Frontend includes token in Authorization header: `Authorization: Bearer <token>`
3. Backend verifies token signature using `BETTER_AUTH_SECRET`
4. Backend extracts user_id from token and compares with URL user_id
5. If match, grants access; if mismatch, returns 403 Forbidden

### Testing
To run the tests:
```bash
# Run all tests
pytest

# Run tests in watch mode
pytest --watch

# Run specific test file
pytest tests/test_api/test_tasks.py

# Run with coverage
pytest --cov=src
```

## API Usage Examples

### Get User Tasks
```bash
curl -X GET \
  http://localhost:8000/api/user123/tasks \
  -H "Authorization: Bearer your_jwt_token_here" \
  -H "Content-Type: application/json"
```

### Create a Task
```bash
curl -X POST \
  http://localhost:8000/api/user123/tasks \
  -H "Authorization: Bearer your_jwt_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Task",
    "description": "Task description",
    "completed": false
  }'
```

### Update a Task
```bash
curl -X PUT \
  http://localhost:8000/api/user123/tasks/task456 \
  -H "Authorization: Bearer your_jwt_token_here" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Task",
    "completed": true
  }'
```

## Environment Variables

- `BETTER_AUTH_SECRET`: Secret key for verifying JWT tokens from Better Auth
- `BETTER_AUTH_URL`: URL of the Better Auth service
- `DATABASE_URL`: Connection string for Neon PostgreSQL database
- `SECRET_KEY`: Secret key for JWT encoding (if needed additionally)
- `ALGORITHM`: Algorithm for JWT encoding (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes

## Common Tasks

### Running Tests
```bash
# Run all tests
pytest

# Run tests with specific marker
pytest -m "auth"  # Run only auth-related tests

# Run tests and see coverage
pytest --cov=src --cov-report=html
```

### Database Operations
```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Downgrade to previous version
alembic downgrade -1
```

### Code Quality
```bash
# Check code style
flake8 src/

# Format code
black src/

# Run type checks
mypy src/
```

## Troubleshooting

### Common Issues
- **JWT Error**: Verify `BETTER_AUTH_SECRET` matches the one used by Better Auth
- **Database Connection**: Check `DATABASE_URL` is properly formatted
- **403 Forbidden**: Ensure JWT user_id matches the user_id in the API route
- **401 Unauthorized**: Verify JWT token is valid and not expired

### Debugging Tips
- Enable debug logging by setting `DEBUG=True` in environment
- Check server logs for detailed error messages
- Use FastAPI's automatic docs at `/docs` to test endpoints
- Verify token contents using JWT debugging tools
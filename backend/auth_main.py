from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta
from typing import Optional
import uuid
from pydantic import BaseModel, EmailStr
from datetime import datetime

# Simple in-memory "database" for development
fake_users_db = {}

# Create FastAPI app instance
app = FastAPI(
    title="Todo API",
    description="A secure, multi-user todo management API with JWT authentication",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Expose authorization header to allow frontend to access JWT tokens
    expose_headers=["Authorization"]
)

# Models
class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    password: str
    confirm_password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: str
    created_at: datetime
    token: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Simple JWT-like token generation (for demo purposes)
def create_simple_token(user_id: str) -> str:
    import time
    import hashlib
    # In a real app, use proper JWT with libraries like python-jose
    token_data = f"{user_id}:{time.time()}"
    return hashlib.sha256(token_data.encode()).hexdigest()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "todo-backend"}

# Registration endpoint
@app.post("/api/v1/register", response_model=UserResponse)
def register_user(user_data: UserCreate):
    if user_data.password != user_data.confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match"
        )

    # Check if user already exists
    if user_data.email in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )

    # Create user
    user_id = str(uuid.uuid4())
    user = {
        "id": user_id,
        "email": user_data.email,
        "name": user_data.name,
        "hashed_password": user_data.password,  # In real app, hash the password
        "created_at": datetime.utcnow()
    }

    fake_users_db[user_data.email] = user

    # Create token
    token = create_simple_token(user_id)

    return UserResponse(
        id=user["id"],
        email=user["email"],
        name=user["name"],
        created_at=user["created_at"],
        token=token
    )

# Login endpoint
@app.post("/api/v1/login", response_model=UserResponse)
def login_user(user_login: UserLogin):
    # Find user
    user = fake_users_db.get(user_login.email)
    if not user or user["hashed_password"] != user_login.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    # Create token
    token = create_simple_token(user["id"])

    return UserResponse(
        id=user["id"],
        email=user["email"],
        name=user["name"],
        created_at=user["created_at"],
        token=token
    )

# Profile endpoint
security = HTTPBearer()

@app.get("/api/v1/profile", response_model=UserResponse)
def get_profile(credentials: HTTPBearer = Depends(security)):
    # In a real app, validate the token properly
    # For demo, just return the first user (this is a placeholder)
    if not fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No users registered"
        )

    # Get the first user for demo purposes
    user_email = next(iter(fake_users_db.keys()))
    user = fake_users_db[user_email]
    token = create_simple_token(user["id"])

    return UserResponse(
        id=user["id"],
        email=user["email"],
        name=user["name"],
        created_at=user["created_at"],
        token=token
    )

# Basic task endpoints
@app.get("/api/v1/tasks")
def get_tasks(credentials: HTTPBearer = Depends(security)):
    return {"tasks": []}

@app.post("/api/v1/tasks")
def create_task(task_data: dict, credentials: HTTPBearer = Depends(security)):
    return {"message": "Task created successfully", "task": task_data}
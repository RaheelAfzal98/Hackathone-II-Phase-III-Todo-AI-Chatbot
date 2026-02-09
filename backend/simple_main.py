from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import settings

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
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Expose authorization header to allow frontend to access JWT tokens
    expose_headers=["Authorization"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "todo-backend"}

# Basic task endpoints without complex models
@app.get("/api/v1/tasks")
def get_tasks():
    return {"tasks": []}

@app.post("/api/v1/tasks")
def create_task():
    return {"message": "Task created successfully"}
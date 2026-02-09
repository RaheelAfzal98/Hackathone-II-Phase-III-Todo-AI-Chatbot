# Quickstart Guide: AI Chatbot Integration

## Overview
This guide provides a quick overview of how to set up and run the AI-powered conversational interface for task management.

## Prerequisites
- Python 3.11+
- Node.js 18+ (for frontend)
- PostgreSQL-compatible database (Neon recommended)
- OpenAI API key
- Existing Phase II backend setup

## Setup Steps

### 1. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Update with your OpenAI API key and database connection
OPENAI_API_KEY=your_openai_key_here
DATABASE_URL=postgresql://username:password@host:port/database
BETTER_AUTH_SECRET=your_auth_secret
```

### 2. Backend Installation
```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run database migrations (includes both Phase II and new conversation models)
alembic upgrade head
```

### 3. MCP Server Setup
```bash
# Start the MCP server (separate process from main API)
python -m src.mcp_server.server
```

### 4. Main API Server
```bash
# In a new terminal, start the main API server
uvicorn src.main:app --reload
```

### 5. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## Usage

### Starting a Conversation
1. Authenticate with existing Phase II credentials
2. Navigate to the chat interface
3. Send a natural language message (e.g., "Add a task to buy groceries")

### Supported Commands
- "Add a task [description]" - Creates a new task
- "Show my tasks" - Lists all tasks
- "Complete task [ID]" - Marks a task as complete
- "Update task [ID] to [new description]" - Updates a task
- "Delete task [ID]" - Removes a task

## API Endpoints
- `POST /api/{user_id}/chat` - Main chat endpoint
- `GET /api/{user_id}/conversations` - List user conversations
- `GET /api/{user_id}/conversations/{id}` - Get specific conversation

## Testing
```bash
# Run backend tests
pytest tests/

# Run frontend tests
npm run test
```

## Troubleshooting
- If AI responses seem incorrect, check that MCP server is running
- If authentication fails, verify JWT configuration matches Phase II
- If conversations aren't persisting, check database connection and migration status
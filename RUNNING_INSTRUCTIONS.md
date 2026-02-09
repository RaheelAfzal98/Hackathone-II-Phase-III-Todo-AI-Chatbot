# Todo AI Chatbot - Running Instructions

## Prerequisites

- Python 3.8+
- Node.js 18+
- npm or yarn
- PostgreSQL (or use the provided Neon DB URL in the .env file)

## Setup Instructions

### 1. Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy the `.env` file in the backend directory (already configured)
   - Ensure all required environment variables are set

4. Create database tables:
```bash
python create_tables.py
```

### 2. Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install JavaScript dependencies:
```bash
npm install
```

## Running the Application

### Method 1: Using the Startup Script (Recommended)

1. Make sure you're in the project root directory:
```bash
cd "E:\Hackathon II Phase III Todo AI Chatbot"
```

2. Run the startup script:
   - On Windows: Double-click `start_servers.bat` or run in Command Prompt:
     ```cmd
     start_servers.bat
     ```
   - On Windows with PowerShell: Run in PowerShell:
     ```powershell
     .\start_servers.ps1
     ```

### Method 2: Manual Startup (Step-by-Step)

#### Step 1: Start the MCP Server
Open a new terminal/command prompt and run:
```bash
cd backend
python start_mcp_server.py
```
This will start the MCP server on `http://localhost:8001`.

#### Step 2: Start the Backend Server
Open another terminal/command prompt and run:
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```
This will start the backend API server on `http://localhost:8000`.

#### Step 3: Start the Frontend Server
Open another terminal/command prompt and run:
```bash
cd frontend
npm run dev
```
This will start the frontend development server on `http://localhost:3000`.

## Application Architecture

- **Frontend**: Next.js application running on port 3000
- **Backend API**: FastAPI application running on port 8000
- **MCP Server**: Model Context Protocol server running on port 8001
- **Database**: PostgreSQL (configured via the .env file)

## Services Overview

1. **Frontend (Next.js)**: User interface for interacting with the Todo AI Chatbot
2. **Backend API (FastAPI)**: Handles authentication, user data, and API endpoints
3. **MCP Server**: Provides tools for the AI agent to interact with the task management system
4. **AI Agent**: Processes natural language requests and calls appropriate tools

## API Endpoints

- `POST /api/{user_id}/chat`: Main chat endpoint for AI interactions
- `GET /api/{user_id}/conversations/{conversation_id}`: Retrieve conversation history
- Traditional task management endpoints from Phase II

## Troubleshooting

### Common Issues:

1. **Port Already in Use**: If you get "address already in use" errors, kill any existing processes using the ports 8000, 8001, or 3000.

2. **Dependency Conflicts**: If you encounter dependency issues, try creating a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Environment Variables**: Ensure the `.env` file contains all required environment variables.

4. **Database Connection**: Verify the PostgreSQL connection string in the `.env` file is correct.

### Verifying Services Are Running:

- Backend API: Visit `http://localhost:8000` - should show welcome message
- Backend API Docs: Visit `http://localhost:8000/api/docs` - should show Swagger UI
- MCP Server: Visit `http://localhost:8001` - should show MCP server message
- Frontend: Visit `http://localhost:3000` - should show the Todo AI Chatbot interface

## Stopping the Application

To stop any running server, press `Ctrl+C` in the respective terminal window.

## Development Notes

- The AI agent connects to the MCP server to perform task operations securely
- All user data is isolated by user ID for security
- The application follows a stateless architecture for scalability
- Conversation history is persisted to the database for continuity
@echo off
echo Starting Todo AI Chatbot Application...

echo Starting MCP Server on port 8001...
start cmd /k "cd /d "%~dp0\backend" && python start_mcp_server.py"

echo Waiting for MCP server to start...
timeout /t 3 /nobreak >nul

echo Starting Backend Server on port 8000...
start cmd /k "cd /d "%~dp0\backend" && uvicorn main:app --host 0.0.0.0 --port 8000"

echo Waiting for backend to start...
timeout /t 3 /nobreak >nul

echo Starting Frontend Server...
start cmd /k "cd /d "%~dp0\frontend" && npm run dev"

echo.
echo All servers started successfully!
echo Backend: http://localhost:8000
echo MCP Server: http://localhost:8001
echo Frontend: http://localhost:3000 (usually)
pause
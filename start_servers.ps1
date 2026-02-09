# PowerShell script to start both the main backend and MCP server

Write-Host "Starting Todo AI Chatbot Application..." -ForegroundColor Green

# Start the MCP server in the background
Write-Host "Starting MCP Server on port 8001..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-Command", "cd '$PSScriptRoot\backend'; python start_mcp_server.py"

# Give MCP server a moment to start
Start-Sleep -Seconds 3

# Start the main backend server in the background
Write-Host "Starting Backend Server on port 8000..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-Command", "cd '$PSScriptRoot\backend'; uvicorn main:app --host 0.0.0.0 --port 8000"

# Give backend a moment to start
Start-Sleep -Seconds 3

# Start the frontend server in the background
Write-Host "Starting Frontend Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-Command", "cd '$PSScriptRoot\frontend'; npm run dev"

Write-Host "All servers started successfully!" -ForegroundColor Green
Write-Host "Backend: http://localhost:8000" -ForegroundColor Cyan
Write-Host "MCP Server: http://localhost:8001" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:3000 (usually)" -ForegroundColor Cyan
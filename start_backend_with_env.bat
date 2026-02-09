@echo off
set DATABASE_URL=postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb
set NEON_DB_URL=postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb
set BETTER_AUTH_SECRET=pohwuyqoVn683bmFDoVzmtQq50Zn3bFV
set SECRET_KEY=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
set OPENAI_API_KEY=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
set OPEN_ROUTER_API_KEY=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

cd /d "E:\Hackathon II Phase III Todo AI Chatbot\backend"
echo Creating tables...
python -c "from src.database.connection import create_tables; create_tables(); print('Tables created successfully')"
echo Starting backend server...
uvicorn main:app --host 0.0.0.0 --port 8000
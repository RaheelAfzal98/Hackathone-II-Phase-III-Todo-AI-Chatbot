import os
import sys
from dotenv import load_dotenv
import tempfile

# Create a temporary .env file with the correct values
temp_env_content = """DATABASE_URL=postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require
NEON_DB_URL=postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require
BETTER_AUTH_SECRET=pohwuyqoVn683bmFDoVzmtQq50Zn3bFV
SECRET_KEY=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
BETTER_AUTH_URL=http://localhost:8000
OPENAI_API_KEY=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
OPEN_ROUTER_API_KEY=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
"""

# Write to a temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.env') as f:
    f.write(temp_env_content)
    temp_env_path = f.name

# Load the temporary .env file
load_dotenv(dotenv_path=temp_env_path)

print("Environment variables loaded from temporary .env file.")

# Print the values to verify
print(f"DATABASE_URL: {os.environ.get('DATABASE_URL', 'NOT SET')}")
print(f"NEON_DB_URL: {os.environ.get('NEON_DB_URL', 'NOT SET')}")

# Clean up the temporary file
import os
os.unlink(temp_env_path)

# Now try to create the tables
print("\nCreating database tables...")
try:
    # Clear any cached modules to ensure fresh import
    modules_to_clear = [key for key in sys.modules.keys() if 'src' in key or 'config' in key or 'database' in key]
    for module in modules_to_clear:
        del sys.modules[module]
    
    from src.database.connection import create_tables
    create_tables()
    print("Tables created successfully.")
except Exception as e:
    print(f"Error creating tables: {e}")
    import traceback
    traceback.print_exc()
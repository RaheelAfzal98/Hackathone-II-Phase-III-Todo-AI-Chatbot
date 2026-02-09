import os
import sys

# Set the correct environment variables before importing anything else
os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['NEON_DB_URL'] = 'postgresql://neondb_owner:npg_JDbCa6ELqGQ2@ep-withered-shape-a7bd9hif-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
os.environ['BETTER_AUTH_SECRET'] = 'pohwuyqoVn683bmFDoVzmtQq50Zn3bFV'
os.environ['SECRET_KEY'] = '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'
os.environ['OPENAI_API_KEY'] = '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'
os.environ['OPEN_ROUTER_API_KEY'] = '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'

print("Environment variables set.")

# Now import and check the settings
from src.config.settings import settings

print("=== Environment Variables Debug (after setting) ===")
print(f"Direct NEON_DB_URL: {os.environ.get('NEON_DB_URL', 'NOT SET')}")
print(f"Direct DATABASE_URL: {os.environ.get('DATABASE_URL', 'NOT SET')}")
print()
print(f"Settings NEON_DB_URL: {settings.NEON_DB_URL}")
print(f"Settings DATABASE_URL: {settings.DATABASE_URL}")

# Test database connection
print("\nTesting database connection...")
try:
    from src.database.connection import ping_database
    result = ping_database()
    print(f"Database ping result: {result}")
except Exception as e:
    print(f"Database ping failed: {e}")
    import traceback
    traceback.print_exc()
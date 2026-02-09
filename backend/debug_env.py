import os
from src.config.settings import settings

print("=== Environment Variables Debug ===")
print(f"Direct NEON_DB_URL: {os.environ.get('NEON_DB_URL', 'NOT SET')}")
print(f"Direct DATABASE_URL: {os.environ.get('DATABASE_URL', 'NOT SET')}")
print()
print(f"Settings NEON_DB_URL: {settings.NEON_DB_URL}")
print(f"Settings DATABASE_URL: {settings.DATABASE_URL}")
print()
print("All environment variables containing 'DB':")
for key, value in os.environ.items():
    if 'DB' in key.upper() or 'DATABASE' in key.upper() or 'NEON' in key.upper():
        print(f"  {key}: {value[:50]}...")
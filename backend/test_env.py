import os
from src.config.settings import settings

print('DATABASE_URL:', repr(settings.DATABASE_URL))
print('NEON_DB_URL:', repr(settings.NEON_DB_URL))
print('ENV FILE LOCATION:', os.path.exists('.env'))
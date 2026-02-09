import os
import sys

# Clear any previously loaded modules
modules_to_remove = [mod for mod in sys.modules.keys() if 'settings' in mod or 'config' in mod]
for mod in modules_to_remove:
    del sys.modules[mod]

# Now import the settings
from src.config.settings import settings

print('DATABASE_URL:', repr(settings.DATABASE_URL))
print('NEON_DB_URL:', repr(settings.NEON_DB_URL))
print('BETTER_AUTH_SECRET:', repr(settings.BETTER_AUTH_SECRET))
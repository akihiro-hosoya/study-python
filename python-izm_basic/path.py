import os

PROJECT_DIR = 'C:¥python-izm'
SETTING_FILE = 'settings.ini'

print(os.path.join(PROJECT_DIR, SETTING_FILE))
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTING_FILE))
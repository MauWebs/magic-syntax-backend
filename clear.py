import os
import glob
import shutil

for filepath in glob.glob('./apps/**/migrations/*.py', recursive=True):
    if not filepath.endswith('__init__.py'):
        os.remove(filepath)

for filepath in glob.glob('./apps/**/migrations/*.pyc', recursive=True):
    os.remove(filepath)

for dirpath in glob.glob('./project/**/__pycache__', recursive=True):
    shutil.rmtree(dirpath)

for dirpath in glob.glob('./apps/**/__pycache__', recursive=True):
    shutil.rmtree(dirpath)

db_path = './db.sqlite3'
if os.path.exists(db_path):
    os.remove(db_path)

print('Archivos y directorios eliminados.')

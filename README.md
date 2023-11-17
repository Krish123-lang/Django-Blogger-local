# DjBlogger
# Setup

* `pip3 install pytest-django`
* `pip3 install python-dotenv`
----
1. `django-admin startproject djblogger .`
2. Create `.env` and `pytest.ini` file in root folder.
3. Create `settings` and `test` folder in `djblogger(project) folder`

4. ## settings (Folder)
- Create `__init__.py`, `local.py` and `production.py`
- Rename `settings.py` to `base.py`
- Modify `base.py`
```
from dotenv import load_dotenv
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG') == "True"
ALLOWED_HOSTS = ["*"]
```

5. `.env`
```
SECRET_KEY=0p82!-2qz18no)&i5gbxbbuffugw5i9m)!1wkp^)re0zx-p@&-
DEBUG=False
```
- `djblogger/settings/local.py`
```
from .base import *
```
- `djblogger/settings/production.py`
```
from .base import *
```
6. ## To generate random_secret_key
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
7. `pytest.ini`
```
[pytest]
DJANGO_SETTINGS_MODULE = djblogger.settings.local
python_files = test_*.py
```
8. `manage.py`
```
import os
from djblogger.settings import base

def main():
    if base.DEBUG:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djblogger.settings.local")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djblogger.settings.production")
```
9. ## test(folder)
- create `test_example.py`
```
def test_example():
    assert 1 == 1
```
10. Run tests using `pytest` in terminal.
----

```markdown
# easytripAfricaTBMS

EasyTripAfrica is a tours booking and management API system built with Django Rest Framework.

Quick start (development)

1. Clone
   - git clone https://github.com/Peterpete671/easytripAfricaTBMS.git
   - cd easytripAfricaTBMS
2. Create virtualenv & install deps
   - python -m venv .venv
   - source .venv/bin/activate # Windows: .venv\Scripts\activate
   - pip install -U pip
   - pip install -r requirements.txt
3. Set env vars
   - export DJANGO_SECRET_KEY="change-me"
   - export DJANGO_DEBUG=True
4. Migrate & run
   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py createsuperuser
   - python manage.py runserver
5. API
   - Base path: http://127.0.0.1:8000/api/
   - Login: POST http://127.0.0.1:8000/api/auth/login/ (username/password)
   - Refresh: POST http://127.0.0.1:8000/api/auth/refresh/
   - Logout: POST http://127.0.0.1:8000/api/auth/logout/ (body: {"refresh": "<token>"})
```

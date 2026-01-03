# easytripAfricaTBMS

EasyTripAfrica is a tours booking and management API built with Django and Django REST Framework.
Quick start (development)

1. Clone
   - git clone https://github.com/Peterpete671/easytripAfricaTBMS.git
   - cd easytripAfricaTBMS
2. Create virtualenv & install deps
   - python -m venv .venv
   - Windows: .venv\Scripts\activate
   - pip install -U pip
   - pip install -r requirements.txt
3. Set env vars
   - set DJANGO_SECRET_KEY="change-me" (Windows PowerShell: $env:DJANGO_SECRET_KEY = 'change-me')
   - set DJANGO_DEBUG=True
4. Migrate & run
   - python manage.py migrate
   - python manage.py createsuperuser
   - python manage.py runserver

Testing the API
Base URL: http://127.0.0.1:8000/api/

Common headers

- `Content-Type: application/json`
- `Authorization: Bearer <access_token>` for protected endpoints

Endpoints and sample payloads

- Register user (public): POST `/api/users/`
  Body:
  {
- Login (get JWT): POST `/api/auth/login/`
  Body:
  {
  Response example:
  {
  "refresh": "<refresh_token>",
- Refresh access token: POST `/api/auth/refresh/`
  Body: { "refresh": "<refresh_token>" }

- Logout (blacklist refresh): POST `/api/auth/logout/`
- List tours (public): GET `/api/tours/`

- Create tour (admin only): POST `/api/tours/`
  Headers: `Authorization: Bearer <admin_access_token>`
  Body:
  {
  "tour_name": "Safari Adventure",
- Delete tour (admin only): DELETE `/api/tours/{tour_id}/`

- Book a tour (authenticated): POST `/api/bookings/`
  Headers: `Authorization: Bearer <access_token>`
  Body:
  {
  "tour_id": 1,
- List bookings: GET `/api/bookings/` (admin -> all, user -> own)

- Create payment: POST `/api/payments/` (authenticated)
  Body example:
  {
  "book_id": 10,
  "amount": "450.00",
  "method": "card",
  "pay_status": "Completed"
  }

Curl examples
Register user:

```
curl -X POST http://127.0.0.1:8000/api/users/ \
   -H "Content-Type: application/json" \
   -d '{"username":"john_doe","email":"john@example.com","password":"securepassword123"}'
```

Login to get tokens:

```
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
   -H "Content-Type: application/json" \
   -d '{"username":"john_doe","password":"securepassword123"}'
```

Create tour (admin):

```
curl -X POST http://127.0.0.1:8000/api/tours/ \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer <admin_access_token>" \
   -d '{"tour_name":"Safari Adventure","tour_description":"3-day safari","tour_days":3,"tour_price":"450.00","category":"safari"}'
Book a tour (user):
```

curl -X POST http://127.0.0.1:8000/api/bookings/ \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer <access_token>" \
 -d '{"tour_id":1,"travel_date":"2026-02-10"}'

````

Notes
- Public registration is enabled: new users can POST to `/api/users/`.
- Admin-only actions: creating/updating/deleting tours and listing all users/bookings require an admin account.
- The project uses JWT (djangorestframework-simplejwt). Use the returned `access` token in the `Authorization` header as `Bearer <access>`.

If you'd like, I can also add a Postman collection or a small test script that runs the full flow (register -> login -> create tour -> book -> list).
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
````

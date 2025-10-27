# myapi (Faker Users) — README



## REQUIMENT BREEE
- Python 3.8+ (Anda pakai 3.12)
- pip
- Windows command line / PowerShell

## Setup (lokal, Windows)
Buka terminal di folder proyek:
```powershell
cd /d e:\Python\myapi
```

Buat virtualenv dan aktifkan:
PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
CMD:
```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

Install dependensi:
```powershell
pip install -r requirements.txt
```
Jika file requirements.txt belum berisi paket yang diperlukan:
```powershell
pip install djangorestframework Faker django-cors-headers
pip freeze > requirements.txt
```

Jalankan migrasi (meskipun proyek ini tidak memakai model custom):
```powershell
python manage.py migrate
```

Jalankan server:
```powershell
python manage.py runserver 0.0.0.0:8800
```
Akses API di http://localhost:8800/api/faker-users/

## Jalankan lewat Docker
Build image:
```powershell
docker build -t myapi:latest .
```
Run container:
```powershell
docker run --rm -p 8800:8800 myapi:latest
```

## Endpoints
Base path: /api/faker-users/

1. GET list (pagination)
- URL: GET /api/faker-users/?page=1&limit=10
- Query params:
  - page (default 1)
  - limit (default 10, max 100)
- Response: JSON { data: [...], pagination: {...} }

Contoh curl:
```bash
curl "http://localhost:8800/api/faker-users/?page=1&limit=5"
```

2. POST create
- URL: POST /api/faker-users/
- Body (JSON). Required: `firstName`, `lastName`, `email`
- Optional: `phone`, `password`, `status`, `role`
- Response: created object (201)

Contoh body:
```json
{
  "firstName": "Budi",
  "lastName": "Santoso",
  "email": "budi@example.com",
  "phone": "+628123456789",
  "password": "secret123",
  "status": "active",
  "role": "admin"
}
```

curl contoh:
```bash
curl -X POST "http://localhost:8800/api/faker-users/" -H "Content-Type: application/json" -d "{\"firstName\":\"Budi\",\"lastName\":\"Santoso\",\"email\":\"budi@example.com\"}"
```

3. GET detail
- URL: GET /api/faker-users/{id}/
- Response: single user object or 404

4. PUT (replace)
- URL: PUT /api/faker-users/{id}/
- Body: full required fields (`firstName`,`lastName`,`email`) plus optional fields
- Replaces target fields, responds updated object

5. PATCH (partial update)
- URL: PATCH /api/faker-users/{id}/
- Body: any subset of allowed fields (`firstName`,`lastName`,`email`,`phone`,`password`,`status`,`role`)
- Responds updated object

6. DELETE
- URL: DELETE /api/faker-users/{id}/
- Response: 204 No Content

Contoh curl untuk PATCH:
```bash
curl -X PATCH "http://localhost:8800/api/faker-users/1001/" -H "Content-Type: application/json" -d "{\"phone\":\"+628000000000\"}"
```

Contoh curl untuk DELETE:
```bash
curl -X DELETE "http://localhost:8800/api/faker-users/1001/"
```

## Catatan penting
- Data hanya disimpan di memori proses (ALL_USERS). Restart server menghapus semua perubahan.
- Password disimpan plain-text di dataset untuk testing saja — jangan gunakan di produksi.
- Jika mengalami error CORS, periksa `CORS_ALLOWED_ORIGINS` di `myapi/settings.py`. Untuk development cepat, Anda bisa sementara aktifkan:
```python
CORS_ALLOW_ALL_ORIGINS = True
```
- Pastikan `rest_framework` dan `corsheaders` ada di `INSTALLED_APPS`.

## Troubleshooting singkat
- ModuleNotFoundError: No module named 'rest_framework' → jalankan `pip install djangorestframework`
- CORS errors → perbaiki `CORS_ALLOWED_ORIGINS` (pastikan setiap origin punya scheme dan host, misal `http://localhost:3000`)

-- End of README
```// filepath: e:\Python\myapi\README.md
# myapi (Faker Users) — README

Singkat: API sederhana yang menghasilkan data user palsu di-memory (Faker). Perubahan data disimpan hanya di proses (ALL_USERS) — restart server menghapus perubahan.

## Prasyarat
- Python 3.8+ (Anda pakai 3.12)
- pip
- (Opsional) Docker
- Windows command line / PowerShell

## Setup (lokal, Windows)
Buka terminal di folder proyek:
```powershell
cd /d e:\Python\myapi
```

Buat virtualenv dan aktifkan:
PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
CMD:
```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

Install dependensi:
```powershell
pip install -r requirements.txt
```
Jika file requirements.txt belum berisi paket yang diperlukan:
```powershell
pip install djangorestframework Faker django-cors-headers
pip freeze > requirements.txt
```

Jalankan migrasi (meskipun proyek ini tidak memakai model custom):
```powershell
python manage.py migrate
```

Jalankan server:
```powershell
python manage.py runserver 0.0.0.0:8800
```
Akses API di http://localhost:8800/api/faker-users/

## Jalankan lewat Docker
Build image:
```powershell
docker build -t myapi:latest .
```
Run container:
```powershell
docker run --rm -p 8800:8800 myapi:latest
```

## Endpoints
Base path: /api/faker-users/

1. GET list (pagination)
- URL: GET /api/faker-users/?page=1&limit=10
- Query params:
  - page (default 1)
  - limit (default 10, max 100)
- Response: JSON { data: [...], pagination: {...} }

Contoh curl:
```bash
curl "http://localhost:8800/api/faker-users/?page=1&limit=5"
```

2. POST create
- URL: POST /api/faker-users/
- Body (JSON). Required: `firstName`, `lastName`, `email`
- Optional: `phone`, `password`, `status`, `role`
- Response: created object (201)

Contoh body:
```json
{
  "firstName": "Budi",
  "lastName": "Santoso",
  "email": "budi@example.com",
  "phone": "+628123456789",
  "password": "secret123",
  "status": "active",
  "role": "admin"
}
```

curl contoh:
```bash
curl -X POST "http://localhost:8800/api/faker-users/" -H "Content-Type: application/json" -d "{\"firstName\":\"Budi\",\"lastName\":\"Santoso\",\"email\":\"budi@example.com\"}"
```

3. GET detail
- URL: GET /api/faker-users/{id}/
- Response: single user object or 404

4. PUT (replace)
- URL: PUT /api/faker-users/{id}/
- Body: full required fields (`firstName`,`lastName`,`email`) plus optional fields
- Replaces target fields, responds updated object

5. PATCH (partial update)
- URL: PATCH /api/faker-users/{id}/
- Body: any subset of allowed fields (`firstName`,`lastName`,`email`,`phone`,`password`,`status`,`role`)
- Responds updated object

6. DELETE
- URL: DELETE /api/faker-users/{id}/
- Response: 204 No Content

Contoh curl untuk PATCH:
```bash
curl -X PATCH "http://localhost:8800/api/faker-users/1001/" -H "Content-Type: application/json" -d "{\"phone\":\"+628000000000\"}"
```

Contoh curl untuk DELETE:
```bash
curl -X DELETE "http://localhost:8800/api/faker-users/1001/"
```

## Catatan penting
- Data hanya disimpan di memori proses (ALL_USERS). Restart server menghapus semua perubahan.
- Password disimpan plain-text di dataset untuk testing saja — jangan gunakan di produksi.
- Jika mengalami error CORS, periksa `CORS_ALLOWED_ORIGINS` di `myapi/settings.py`. Untuk development cepat, Anda bisa sementara aktifkan:
```python
CORS_ALLOW_ALL_ORIGINS = True
```
- Pastikan `rest_framework` dan `corsheaders` ada di `INSTALLED_APPS`.

## Troubleshooting singkat
- ModuleNotFoundError: No module named 'rest_framework' → jalankan `pip install djangorestframework`
- CORS errors → perbaiki `CORS_ALLOWED_ORIGINS` (pastikan setiap origin punya scheme dan host, misal `http://localhost:3000`)

-- End of README
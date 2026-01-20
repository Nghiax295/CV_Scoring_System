# CVScoringSystem

Django project sạch, chuẩn, sẵn sàng phát triển.

## Công nghệ

- Python
- Django 6.0.1
- SQLite (mặc định)

## Yêu cầu

- Python 3.x
- pip

## Cài đặt

### 1. Clone repository

```bash
git clone <repository-url>
cd Python
```

### 2. Tạo và kích hoạt virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Cài đặt dependencies

```bash
pip install django
```

### 4. Chạy migrations

```bash
python manage.py migrate
```

## Chạy server

```bash
python manage.py runserver
```

Truy cập: http://127.0.0.1:8000/

## Cấu trúc dự án

```
Python/
├── venv/                      # Virtual environment
├── CVScoringSystem/           # Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Cấu hình project
│   ├── urls.py               # URL routing
│   └── wsgi.py
├── manage.py                  # Django management
├── .gitignore                # Git ignore rules
└── README.md                 # Documentation
```

## Git

### Trạng thái hiện tại

- ✓ Git repository đã khởi tạo
- ✓ Commit đầu tiên đã hoàn thành

### Push lên GitHub

```bash
git remote add origin <github-repo-url>
git branch -M main
git push -u origin main
```

## Lưu ý

- Database mặc định: SQLite (db.sqlite3)
- Secret key: Nên thay đổi trong production
- DEBUG mode: Tắt trong production

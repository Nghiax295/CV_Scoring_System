# CVScoringSystem

Hệ thống chấm điểm CV sử dụng AI để đánh giá và xếp hạng ứng viên tự động.

## Giới thiệu

CVScoringSystem là một ứng dụng Django được xây dựng để:
- Tự động phân tích và chấm điểm CV của ứng viên
- Hỗ trợ nhà tuyển dụng (recruiter) quản lý và đánh giá ứng viên
- Tích hợp AI để phân tích kỹ năng và kinh nghiệm (sẽ tích hợp sau)

## Công nghệ sử dụng

- **Python** 3.x
- **Django** 6.0.1
- **SQLite** (database tạm thời, sẽ chuyển sang PostgreSQL sau)
- **AI/ML** (sẽ tích hợp sau)

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
pip install -r requirements.txt
```

### 4. Chạy migrations

```bash
python manage.py migrate
```

### 5. Tạo superuser

```bash
python manage.py createsuperuser
```

### 6. Chạy development server

```bash
python manage.py runserver
```

Truy cập:
- Trang chủ: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Cấu trúc project

```
Python/
├── venv/                      # Virtual environment
├── CVScoringSystem/           # Django core settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Cấu hình project
│   ├── urls.py               # URL routing
│   └── wsgi.py
├── accounts/                  # App quản lý user
│   ├── migrations/           # Database migrations
│   ├── admin.py              # Admin configuration
│   ├── apps.py
│   ├── models.py             # Custom User model
│   ├── tests.py
│   └── views.py
├── manage.py                  # Django CLI
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # Documentation
```

## Trạng thái hiện tại

### ✅ Đã hoàn thành

- **Custom User Model**: Kế thừa `AbstractUser` với field `role`
- **Phân quyền người dùng**:
  - `recruiter`: Nhà tuyển dụng
  - `candidate`: Ứng viên (default)
- **Admin Interface**: Quản lý user với role selector
- **Authentication**: Django auth system đã cấu hình

### 🚧 Đang phát triển

- CV upload và parsing
- AI scoring engine
- Dashboard cho recruiter
- Profile cho candidate

## Git workflow

### Push lên GitHub

```bash
git remote add origin <github-repo-url>
git branch -M main
git push -u origin main
```

### Commit convention

```bash
git add .
git commit -m "Mô tả ngắn gọn thay đổi"
git push
```

## Lưu ý

- **Database**: SQLite (chỉ dùng cho development)
- **SECRET_KEY**: Đổi trong production
- **DEBUG**: Tắt trong production
- **ALLOWED_HOSTS**: Cấu hình cho production

## Roadmap

1. ✅ Setup Django project
2. ✅ Custom User model với role
3. ✅ Admin interface
4. 🔲 CV upload functionality
5. 🔲 AI scoring engine
6. 🔲 Recruiter dashboard
7. 🔲 Candidate profile
8. 🔲 API endpoints
9. 🔲 Frontend UI

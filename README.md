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
├── media/                     # Uploaded files (CVs)
├── CVScoringSystem/           # Django core settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Cấu hình project
│   ├── urls.py               # URL routing
│   └── wsgi.py
├── accounts/                  # App quản lý user
│   ├── migrations/           # Database migrations
│   ├── templates/            # Login & dashboard templates
│   ├── admin.py              # Admin configuration
│   ├── decorators.py         # role_required decorator
│   ├── models.py             # Custom User model
│   ├── views.py              # Authentication views
│   └── urls.py               # Account URLs
├── cv/                        # App quản lý CV
│   ├── migrations/           # Database migrations
│   ├── templates/            # CV templates
│   ├── admin.py              # CV admin
│   ├── forms.py              # CV upload form
│   ├── models.py             # CV model
│   ├── views.py              # CV views
│   └── urls.py               # CV URLs
├── manage.py                  # Django CLI
├── requirements.txt           # Python dependencies
├── UPDATE_LOG.md             # Update history
├── .gitignore                # Git ignore rules
└── README.md                 # Documentation
```

## Chức năng hiện tại

### 🔐 Authentication & Authorization

- Login/Logout system
- Role-based access control (recruiter/candidate)
- Custom decorator `@role_required`
- 403 Forbidden cho truy cập không hợp lệ

### 👤 User Management

- Custom User model với field `role`
- Django admin interface để quản lý users
- Phân quyền: recruiter / candidate

### 📄 CV Management

**Candidate:**

- Upload CV (chỉ file PDF) tại `/cv/upload/`
- Xem danh sách CV của mình tại `/cv/my/`
- Download CV đã upload

**Recruiter:**

- Xem tất cả CV của candidates tại `/cv/recruiter/`
- Download bất kỳ CV nào
- Read-only access (không upload/xóa)

### 🎯 Dashboard

- Candidate dashboard: `/candidate/dashboard/`
- Recruiter dashboard: `/recruiter/dashboard/`
- Redirect tự động theo role sau login

## URLs chính

| URL                     | Role      | Mô tả                    |
| ----------------------- | --------- | ------------------------ |
| `/login/`               | All       | Đăng nhập                |
| `/logout/`              | All       | Đăng xuất                |
| `/admin/`               | Admin     | Django admin             |
| `/candidate/dashboard/` | Candidate | Dashboard ứng viên       |
| `/recruiter/dashboard/` | Recruiter | Dashboard nhà tuyển dụng |
| `/cv/upload/`           | Candidate | Upload CV                |
| `/cv/my/`               | Candidate | Danh sách CV của mình    |
| `/cv/recruiter/`        | Recruiter | Xem tất cả CV            |

## Test Accounts

Sau khi chạy migrations, tạo test users:

```bash
# Candidate
python manage.py shell -c "from accounts.models import User; User.objects.create_user(username='candidate', password='candidate123', role='candidate')"

# Recruiter
python manage.py shell -c "from accounts.models import User; User.objects.create_user(username='recruiter', password='recruiter123', role='recruiter')"
```

## Trạng thái hiện tại

### ✅ Đã hoàn thành

- **Custom User Model**: Kế thừa `AbstractUser` với field `role`
- **Phân quyền người dùng**:
  - `recruiter`: Nhà tuyển dụng
  - `candidate`: Ứng viên (default)
- **Admin Interface**: Quản lý user với role selector
- **Authentication**: Login/Logout với role-based redirect
- **CV Upload**: Candidate upload PDF files
- **CV Management**: View, list, download CVs
- **Access Control**: Role-based với decorator
- **Media Files**: Cấu hình upload và serve files

### 🚧 Đang phát triển

- AI scoring engine
- CV parsing tự động
- Filter và search CVs
- Candidate profile detail
- Recruiter analytics dashboard

## Roadmap

1. ✅ Setup Django project
2. ✅ Custom User model với role
3. ✅ Admin interface
4. ✅ CV upload functionality
5. ✅ CV list cho candidate
6. ✅ CV list cho recruiter
7. 🔲 AI scoring engine
8. 🔲 CV parsing và extract thông tin
9. 🔲 Search và filter CVs
10. 🔲 API endpoints
11. 🔲 Frontend UI nâng cao

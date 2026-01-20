# Update Log - CVScoringSystem

## Update lần 1 - 9:37 PM 20/01/2026
**Đã thêm:**
- Custom User model với field role (recruiter/candidate)
- Django admin cho quản lý User
- Login/Logout system với role-based redirect
- Dashboard riêng cho recruiter và candidate
- Decorator `role_required` để kiểm tra quyền truy cập
- Protection 403 Forbidden khi truy cập sai role
- Templates cơ bản cho login và dashboards

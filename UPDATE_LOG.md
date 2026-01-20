# Update Log - CVScoringSystem

## Update lần 2 - 9:45 PM 20/01/2026
**Đã thêm:**
- App `cv` để quản lý CV
- Model CV với owner (ForeignKey → User), file, uploaded_at
- Media configuration (MEDIA_URL, MEDIA_ROOT)
- Admin interface cho CV model
- Serve media files trong development

## Update lần 1 - 9:37 PM 20/01/2026

**Đã thêm:**

- Custom User model với field role (recruiter/candidate)
- Django admin cho quản lý User
- Login/Logout system với role-based redirect
- Dashboard riêng cho recruiter và candidate
- Decorator `role_required` để kiểm tra quyền truy cập
- Protection 403 Forbidden khi truy cập sai role
- Templates cơ bản cho login và dashboards

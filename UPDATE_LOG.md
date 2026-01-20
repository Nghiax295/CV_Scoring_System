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

## Update lần 2 - 9:45 PM 20/01/2026

**Đã thêm:**

- App `cv` để quản lý CV
- Model CV với owner (ForeignKey → User), file, uploaded_at
- Media configuration (MEDIA_URL, MEDIA_ROOT)
- Admin interface cho CV model
- Serve media files trong development

## Update lần 3 - 9:52 PM 20/01/2026

**Đã thêm:**

- CVUploadForm chỉ cho phép upload file PDF
- View upload_cv với @role_required('candidate')
- URL /cv/upload/ cho upload CV
- Template upload_cv.html với form multipart
- Chặn recruiter upload CV (403 Forbidden)
- CV tự động gắn với user đang login

## Update lần 4 - 10:00 PM 20/01/2026

**Đã thêm:**

- View my_cv_list để candidate xem danh sách CV của mình
- URL /cv/my/ với @role_required('candidate')
- Template my_cv_list.html hiển thị tên file, thời gian, link download
- Query CV theo owner và order by uploaded_at giảm dần
- Chặn recruiter xem CV của candidate (403 Forbidden)
- Redirect về my_cv_list sau khi upload thành công

## Update lần 5 - 10:07 PM 20/01/2026

**Đã thêm:**

- View recruiter_cv_list để recruiter xem tất cả CV
- URL /cv/recruiter/ với @role_required('recruiter')
- Template recruiter_cv_list.html hiển thị candidate, email, file, thời gian, download
- Query với select_related('owner') để optimize database
- Read-only cho recruiter, không có chức năng upload/xóa
- Chặn candidate truy cập danh sách CV của recruiter (403 Forbidden)

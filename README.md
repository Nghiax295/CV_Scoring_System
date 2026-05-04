# CV AI Project

Django web app for job postings and CV-based applications with role-based access.

## Features

- Role-based accounts: recruiters and applicants.
- Job listing with search, tags, and pagination.
- Recruiter dashboard to create and edit jobs, plus review applicants.
- Applicant flow to apply with PDF CVs, view applications, and withdraw.
- Seed command to generate sample users, jobs, applications, and CV files.
- Admin site for system management (admins log in via /admin only).

## Apps

- accounts: custom user model and auth views.
- jobs: job posts, applications, dashboards, and CV uploads.
- applications: placeholder app (no models yet).
- ai_services: placeholder app (no models yet).

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies:
   - pip install -r requirements.txt
3. Create a local env file:
   - copy .env.example to .env and update values
4. Run migrations:
   - python manage.py migrate
5. (Optional) Seed sample data:
   - python manage.py seed_data
6. Start the dev server:
   - python manage.py runserver

## Environment Variables

- DJANGO_SECRET_KEY
- DJANGO_DEBUG
- DJANGO_ALLOWED_HOSTS (comma-separated)

## Sample Data

After running seed_data:

- recruiter1..recruiter3 (password: 123456)
- applicant1..applicantN (password: 123456)
  A sample CV is created at media/sample_cv.pdf.

## Useful Routes

- / home
- /accounts/register/ register
- /accounts/login/ login
- /jobs/ job list
- /jobs/myjobs/ recruiter dashboard
- /jobs/applications/ applicant dashboard
- /admin/ admin site

## Notes

- SQLite database is stored locally (db.sqlite3).
- Uploaded CVs are stored under media/.

import random
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from faker import Faker

from jobs.models import Application, JobPost

User = get_user_model()
fake = Faker()

JOB_TITLES = [
    "Python Backend Developer",
    "AI / Machine Learning Engineer",
    "Data Analyst",
    "Frontend Developer (React)",
    "Full Stack Engineer",
    "DevOps / Cloud Engineer",
    "Mobile Developer (Flutter)",
    "NLP / LLM Researcher",
    "QA Automation Engineer",
    "Cybersecurity Analyst",
    "Embedded Systems Engineer",
    "Product Manager (Technical)",
]

TAG_POOL = [
    "Python", "Django", "FastAPI", "React", "Vue", "TypeScript",
    "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
    "Docker", "Kubernetes", "AWS", "GCP", "PostgreSQL",
    "REST API", "GraphQL", "CI/CD", "Linux", "Git",
]


class Command(BaseCommand):
    help = "Seed the database with sample recruiters, applicants, jobs, and applications."

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("=== Seeding database ==="))

        cv_path = self._ensure_sample_cv()

        recruiters = self._create_recruiters()
        applicants = self._create_applicants()
        jobs = self._create_jobs(recruiters)
        self._create_applications(applicants, jobs, cv_path)

        self.stdout.write(self.style.SUCCESS("\nDone! Database seeded successfully."))

    # ------------------------------------------------------------------
    # PDF helper
    # ------------------------------------------------------------------

    def _ensure_sample_cv(self):
        """Return path to media/sample_cv.pdf, creating it if absent."""
        pdf_path = Path(settings.MEDIA_ROOT) / "sample_cv.pdf"
        if not pdf_path.exists():
            self._write_minimal_pdf(pdf_path)
            self.stdout.write(f"  Created {pdf_path}")
        else:
            self.stdout.write(f"  PDF already exists: {pdf_path}")
        return pdf_path

    @staticmethod
    def _write_minimal_pdf(dest: Path):
        """Write a valid minimal PDF (no external libraries required)."""
        stream_data = (
            b"BT /F1 14 Tf 72 740 Td (Sample CV - Placeholder) Tj ET"
        )
        objs = [
            b"1 0 obj\n<</Type /Catalog /Pages 2 0 R>>\nendobj\n",
            b"2 0 obj\n<</Type /Pages /Kids [3 0 R] /Count 1>>\nendobj\n",
            (
                b"3 0 obj\n<</Type /Page /Parent 2 0 R "
                b"/MediaBox [0 0 612 792] /Contents 4 0 R "
                b"/Resources <</Font <</F1 5 0 R>>>>>>\nendobj\n"
            ),
            (
                b"4 0 obj\n<</Length "
                + str(len(stream_data)).encode()
                + b">>\nstream\n"
                + stream_data
                + b"\nendstream\nendobj\n"
            ),
            b"5 0 obj\n<</Type /Font /Subtype /Type1 /BaseFont /Helvetica>>\nendobj\n",
        ]
        header = b"%PDF-1.4\n"
        body = b"".join(objs)

        # Compute xref offsets
        offsets, pos = [], len(header)
        for obj in objs:
            offsets.append(pos)
            pos += len(obj)

        xref = b"xref\n0 6\n0000000000 65535 f \n"
        for off in offsets:
            xref += f"{off:010d} 00000 n \n".encode()

        trailer = (
            b"trailer\n<</Size 6 /Root 1 0 R>>\nstartxref\n"
            + str(len(header) + len(body)).encode()
            + b"\n%%EOF"
        )
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(header + body + xref + trailer)

    # ------------------------------------------------------------------
    # User creation
    # ------------------------------------------------------------------

    def _create_recruiters(self):
        self.stdout.write("\n[Recruiters]")
        recruiters = []
        for i in range(1, 4):
            username = f"recruiter{i}"
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                self.stdout.write(f"  skip  {username} (already exists)")
            else:
                user = User.objects.create_user(
                    username=username,
                    password="123456",
                    role="recruiter",
                )
                self.stdout.write(self.style.SUCCESS(f"  created {username}"))
            recruiters.append(user)
        return recruiters

    def _create_applicants(self):
        self.stdout.write("\n[Applicants]")
        count = random.randint(15, 20)
        applicants = []
        for i in range(1, count + 1):
            username = f"applicant{i}"
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                self.stdout.write(f"  skip  {username} (already exists)")
            else:
                user = User.objects.create_user(
                    username=username,
                    password="123456",
                    role="applicant",
                )
                self.stdout.write(self.style.SUCCESS(f"  created {username}"))
            applicants.append(user)
        return applicants

    # ------------------------------------------------------------------
    # Job creation
    # ------------------------------------------------------------------

    def _create_jobs(self, recruiters):
        self.stdout.write("\n[Jobs]")
        jobs = []
        titles = JOB_TITLES.copy()
        random.shuffle(titles)
        title_iter = iter(titles)

        for recruiter in recruiters:
            existing = list(JobPost.objects.filter(recruiter=recruiter))
            if existing:
                self.stdout.write(f"  skip  [{recruiter.username}] already has {len(existing)} job(s)")
                jobs.extend(existing)
                continue

            num_jobs = random.randint(3, 5)
            for _ in range(num_jobs):
                try:
                    title = next(title_iter)
                except StopIteration:
                    # If we exhaust the list, restart
                    titles = JOB_TITLES.copy()
                    random.shuffle(titles)
                    title_iter = iter(titles)
                    title = next(title_iter)

                tags = ", ".join(random.sample(TAG_POOL, k=random.randint(3, 6)))
                job = JobPost.objects.create(
                    title=title,
                    description=fake.paragraph(nb_sentences=5),
                    requirement=fake.paragraph(nb_sentences=4),
                    tags=tags,
                    recruiter=recruiter,
                )
                self.stdout.write(
                    self.style.SUCCESS(f"  created [{recruiter.username}] '{job.title}'")
                )
                jobs.append(job)

        return jobs

    # ------------------------------------------------------------------
    # Application creation
    # ------------------------------------------------------------------

    def _create_applications(self, applicants, jobs, cv_path: Path):
        self.stdout.write("\n[Applications]")
        cv_bytes = cv_path.read_bytes()

        for applicant in applicants:
            num_apps = random.randint(1, 3)
            chosen_jobs = random.sample(jobs, k=min(num_apps, len(jobs)))

            for job in chosen_jobs:
                # Respect unique_together: skip if already applied
                if Application.objects.filter(job=job, applicant=applicant).exists():
                    self.stdout.write(
                        f"  skip  {applicant.username} -> '{job.title}' (already applied)"
                    )
                    continue

                app = Application(job=job, applicant=applicant)
                file_name = f"{applicant.username}_cv.pdf"
                app.cv_file.save(file_name, ContentFile(cv_bytes), save=False)
                app.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"  applied {applicant.username} -> '{job.title}'"
                    )
                )

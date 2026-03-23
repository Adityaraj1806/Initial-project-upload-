from django.db import models
from django.contrib.auth.models import User

# -------------------------
# Faculty Model
# -------------------------
class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

# -------------------------
# Publication Model
# -------------------------
class Publication(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=255)
    journal = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

# -------------------------
# Research Project Model
# -------------------------
class ResearchProject(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    funding_agency = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

# -------------------------
# Teaching Assignment Model
# -------------------------
class TeachingAssignment(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='courses')
    course_name = models.CharField(max_length=255)
    semester = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course_name} ({self.semester}-{self.year})"

# -------------------------
# Awards / Recognition Model
# -------------------------
class Award(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='awards')
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.year})"

# -------------------------
# Appraisal Model
# -------------------------
class Appraisal(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='appraisals')
    year = models.PositiveIntegerField()
    performance_score = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.faculty.user.get_full_name() or self.faculty.user.username} - {self.year}"
from django.contrib import admin
from .models import Faculty, Publication, ResearchProject, TeachingAssignment, Award

admin.site.register(Faculty)
admin.site.register(Publication)
admin.site.register(ResearchProject)
admin.site.register(TeachingAssignment)
admin.site.register(Award)
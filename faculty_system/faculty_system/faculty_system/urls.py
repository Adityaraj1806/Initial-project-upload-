from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),      # Admin panel
    path('', include('appraisal.urls')),  # Include appraisal app URLs
]
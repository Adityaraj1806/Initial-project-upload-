from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # Home page
    path('register/', views.register, name='register'),   # Register page
    path('login/', views.user_login, name='login'),       # Login page
    path('logout/', views.user_logout, name='logout'),    # Logout
    path('dashboard/', views.dashboard, name='dashboard'),# Dashboard
    path('add/', views.add_appraisal, name='add_appraisal'), # Add Appraisal
]
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Faculty, Appraisal

# -------------------------
# Home Page
# -------------------------
def home(request):
    faculties = Faculty.objects.all()  # Get all faculties
    return render(request, 'appraisal/home.html', {'faculties': faculties})

# -------------------------
# Register Page
# -------------------------
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'appraisal/register.html', {'error': 'User already exists'})

        # Create user and linked Faculty
        user = User.objects.create_user(username=username, password=password)
        Faculty.objects.create(user=user, department='', designation='')

        return redirect('login')

    return render(request, 'appraisal/register.html')

# -------------------------
# Login Page
# -------------------------
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'appraisal/login.html', {'error': 'Invalid Credentials'})

    return render(request, 'appraisal/login.html')

# -------------------------
# Logout
# -------------------------
def user_logout(request):
    logout(request)
    return redirect('login')

# -------------------------
# Dashboard
# -------------------------
@login_required
def dashboard(request):
    faculty = get_object_or_404(Faculty, user=request.user)
    data = Appraisal.objects.filter(faculty=faculty)
    return render(request, 'appraisal/dashboard.html', {'data': data})

# -------------------------
# Add Appraisal
# -------------------------
@login_required
def add_appraisal(request):
    faculty = get_object_or_404(Faculty, user=request.user)

    if request.method == "POST":
        year = request.POST.get('year')
        performance_score = request.POST.get('performance_score')
        remarks = request.POST.get('remarks')

        Appraisal.objects.create(
            faculty=faculty,
            year=year,
            performance_score=performance_score,
            remarks=remarks
        )
        return redirect('dashboard')

    return render(request, 'appraisal/add_appraisal.html')
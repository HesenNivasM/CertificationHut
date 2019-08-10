from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from courses.models import Course

import json


def account_dashboard(request):
    all_courses = Course.objects.all()
    enrolled_courses = []
    for course in all_courses:
        if str(request.user.username) in json.decoder.JSONDecoder().decode(course.students_enrolled):
            enrolled_courses.append(course)
    return render(request, "account/dashboard.html", {
        "enrolled_courses": enrolled_courses
    })


def account_signup(request):
    if request.method == "POST" and request.POST.get("signup_submit"):
        username = str(request.POST.get("username"))
        password = str(request.POST.get("password"))
        email = str(request.POST.get("email"))
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect("account_login")
        else:
            return render(request, 'account/signup.html', {
                "username_taken": True,
            })

    return render(request, 'account/signup.html', {
        "username_taken": False
    })


def account_login(request):
    if request.method == "POST" and request.POST.get("login_submit"):
        username = str(request.POST.get("username"))
        password = str(request.POST.get("password"))
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_index")
        return render(request, 'account/login.html', {
            "invalid_login": True
        })
    return render(request, 'account/login.html', {
        "invalid_login": False
    })


def account_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home_index")

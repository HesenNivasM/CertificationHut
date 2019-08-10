from django.shortcuts import render, redirect
from .models import Course

import re
import json


def classroomcourses_index(request):
    if request.method == "POST" and request.POST.get("submit_enroll_form"):
        course_number = int(request.POST.get("course_number"))
        course_credential = Course.objects.get(pk=course_number)
        students_enrolled = json.decoder.JSONDecoder().decode(
            course_credential.students_enrolled)
        if str(request.user.username) not in students_enrolled:
            students_enrolled.append(str(request.user.username))
        course_credential.students_enrolled = json.dumps(students_enrolled)
        course_credential.save()
        return redirect("account_dashboard")
    if request.method == "POST" and request.POST.get("classroomcourse_submit"):
        course_id = int(request.POST.get("classroomcourse_id"))
        course = Course.objects.get(pk=course_id)
        return render(request, "courses/classroomcourses/course.html", {
            "course": course,
            "image_path": re.findall(r'"([^"]*)"', str(course.image))[0],
        })
    classroomcourses = Course.objects.filter(course_type=1)
    # Get unique categories as a set
    categories = set()
    for classroomcourse in classroomcourses:
        categories.add(classroomcourse.category)
    # Inititalize unique category as a key in dict with list of particular category
    category_dict = {}
    for category in categories:
        category_dict[category] = []
    for classroomcourse in classroomcourses:
        category_dict[classroomcourse.category].append(classroomcourse)
    return render(request, "courses/classroomcourses/index.html", {
        "categories": categories,
        "category_dict": category_dict,
    })


def liveonlinecourses_index(request):
    if request.method == "POST" and request.POST.get("submit_enroll_form"):
        course_number = int(request.POST.get("course_number"))
        course_credential = Course.objects.get(pk=course_number)
        students_enrolled = json.decoder.JSONDecoder().decode(
            course_credential.students_enrolled)
        if str(request.user.username) not in students_enrolled:
            students_enrolled.append(str(request.user.username))
        course_credential.students_enrolled = json.dumps(students_enrolled)
        return redirect("account_dashboard")
    if request.method == "POST" and request.POST.get("liveonlinecourse_submit"):
        course_id = int(request.POST.get("liveonlinecourse_id"))
        course = Course.objects.get(pk=course_id)
        print(re.findall(r'"([^"]*)"', str(course.image))[0])
        return render(request, "courses/liveonlinecourses/course.html", {
            "course": course,
            "image_path": re.findall(r'"([^"]*)"', str(course.image))[0],
        })
    liveonlinecourses = Course.objects.filter(course_type=2)
    # Get unique categories as a set
    categories = set()
    for liveonlinecourse in liveonlinecourses:
        categories.add(liveonlinecourse.category)
    # Inititalize unique category as a key in dict with list of particular category
    category_dict = {}
    for category in categories:
        category_dict[category] = []
    for liveonlinecourse in liveonlinecourses:
        category_dict[liveonlinecourse.category].append(liveonlinecourse)
    return render(request, "courses/liveonlinecourses/index.html", {
        "categories": categories,
        "category_dict": category_dict,
    })

from django.shortcuts import render
from courses.models import Course

import re


def home_index(request):
    if request.method == "POST" and request.POST.get("liveonlinecourse_id"):
        course_id = int(request.POST.get("liveonlinecourse_id"))
        course = Course.objects.get(pk=course_id)
        print(re.findall(r'"([^"]*)"', str(course.image))[0])
        return render(request, "courses/liveonlinecourses/course.html", {
            "course": course,
            "image_path": re.findall(r'"([^"]*)"', str(course.image))[0],
        })
    if request.method == "POST" and request.POST.get("classroomcourse_id"):
        course_id = int(request.POST.get("classroomcourse_id"))
        course = Course.objects.get(pk = course_id)        
        return render(request, "courses/classroomcourses/course.html", {
            "course": course,
            "image_path": re.findall(r'"([^"]*)"', str(course.image))[0],
        })
    liveonlinecourses = Course.objects.filter(course_type=2)
    liveonlinecourses_list = []
    for liveonlinecourse in liveonlinecourses:
        temp = []
        temp.append(liveonlinecourse)
        temp.append(re.findall(r'"([^"]*)"', str(liveonlinecourse.image))[0])
        liveonlinecourses_list.append(temp)
    classroomcourses = Course.objects.filter(course_type=1)[:2]
    classroomcourses_list = []
    for classroomcourse in classroomcourses:
        temp = []
        temp.append(classroomcourse)
        temp.append(re.findall(r'"([^"]*)"', str(classroomcourse.image))[0])
        classroomcourses_list.append(temp)
    return render(request, "home/index.html", {
        "livecourses_list_with_image_path": liveonlinecourses_list,
        "classroomcourses_list_with_image_path": classroomcourses_list,
    })

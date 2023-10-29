from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from .data import courses

# Create your views here.
def list_course(request: HttpRequest):
    return render(request, 'list.html', {
        'courses': courses
    })

def detail_course(request: HttpRequest, course_id: int):
    course = None
    for c in courses:
        if c['id'] == course_id:
            course = c
            break
    if course is None:
        messages.error(request, f"Không tìm thấy khóa học có id = {course_id}")
        return redirect("/courses/list/")
    
    return render(request, 'detail.html', {
        'course': course,
        "courses": courses
    })
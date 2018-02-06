from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

def courses(request):
    courses = Course.objects.all()
    course_list = "- ".join([str(course) for course in courses])
    return HttpResponse(course_list)

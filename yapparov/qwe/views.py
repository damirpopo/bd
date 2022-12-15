from django.shortcuts import render
from datetime import date
from .models import Student, Course
from django.shortcuts import HttpResponseRedirect

def index(request):
    studets = Student.objects.all()
    return render(request, 'index.html', {'students': studets})
def create(request):
    initialize()

    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        course_ids = request.POST.getlist('courses')
        student.save()

        courses = Course.objects.filter(id__in=course_ids)
        student.courses.set(courses, through_defaults={'date':date.today()})
        return HttpResponseRedirect('/')
    courses = Course.objects.all()
    return render(request, 'create.html', {'courses': courses})
def initialize():
    if Course.objects.all().count() == 0:
        Course.objects.create(name = 'Python')
        Course.objects.create(name = 'Django')
        Course.objects.create(name = 'FastAPI')

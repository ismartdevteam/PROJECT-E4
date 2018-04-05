from django.shortcuts import render,redirect
from login.models import Course
from login.models import Sheet
from login.models import Exercise
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
	#main view for the teacher
	context = {}
	return render(request, 'student/index.html', context)

def courses_view(request):
	#view for the courses the teacher is teacher
	Courses = get_object_or_404(Course)
	#Courses = Course.objects.get()
	context = {'courses' : Courses}
	return render(request, 'student/courses_view.html', context)

def sheets_view(request):
	#view for the sheets of all the courses taught by the teacher
	Sheets = Sheet.objects.get()
	context = {'sheets' : Sheets}
	return render(request, 'student/sheets_view.html', context)

def exercises_view(request):
	#view for the exercises of all the courses by the teacher
	Exercies = Exercie.objects.get()
	context = {'exercises' : Exercies}
	return render(request, 'student/exercises_view.html', context)
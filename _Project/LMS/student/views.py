from django.shortcuts import render,redirect
from django.http import Http404
from login.models import Student_Course
from login.models import Student_Sheet
from login.models import Student_Exercise

# Create your views here.

def index(request):
	#main view for the teacher
	context = {}
	return render(request, 'student/index.html', context)

def courses_view(request):
	#view for the courses the student is registered
	try:
		Courses = Student_Course.objects.get(student_id=request.user)
		context = {'courses' : Courses}
	except:
		raise Http404("404")
			
	return render(request, 'student/courses_view.html', context)

def sheets_view(request):
	#view for the sheets of all the courses taught by the teacher
	try:
		Sheets = Student_Sheet.objects.get(student_id=request.user)
		context = {'courses' : Courses}
	except:
		raise Http404("404")
			
	return render(request, 'student/sheets_view.html', context)

def exercises_view(request):
	#view for the exercises of all the courses by the teacher
	try:
		Exercises = Student_Exercise.objects.get(student_id=request.user)
		context = {'courses' : Exercises}
	except:
		raise Http404("404")
			
	return render(request, 'student/exercises_view.html', context)
from django.shortcuts import render

import json, logging
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from login.models import Student_Course, Student_Sheet, Student_Exercise
@csrf_exempt
@login_required
def index(request):
	#main view for the teacher
	User_ID = User.objects.get(username = request.user)
	number_of_courses_registered = Student_Course.objects.filter(student_id = User_ID).count()
	number_of_sheets_registered = Student_Sheet.objects.filter(student_id = User_ID).count()
	number_of_exercises_registered = Student_Exercise.objects.filter(student_id = User_ID).count()
	context = {'number_of_courses_registered' : number_of_courses_registered, 'number_of_sheets_registered' : number_of_sheets_registered, 'number_of_exercises_registered' : number_of_exercises_registered}
	return render(request, 'student/index.html', context)

@csrf_exempt
@login_required
def courses_view(request):
	#view for the courses the student is registered
	context = {}
	try:
		User_ID = User.objects.get(username = request.user)
		print(User_ID)
	except:
		raise Http404("404")
		Courses = Student_Course.objects.filter(student_id = User_ID)
		print(Courses)
		Courses_Names = Course.objects.filter(student_id = User_ID)
		print(Courses_Names)

		context = {'courses' : Courses, 'courses_names' : Courses_Names}
	return render(request, 'student/courses_view.html', context)

def sheets_view(request):
	#view for the sheets of all the courses taught by the teacher
	context = {}
	try:
		User_ID = User.objects.get(username = request.user)
		Sheets = Student_Sheet.objects.filter(student_id=User_ID)
		context = {'courses' : Sheets}
	except:
		raise Http404("404")
			
	return render(request, 'student/sheets_view.html', context)

def exercises_view(request):
	#view for the exercises of all the courses by the teacher
	context = {}
	try:
		User_ID = User.objects.get(username = request.user)
		Exercises = Student_Exercise.objects.filter(student_id=User_ID)
		context = {'courses' : Exercises}
	except:
		raise Http404("404")
			
	return render(request, 'student/exercises_view.html', context)
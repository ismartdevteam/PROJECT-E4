from django.shortcuts import render

import json, logging, datetime
from login.models import Role, Course, LMSUser
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
logger = logging.getLogger(__name__)

@csrf_exempt
@login_required
def index(request):
	courses = Course.objects.filter(teacher_id=request.user)
	number_of_sheets=0
	number_of_exercises=0
	number_of_students=0
	for c in courses:
		sheets=c.getSheets();
		number_of_students+=c.getStudents().count()
		for e in sheets:
			number_of_exercises+=e.getExercises().count()
		number_of_sheets+=sheets.count()
	number_of_exercises= number_of_exercises
	return render(request, 'teacher/index.html', {
		'title':'Home',
    	'courses': courses,
    	'number_of_sheets':number_of_sheets,
    	'number_of_exercises':number_of_exercises,
    	'number_of_students':number_of_students
	})
@csrf_exempt
@login_required
def courses_view(request):
	courses = Course.objects.filter(teacher_id=request.user)

	return render(request, 'teacher/courses.html', {
		'title':'Courses',
    	'courses': courses,

	})

@csrf_exempt
@login_required
def sheets_view(request):
	courses = Course.objects.filter(teacher_id=request.user)
	sheets_data=list()
	for c in courses:
		sheets=c.getSheets();
		number_of_students=c.getStudents().count()
		for e in sheets:
			data={ 
				'course_name':c.course_name,
				'sheet':e,
				}
			sheets_data.append(data)
	return render(request, 'teacher/sheets.html', {
		'title':'Sheets',
		'courses': courses,
    	'sheets_data': sheets_data,

	})

@csrf_exempt
@login_required
def exercises_view(request):
	courses = Course.objects.filter(teacher_id=request.user)
	exercises_data=list()
	for c in courses:
		sheets=c.getSheets();
		number_of_students=c.getStudents().count()
		for e in sheets:
			for ex in e.getExercises():
				number_of_given=ex.getStudentExercises().count()
				
				data={ 
					'course_name':c.course_name,
					'sheet_name':e.sheet_name,
					'exercise': ex,
					'number_of_students':number_of_students,
					'number_of_given':number_of_given,
					'progress':number_of_given/number_of_students*100
					}
				exercises_data.append(data)
	return render(request, 'teacher/exercises.html', {
		'title':'Exercises',
		'courses': courses,
    	'exercises_data': exercises_data,

	})

def activities(request):
	print(request.user)
	courses = Course.objects.filter(teacher_id=request.user)
	students_datas=list()
	for c in courses:
		sheets=c.getSheets();
		for e in sheets:
			exercises=e.getExercises()
			for ex in exercises:
				for se in ex.getStudentExercises():
					data={ 
					'course_name':c.course_name,
					'sheet_name':e.sheet_name,
					'student': se,
					}
					students_datas.append(data)
	print(*students_datas, sep = "\n")
	return render(request, 'teacher/activities.html', {
      	'students_datas':students_datas,
      	'last_loaded':datetime.datetime.now().strftime('%H:%M %p')
    })
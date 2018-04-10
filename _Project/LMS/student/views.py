from django.shortcuts import render
from django.http import JsonResponse
import json, logging
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from login.models import Student_Course, Student_Sheet, Student_Exercise, Course, Sheet
@csrf_exempt
@login_required
def index(request):
	#main view for the student

	#Get the student user
	User_ID = User.objects.get(username = request.user)
	#Get the all the course details the student is registered in 
	courses_details = Student_Course.objects.filter(student_id = User_ID)

	#Creation of JSON object
	JSON_object = list()
	for c in courses_details:
		course_object = Course.objects.get(course_id = c.course_id.course_id)
		entry = {'name' : course_object.course_name, 'mark' : format(c.overall_score, '.2f')}
		JSON_object.append(entry)
	print(*JSON_object,sep='\n')
	JSON_object=json.dumps(JSON_object)
	#print(JSON_object)

	#Get # of Courses, Sheets, and Exercises registered by the student 
	number_of_courses_registered = Student_Course.objects.filter(student_id = User_ID).count()
	number_of_sheets_registered = Student_Sheet.objects.filter(student_id = User_ID).count()
	number_of_exercises_registered = Student_Exercise.objects.filter(student_id = User_ID).count()

	#Pass the information through the context object
	context = {'JSON_object' : JSON_object, 'courses_details' : courses_details, 'number_of_courses_registered' : number_of_courses_registered, 'number_of_sheets_registered' : number_of_sheets_registered, 'number_of_exercises_registered' : number_of_exercises_registered}
	return render(request, 'student/index.html', context)


@csrf_exempt
@login_required
def courses_view(request):
	#view for the courses the student is registered in
	courses = []
	context = {}
	
	#try:
	User_ID = User.objects.get(username = request.user)
	courses_details = Student_Course.objects.filter(student_id = User_ID)

	for c in courses_details:
		course_object = Course.objects.get(course_id = c.course_id.course_id)
		courses.append(course_object)
	#except:
		#raise Http404("404")
	context = {'courses' : courses}
	
	return render(request, 'student/courses_view.html', context)

def sheets_view(request):
	#view for the sheets of all the courses the student is registered in
	sheets_names = []
	context = {}
	
	try:
		User_ID = User.objects.get(username = request.user)
		sheets = Student_Sheet.objects.filter(student_id=User_ID)

		for s in sheets:
			sheet_object = Sheet.objects.get(sheet_id = s.sheet_id.sheet_id)
			sheets_names.append(sheet_object.sheet_name)
	except:
		raise Http404("404")

	context = {'sheets_names' : sheets_names}
			
	return render(request, 'student/sheets_view.html', context)

def exercises_view(request):
	#view for the exercises of all the sheets of all the courses the student is registered in
	questions_names = []
	context = {}

	try:
		User_ID = User.objects.get(username = request.user)
		exercises = Student_Exercise.objects.filter(student_id=User_ID)

		for e in exercises:
			exercise_object = Sheet.objects.get(sheet_id = s.sheet_id.sheet_id)

		context = {'courses' : Exercises}
	except:
		raise Http404("404")
			
	return render(request, 'student/exercises_view.html', context)

@csrf_exempt
@login_required
def course_details(request):
	#view for the details about a course
	course_name_passed = request.GET.get('course_name')

	#get all the students registered in this course
	course = Course.objects.get(course_name = course_name_passed)
	students_registered = Student_Course.objects.filter(course_id = course)

	print(students_registered)

	JSON_object = list()

	for s in students_registered:
		entry = {'student_name' : '' + s.student_id.last_name + ', ' + s.student_id.first_name, 'mark' : format(s.overall_score, '.2f')}
		JSON_object.append(entry)

	#print(*JSON_object,sep='\n')

	JSON_object=json.dumps(JSON_object)

	#print(JSON_object)

	context = {'JSON_object' : JSON_object}
	
	return render(request, 'student/course_details.html', context)
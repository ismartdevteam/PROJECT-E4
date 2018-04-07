from django.shortcuts import render

import json, logging
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
	for c in courses:
		sheets=c.getSheets();
		for e in sheets:
			number_of_exercises+=e.getExercises().count()
		number_of_sheets+=sheets.count()

	number_of_exercises= number_of_exercises
	return render(request, 'teacher/index.html', {
		'title':'Courses',
    	'courses': courses,
    	'number_of_sheets':number_of_sheets,
    	'number_of_exercises':number_of_exercises
	})
@csrf_exempt
@login_required
def courses_view(request):
	courses = Course.objects.filter(teacher_id=request.user)

	return render(request, 'teacher/courses.html', {
		'title':'Courses',
    	'courses': courses,


	})
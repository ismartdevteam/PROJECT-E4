from django.shortcuts import render

# Create your views here.

import json, logging
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# time_spend_succeed, score, from Student_Exercise model and student_id, CORRECT and INCORRECT from Student_Question
from login.models import Student_Exercise, Student_Question

@csrf_exempt
@login_required

def index(request):
	context = {}

	exercises =Student_Exercise.objects.all()
	for ex in exercises:
		questions=Question.objects.filter(exercise_id=ex.exercise_id)
		for q in questions:
			difficulty_index =q.difficulty_index
			answers=Student_Question.objects.filter(Question_id=q)


	questions = Student_Question.objects.all()
	for c in courses:
		sheets=c.getSheets()

	print(courses)
	context={'courses':courses}

	return render(request, 'anticheat/index.html', context)


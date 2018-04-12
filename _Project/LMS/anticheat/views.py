from django.shortcuts import render
from django.http import JsonResponse
import json, logging
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import Per
issionDenied
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from login.models import Student_Course, Student_Sheet, Student_Exercise, Course, Sheet
# Create your views here.

@login_required
@csrf_exempt
def index(request):
	#for i in User.student_id:
	#	cheater_student_id = User.objects.get(exercise_cheater=i)
	


	

	return render(request, 'anticheat/index.html', {'title':'Anticheat'})

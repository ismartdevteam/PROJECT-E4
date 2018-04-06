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
def courses_view(request):
	print('ads')
	try:
		courses = Course.objects.get(teacher_id=request.user)
		print(courses)
	except:
		raise Http404("404")
 	#print(courses)
 	#Getting profss

	return render(request, 'teacher/index.html', {
    	'data': courses
	})

import json, logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from login.models import Role,LMSUser


logger = logging.getLogger(__name__)
@login_required
@csrf_exempt


#This view is the main and first view that is used to handle user 
#requests. It checks which type of user is logging in based on their role.
#If a user is a teacher, the user is redirected to the teacher dashboard.
#If a user is a student, the user is redirected to the student dashboard.
#Note the the redirection code lines in this function redirects to the urls.py,
#and not directly to the html pages.


def index(request):
	try:
		chechUser=request.user.lmsuser
		if chechUser.have_role(Role.TEACHER):
			return HttpResponseRedirect('/teacher/')
		elif chechUser.have_role(Role.STUDENT):
			return HttpResponseRedirect('/student/')
		else:
			return HttpResponseRedirect('/anticheat/')
	except chechUser.DoesNotExist:
		return HttpResponseRedirect('/admin')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

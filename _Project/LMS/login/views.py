import json, logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from login.models import Role,LMSUser
logger = logging.getLogger(__name__)
@login_required
@csrf_exempt
def index(request):
	try:
		chechUser=request.user.lmsuser
		if chechUser.have_role(Role.TEACHER):
			return HttpResponseRedirect('/teacher/courses_view')
		elif chechUser.have_role(Role.TEACHER):
			return HttpResponseRedirect('/student/')
		else:
			return HttpResponseRedirect('/anticheat/')
	except chechUser.DoesNotExist:
		return HttpResponseRedirect('/admin')








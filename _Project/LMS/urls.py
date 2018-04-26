
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from login.views import index,logout_view

from django.conf import settings
urlpatterns = [
url(r'^$', index ),
path('admin/', admin.site.urls),
path('login/', include('login.urls')),
path('anticheat/', include('anticheat.urls')),
path('student/', include('student.urls')),

url('teacher/', include('teacher.urls')),
url(r'^logout/$', logout_view)

]

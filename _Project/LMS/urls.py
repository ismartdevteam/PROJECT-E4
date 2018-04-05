
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from login.views import index
urlpatterns = [
    url(r'^$', index ),
path('admin/', admin.site.urls),
path('login/', include('login.urls')),
path('anticheat/', include('anticheat.urls')),
path('student/', include('student.urls')),
<<<<<<< HEAD
url('teacher/', include('teacher.urls'))

=======
path('teacher/', include('teacher.urls'))
>>>>>>> 34efe62df7c510b73686f706054812b1aff0f98e
]


from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.index ),
    url('courses_view', views.courses_view),
]
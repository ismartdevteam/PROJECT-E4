
from django.conf.urls import url
from . import views

urlpatterns = [
    url('courses_view', views.courses_view),
]
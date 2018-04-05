
from django.conf.urls import url
from . import views

urlpatterns = [
    url('courses', views.courses_view),
]
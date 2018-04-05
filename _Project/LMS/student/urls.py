from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('courses_view/', views.courses_view, name = 'courses'),
	path('sheets_view/', views.sheets_view, name = 'sheets'),
	path('exercises_view/', views.exercises_view, name = 'exercises')
]
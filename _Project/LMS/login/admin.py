from django.contrib import admin

# Register your models here.
from .models import LMSUser
from .models import Course
from .models import Sheet
from .models import Exercise
from .models import Question

admin.site.register(LMSUser)

admin.site.register(Course)

admin.site.register(Sheet)

admin.site.register(Exercise)

admin.site.register(Question)
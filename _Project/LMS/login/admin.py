from django.contrib import admin

# Register your models here.
from .models import LMSUser
from .models import Course
from .models import Sheet
from .models import Exercise
from .models import Question
from .models import Connection
from .models import Student_Course
from .models import Student_Sheet
from .models import Student_Exercise
from .models import Student_Question

admin.site.register(LMSUser)

admin.site.register(Course)

admin.site.register(Sheet)

admin.site.register(Exercise)

admin.site.register(Question)

admin.site.register(Connection)

admin.site.register(Student_Course)

admin.site.register(Student_Sheet)

admin.site.register(Student_Exercise)

admin.site.register(Student_Question)

from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
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
from .models import Role

class LMSUserInline(admin.StackedInline):
    model = LMSUser
    filter_horizontal = ('role',)
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    inlines = (LMSUserInline, )
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display=('__str__', 'course_name', 'course_id')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Sheet)

admin.site.register(Exercise)

admin.site.register(Question)

admin.site.register(Connection)

admin.site.register(Student_Course)

admin.site.register(Student_Sheet)

admin.site.register(Student_Exercise)

admin.site.register(Role)

from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    """ Default role are created at migration. See 'playexo/migrations/xxxx_add_role_data.py'
        If you add a new default role, do not forget to add it to the migration file. """
     
    ADMINISTRATOR = 'AD'
    TEACHER = 'TH'
    STUDENT = 'ST'
    ANTICHEAT = 'AC'
    ROLES = (
        (ADMINISTRATOR, 'Administrator'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (ANTICHEAT, 'Anticheat')
    )
    
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10) 
    email = models.CharField(max_length=20, default="blah") 
    password = models.CharField(max_length=15) 
    role = models.CharField(primary_key = True, max_length=2, choices=ROLES, null = False, default=TEACHER)
    
    def __str__(self):
        return self.role

class LMSUser(models.Model):
      
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE, null = False)
    role = models.ManyToManyField(Role, blank=True)
    
    def is_admin(self):
        return (Role.objects.get(role=Role.ADMINISTRATOR) in self.role.all() or self.user.is_staff or self.user.is_superuser)
  
    def have_role(self, role):
        return (Role.objects.get(role=role) in self.role.all())
    
    def set_role(self, role):
        if not self.have_role(role):
            self.role.add(role)
    
    def unset_role(self, role):
        if self.have_role(role):
            self.role.remove(role)

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    teacher_id = models.IntegerField()
    course_level = models.FloatField()
    teacher_feedback = models.CharField(max_length=100)

    def __str__(self):
        return '\nCourse ID: {}\nTeacher ID: {}\nCourse Level: {}\nTeacher Feedback: {}\n'.format(self.course_id, self.teacher_id, self.course_level, self.teacher_feedback)

class Sheet(models.Model):
    sheet_id = models.IntegerField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sheet_name = models.CharField(max_length=25)
    number_exercises = models.IntegerField()
    end_date = models.DateTimeField()

    def __str__(self):
        return '\nSheet ID: {}\nCourse ID: {}\nSheet Name: {}\nNumber of Exercises: {}\nEnd Date: {}\n'.format(self.sheet_id, self.course_id, self.sheet_name, self.number_exercises, self.end_date)

class Exercise(models.Model):
    exercise_id = models.IntegerField(primary_key=True)
    sheet_id = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    score = models.FloatField()
    difficulty_index = models.FloatField()
    duration_allowed = models.TimeField()
    success_rate = models.FloatField()

    def __str__(self):
        return '\nExercise ID: {}\nSheet ID: {}\nScore: {}\nDifficulty Index: {}\nDuration Allowed: {}\nSuccess Rate: {}\n'.format(self.exercise_id, self.sheet_id, self.score, self.difficulty_index, self.duration_allowed, self.success_rate)

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return '\nQuestion ID: {}\nExercise ID: {}\n'.format(self.question_id, self.exercise_id)
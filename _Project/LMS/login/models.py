from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
class Role(models.Model):
    ADMINISTRATOR = 'AD'
    TEACHER = 'TH'
    STUDENT = 'ST'
    ANTICHEAT = 'AC'
    ROLES = (
        (ADMINISTRATOR, 'Administrator'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (ANTICHEAT, 'Anticheat'),
    )
    
    role = models.CharField(primary_key=True,max_length=2, choices=ROLES, null = False, default=TEACHER)
    
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

    def __str__(self):
        return '\nUsername: {}\nRole: {}\n'.format(self.user, self.role)

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=150)
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_level = models.FloatField(default=0)
    def getSheets(self):
        return Sheet.objects.filter(course_id=self)
    def getStudents(self):
        return Student_Course.objects.filter(course_id=self)
    def __str__(self):
        return '\nID: {}\nName: {}'.format(self.course_id, self.course_name)

class Sheet(models.Model):
    sheet_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    sheet_name = models.CharField(max_length=150)
    number_exercises = models.IntegerField(default=0)
    end_date = models.DateTimeField()
    #sheet_status = finished or not finished #we need something to indicate that a sheet was submitted by the student.
    def getExercises(self):
        return Exercise.objects.filter(sheet_id=self)
    def getStudentsSheet(self):
        return Student_Sheet.objects.filter(sheet_id=self)
    def getMeanScore(self):
        return Student_Sheet.objects.filter(sheet_id=self).aggregate(Avg('score'))
    def getMeanTimeSpent(self):
        return Student_Sheet.objects.filter(sheet_id=self).aggregate(Avg('total_time_spent'))
    def __str__(self):
        return '\nSheet ID: {}\nSheet Name: {}'.format(self.sheet_id, self.sheet_name)

class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    sheet_id = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    difficulty_index = models.FloatField(default=0)
    duration_allowed = models.TimeField(default=0)
    success_rate = models.FloatField(default=0)
    def getStudentExercises(self):
        return Student_Exercise.objects.filter(exercise_id=self).order_by('-submit_date')
    def __str__(self):
        return '\nExercise ID: {}\nSheet ID: {}\n'.format(self.exercise_id, self.sheet_id)

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return '\nQuestion ID: {}\nExercise ID: {}\n'.format(self.question_id, self.exercise_id)

class Connection(models.Model):
    connection_id = models.AutoField(primary_key=True)
    connection_date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Student_Course(models.Model):
    student_course_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    overall_score = models.IntegerField(default=0)
    teacher_feedback = models.CharField(max_length=100,default=0)

class Student_Sheet(models.Model):
    student_sheet_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sheet_id = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    feedback = models.CharField(max_length=100)
    total_time_spent = models.IntegerField(default=0)


class Student_Exercise(models.Model):
    student_exercise_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    number_of_attempts = models.IntegerField(default=0)
    number_of_tries = models.FloatField(default=0)
    time_spend_by_exercises = models.IntegerField(default=0)
    time_spend_succeed = models.IntegerField(default=0)
    total_time_spent = models.IntegerField(default=0)
    number_abort = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    number_correct_attempts = models.IntegerField(default=0)
    student_level = models.CharField(max_length=2)
    completed_time = models.IntegerField(default=0)
    feedback = models.CharField(max_length=100)
    submit_date = models.DateTimeField()
    ##student_exercisecol = models.CharField(max_length=45)

class Student_Question(models.Model):
    student_question_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    SKIPPED = 'SK'
    CORRECT = 'CR'
    INCORRECT = 'IN'
    STARTED = 'ST'
    NULL = 'NL'
    STATUSES = (
        (SKIPPED, 'Skipped'),
        (CORRECT, 'Correct'),
        (INCORRECT, 'Incorrect'),
        (STARTED, 'Started'),
        (NULL, 'Null')
    )
    
    question_status = models.CharField( max_length=2,choices=STATUSES, null = True, default=NULL)
    time_spent = models.IntegerField(default=0)
    submit_date = models.DateTimeField()
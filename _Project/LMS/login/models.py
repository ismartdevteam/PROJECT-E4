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
    
    role = models.CharField(primary_key=True,max_length=2, choices=ROLES, null = False, default=TEACHER)
    
    def __str__(self):
        return self.role

class LMSUser(models.Model):
    user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE, null = False)
    role = models.ManyToManyField(Role, blank=True)
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True) 
    email = models.CharField(max_length=20, null=True) 
    
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
    teacher_id = models.ForeignKey(LMSUser, on_delete=models.CASCADE)
    course_level = models.FloatField()

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

class Connection(models.Model):
    connection_id = models.IntegerField(primary_key=True)
    connection_date = models.DateTimeField()
    user_id = models.ForeignKey(LMSUser, on_delete=models.CASCADE)

class Student_Course(models.Model):
    student_course_id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(LMSUser, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_feedback = models.CharField(max_length=100)

class Student_Sheet(models.Model):
    student_sheet_id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(LMSUser, on_delete=models.CASCADE)
    sheet_id = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    score = models.FloatField()
    feedback = models.CharField(max_length=100)
    total_time_spent = models.IntegerField()

class Student_Exercise(models.Model):
    student_exercise_id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(LMSUser, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    number_of_attempts = models.IntegerField()
    number_of_tries = models.FloatField()
    time_spend_by_exercises = models.IntegerField()
    time_spend_succeed = models.IntegerField()
    total_time_spent = models.IntegerField()
    number_abort = models.IntegerField()
    score = models.FloatField()
    number_correct_attempts = models.IntegerField()
    student_level = models.CharField(max_length=2)
    completed_time = models.IntegerField()
    feedback = models.CharField(max_length=100)
    submit_date = models.DateTimeField()
    ##student_exercisecol = models.CharField(max_length=45)

class Student_Question(models.Model):
    student_question_id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(LMSUser, on_delete=models.CASCADE)
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
    
    question_status = models.IntegerField(max_length=2, choices=STATUSES, null = True, default=NULL)
    time_spent = models.IntegerField()
    submit_date = models.DateTimeField()
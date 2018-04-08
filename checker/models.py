from django.db import models
from teacher.models import Classes
from student.models import Students

# Create your models here.

#
# class Class(models.Model):
#     class_section = models.CharField(max_length=3,primary_key=True)
#
#     def __str__(self):
#         return self.class_section
#
#
# class Students(models.Model):
#     roll_no = models.CharField(max_length=10)
#     name = models.CharField(max_length=20)
#     in_class = models.ForeignKey(Class)
#
#     def __str__(self):
#         return str(self.roll_no) + str(self.name) + str(self.in_class)


class QuestionPaper(models.Model):
    of_class = models.ForeignKey(Classes)
    #subject = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + str(self.of_class)


class Question(models.Model):
    statement = models.CharField(max_length=200)
    total_marks = models.IntegerField()
    question_paper = models.ForeignKey(QuestionPaper)
    question_number = models.IntegerField()

    def __str__(self):
        return str(self.question_paper.id) + str(self.question_paper.of_class) + "-" + str(self.pk)


class AnswerSheet(models.Model):
    of_student = models.ForeignKey(Students)
    of_paper = models.ForeignKey(QuestionPaper)
    sheet = models.FileField(upload_to='media/')


class Marks(models.Model):
    number = models.IntegerField()
    of_student = models.ForeignKey(Students)
    of_question = models.ForeignKey(Question)


class Parameters(models.Model):
    of_question = models.ForeignKey(Question)
    marks = models.IntegerField()
    name = models.CharField(max_length=10)


class ParameterMarks(models.Model):
    of_parameter = models.ForeignKey(Parameters)
    marks = models.IntegerField()
    of_student = models.ForeignKey(Students)


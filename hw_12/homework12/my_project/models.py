from django.db import models


class Homework(models.Model):
    text = models.TextField()
    deadline = models.DurationField()
    created = models.DateTimeField()


class Student(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)


class Teacher(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)


class HomeworkResult(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField()

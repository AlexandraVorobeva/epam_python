from django.contrib import admin

from .models import Student, Teacher, Homework, HomeworkResult

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Homework)
admin.site.register(HomeworkResult)

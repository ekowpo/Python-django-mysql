from django.contrib import admin
from .models import Department,Course,Semester,Lecturer,SemesterCourse

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Lecturer)
admin.site.register(SemesterCourse)

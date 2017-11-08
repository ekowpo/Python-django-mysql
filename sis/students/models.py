from django.db import models

class Student(models.Model):
    firstName= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    dateOfBirth=models.DateField(verbose_name=None)
    email=models.EmailField()
    address=models.CharField(max_length=500)
    postalCode=models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.pk+' - '+self.firstName +' '+self.lastName


class Semester(models.Model):
    SEMESTER_TYPE = (
        ('F', 'Fall'),
        ("S1", 'Summer 1'),
        ("S2", 'Summer 2'),
        ('W', 'Winter'),
    )
    semesterType = models.CharField(max_length=10, choices=SEMESTER_TYPE, null=True)
    startDate=models.CharField(max_length=4 , null=True)
    endDate= models.CharField(max_length=4, null=True)
    dne=models.DateField(auto_now=False,auto_now_add=False, null=True)

    def __str__(self):
        return self.get_semesterType_display() + ' ' + self.startDate


class Lecturer(models.Model):
    firstName= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    dateOfBirth=models.DateField(verbose_name=None)
    email=models.EmailField()
    address=models.CharField(max_length=500)
    postalCode=models.CharField(max_length=10)
    phone= models.CharField(max_length=20)


class Department(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=4)

    def __str__(self):
        return self.code + ' - ' + self.name

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,)

    def __str__(self):
        return self.code + ' - ' + self.name

class Location(models.Model):
    name=models.CharField(max_length=250)
    code=models.CharField(max_length=6)

    def __str__(self):
        return self.code + ' - ' + self.name


class SemesterCourse(models.Model):
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE, )
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,)
    lecturer = models.ForeignKey(
        Lecturer,
        on_delete=models.CASCADE, )
    location=models.ForeignKey(
        Location,
        on_delete=models.CASCADE,)
    DAYS=(("Mon",'Monday'),
         ("Tues", 'Tuesday'),
         ("Wed",'Wednessday'),
         ("Thu", "Thursday"),
         ("Fri","Friday"),)
    start_Time=models.DateTimeField
    end_Time= models.TimeField
    day=models.CharField(max_length=3, choices=DAYS, null=True)

class CourseRegistration(models.Model):
    class Meta:
        unique_together = (('student', 'course'),)
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE,)
    course=models.ForeignKey(
        SemesterCourse,
        on_delete=models.CASCADE,)
    status =(("C", "Completed"), ("D","Droped"),)
    grade = (("A+", "A+"), ("A", "A"), ("A-", "A-"), ("B+", "B+"), ("B", "B"), ("B-", "B-"), ("C", "C"), ("F", "F"))




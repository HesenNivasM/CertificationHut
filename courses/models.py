from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Course(models.Model):
    title = models.CharField(max_length=10000)
    # 1 for classroomcourses and 2 for liveonlinecourses
    instructor = models.CharField(max_length=10000)
    course_type = models.IntegerField(choices=[
        (1, "Classroom Courses"),
        (2, "Live Online Courses")
    ])
    image = RichTextUploadingField()
    category = models.CharField(max_length=1000)
    price = models.IntegerField()
    description = RichTextUploadingField()
    curriculum = RichTextUploadingField()
    lectures = models.IntegerField()
    no_of_quizzes = models.IntegerField()
    duration = models.IntegerField()  # In hours
    skill_level = models.CharField(max_length=1000)
    language = models.CharField(max_length=1000)
    no_of_students = models.IntegerField()
    students_enrolled = models.CharField(max_length=10000, default="[]")
    certificate_type = models.CharField(max_length=1000)
    asssessment_type = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.title + " by " + self.instructor)

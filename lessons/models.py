"""Models for the lessons app"""
from django.db import models
from profiles.models import Teacher
from students.models import Student


# Time periods variations
TIME_PERIODS = (
    (0, '9:00-9:45'),
    (1, '10:00-10:45'),
    (2, '11:00-11:45'),
    (3, '14:00-14:45'),
    (4, '15:00-15:45'),
    (5, '16:00-16:45'),
    (6, '17:00-17:45'),
    (7, '18:00-18:45'),
)

# Subject variations
SUBJECTS = (
    (1, 'art'),
    (2, 'math'),
    (3, 'casa'),
    (4, 'chinese'),
    (5, 'toddlers'),
    (6, 'music'),
    (7, 'english'),
    (8, 'sport'),
    (9, 'cooking'),
    (10, 'infants'),
)

class Lesson(models.Model):
    """Lesson model"""
    date = models.DateField()
    time = models.IntegerField(choices=TIME_PERIODS, default=0)
    subject = models.IntegerField(choices=SUBJECTS, default=1)
    teachers = models.ManyToManyField(Teacher, related_name='lessons')
    students = models.ManyToManyField(Student, related_name='lessons')

    def get_time(self):
        """Get time period name of the lesson"""
        return dict(TIME_PERIODS)[self.time]

    def get_subject(self):
        """Get subject name of the lesson"""
        return dict(SUBJECTS)[self.subject]

    def get_subjects(self):
        """Get all subjects choices of the lesson"""
        return dict(SUBJECTS)

    def get_time_periods(self):
        """Get all time periods choices of the lesson"""
        return dict(TIME_PERIODS)

    def get_teachers(self):
        """Get all teachers of the lesson"""
        return self.teachers.all()

    def get_students(self):
        """Get all students of the lesson"""
        return self.students.all()

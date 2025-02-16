# from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('employer', 'Employer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True, blank=True)
    
    # Student fields
    degree = models.CharField(max_length=100, null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)

    # Employer fields
    current_role = models.CharField(max_length=100, null=True, blank=True)
    experience_years = models.IntegerField(null=True, blank=True)

    # Skill fields
    software_skills = models.TextField(blank=True)  # Comma-separated
    music_skills = models.TextField(blank=True)
    sports_skills = models.TextField(blank=True)

    # Scoring system
    mentor_score = models.IntegerField(default=0)
    mentee_score = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        "auth.Group", related_name="customuser_set", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="customuser_permissions", blank=True
    )

    def total_score(self):
        return self.mentor_score + self.mentee_score

    def __str__(self):
        return self.username

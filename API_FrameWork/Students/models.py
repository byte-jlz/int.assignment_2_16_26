from django.db import models

class StudentProfile(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    year_level = models.IntegerField()
    
    RELATIONSHIP_CHOICES = [
        ('Single', 'Single'),
        ('In a Relationship', 'In a Relationship'),
        ('Married', 'Married'),
    ]
    relationship_status = models.CharField(
        max_length=20, 
        choices=RELATIONSHIP_CHOICES, 
        default='Single'
    )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
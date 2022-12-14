from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

# Create your models here.

Locations = (
    ('M', 'Muharraq'),
    ('S', 'Seef')
)

class Class(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    trainer = models.CharField(max_length=100)
    location = models.CharField(
        max_length=1,
        choices=Locations,
        default=Locations[0][0]
    )
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    days = ArrayField(models.CharField(max_length=100), size = 2)
    time = models.TimeField('Start Time')
    duration = models.CharField(max_length=100)
    seats = models.IntegerField('Total Seats')

    def __str__(self):
        return self.name

class Membership(models.Model):
    location = models.CharField(
        max_length=1,
        choices=Locations,
        default=Locations[0][0]
    )
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    user_code = models.IntegerField(default=0, blank=True)
    credit = models.IntegerField(default=0, blank=True)
    image = models.CharField(max_length=800, default='image not available', blank=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    classes = models.ManyToManyField(Class, blank=True)
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone 
 

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = models.TextField(max_length=5000)
    event_location = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_ticket = models.CharField(max_length=200)
    skills_keynote = models.BooleanField()
    skills_facilitator = models.BooleanField()
    skills_mentor = models.BooleanField()
    skills_expert = models.BooleanField()
    skills_enthusiast = models.BooleanField()
    class Size(models.IntegerChoices):
        INTIMATE = 1
        SMALL = 2
        MEDIUM = 3
        LARGE = 4
        VERYLARGE = 5
        HUGE = 6
    event_size = models.IntegerField(choices=Size.choices)
    is_paid = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.URLField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="host"
    )


class Application(models.Model):
    reason_apply = models.TextField(max_length=5000)
    is_assessed = models.BooleanField()
    is_accepted = models.BooleanField()
    apply_keynote = models.BooleanField()
    apply_facilitator = models.BooleanField()
    apply_mentor = models.BooleanField()
    apply_expert = models.BooleanField()
    apply_enthusiast = models.BooleanField()
    is_anon = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='hero'
    )

class ReviewEvent(models.Model):
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        related_name='review_event'
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='review_hero'
    )
    comment = models.TextField(max_length=2000)
    class Scale(models.IntegerChoices):
        ONESTAR = 1
        TWOSTARS = 2
        THREESTARS = 3
        FOURSTARS = 4
        FIVESTARS = 5
    rating = models.IntegerField(choices=Scale.choices)

class ReviewApplication(models.Model):
    application = models.ForeignKey(
        'Application',
        on_delete=models.CASCADE,
        related_name='review_application'
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='review_host'
    )
    comment = models.TextField(max_length=2000)

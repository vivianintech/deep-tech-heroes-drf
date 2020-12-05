from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_hero = models.BooleanField(default=False)
    is_host = models.BooleanField(default=False)
    rec_newsletter = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.username


class HostUser(CustomUser):
    organisation_name = models.CharField(max_length=100)
    organisation_logo = models.URLField()
    host_phone = models.CharField(max_length=10)


class HeroUser(CustomUser):
    year_of_birth = models.IntegerField()
    hero_phone = models.CharField(max_length=10)
    hero_location = models.CharField(max_length=100)
    hero_image = models.URLField()
    linkedin_url = models.URLField()
    hero_bio = models.CharField(max_length=5000)
    gender = models.CharField(max_length=25)
    pref_pronoun = models.CharField(max_length=50)
    has_bluecard = models.BooleanField()
    has_yellowcard = models.BooleanField()
    is_virtual_accepted = models.BooleanField()
    is_paid_preferred = models.BooleanField()
    culture = models.CharField(max_length=250)
    hero_language = models.CharField(max_length=200)
    hero_disability = models.BooleanField()
    badge_keynote = models.BooleanField()
    badge_facilitator = models.BooleanField()
    badge_mentor = models.BooleanField()
    badge_expert = models.BooleanField()
    badge_enthusiast = models.BooleanField()



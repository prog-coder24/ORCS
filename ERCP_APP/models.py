from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    #Add fields here
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


CATEGORY = (
    ("OPEN","OPEN"),
    ("OBC","OBC"),
    ("ST", "ST"),
    ("SC", "SC"),
    ("NT", "NT")
)

RAILWAY_LINE=(
    ("Central Railways","Central Railways"),
    ("Western Railways","Western Railways")
)

RAILWAY_CLASS=(
    ("First Class","First Class"),
    ("Second Class","Second Class")
)

DURATION=(
    ("Monthly","Monthly"),
    ("Quaterly","Quaterly")
)


class CardDetails(models.Model):
    user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, related_name='card_details')
    user_name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    category = models.CharField(max_length=100, null=False, blank=False, choices=CATEGORY)
    academic_class = models.CharField(max_length=8, null=False, blank=False)
    roll_no = models.IntegerField(null=False, blank=False, unique=True)
    division = models.IntegerField(null=False, blank=False)
    date_of_birth = models.DateField(max_length=50, null=False, blank=False)
    years = models.IntegerField(null=False, blank=False)
    months = models.IntegerField(null=False, blank=False)
    residential_addr = models.CharField(max_length=755, null=False, blank=False)
    taluka = models.CharField(max_length=50, null=False, blank=False)
    district = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    journey_from = models.CharField(max_length=50, null=False, blank=False)
    journey_to = models.CharField(max_length=50, null=False, blank=False)
    via = models.CharField(max_length=50, null=True, blank=True)
    railway_line = models.CharField(max_length=100, null=False, blank=False, choices=RAILWAY_LINE)

    def __str__(self):
        return self.user_name

class FormDetails(models.Model):
     user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, related_name='form_details')
     railway_class = models.CharField(max_length=100, null=False, blank=False, choices=RAILWAY_CLASS)
     duration = models.CharField(max_length=100, null=False, blank=False, choices=DURATION)
     issue_date = models.DateTimeField(default=timezone.now)
     applied_date = models.DateTimeField(default=timezone.now)
     status = models.BooleanField(default=False)

     def __str__(self):
        return self.status

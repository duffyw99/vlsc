from __future__ import unicode_literals

from django.db import models

# Classes are table names

SUFFIX_CHOICES = (
    (1, ''),
    (2, 'Jr'),
    (3, '3rd'),
    (4, '4th'),
)

class MemberQueryset(models.query.Queryset):
    def active(self):
        return self.filter(active=True)

    def on_staff(self):
        return self.filter(on_staff=True)

class MemberManager(models.Manager):
    def get_queryset(self):
        return MemberQueryset(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def on_staff(self):
        return self.get_queryset().on_staff()
# Below will return active members on staff (update Profile table to relevant)
# Profile.objects.on_staff().active()

class Profile(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    suffix = models.CharField(max_length=1, choices=SUFFIX_CHOICES, default=1)
    recruit_class = models.CharField(max_length=3)
    recruit_year = models.PositiveSmallIntegerField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=100)
    member_photo = models.CharField(max_length=1000)

    objects = MemberManager()

    def __unicode__(self):
        return self.last_name + ', ' + self.first_name

class Contact(models.Model):
    # member primary key, delete all addresses associated
    member_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    member_street = models.CharField(max_length=250)
    member_city = models.CharField(max_length=250)
    member_state = models.CharField(max_length=2)
    member_zip = models.PositiveSmallIntegerField()
    member_email = models.EmailField(max_length=254)
    email_opt_in = models.BooleanField(defaul=False)
    member_phone = models.CharField(max_length=250)
    text_opt_in = models.BooleanField(default=False)
    phone_service = models.CharField(max_length=250)
    last_mod  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.member_email

STANDING_CHOICES = (
    ('Good Standing','Good Standing'),
    ('School Leave','School Leave'),
    ('Military Leave','Military Leave'),
    ('Suspended','Suspended'),
    ('Simple Discharge','Simple Discharge'),
    ('Dishonorable Discharge','Dishonorable Discharge'),
)

RETIRED_CHOICES = (
    ('', 'Not Retired'),
    ('Honorably Retired', 'Honorably Retired'),
    ('Medically Retired', 'Medically Retired'),
    ('Honorary Retirement', 'Honorary Retirement'),
)

class Disposition(models.Model):
    member_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    standing = models.CharField(max_length=50, choices=STANDING_CHOICES, default='Good Standing')
    leave_start_date = models.DateField(blank=True, null=True)
    leave_end_date = models.DateField(blank=True, null=True)
    on_staff = models.BooleanField(default=False)
    retired = models.BooleanField(default=False)
    retirement_type = models.CharField(max_length=50, choices=RETIRED_CHOICES, default='')
    past_captain = models.BooleanField(default=False)
    honorary_member = models.BooleanField(default=False)
    deceased = models.BooleanField(default=False)
    deceased_date = models.DateField(blank=True, null=True)
    last_mod = models.DateTimeField(auto_now=True)

class Points(models.Model):
    recorded_date = models.DateTimeField(auto_now_add=True)
    member_id = models.ForeignKey(Profile, on_delete=models.PROTECT)
    service_date = models.DateField()
    season = models.PositiveSmallIntegerField()
    service_type = models.CharField(max_length=50)
    points = models.SmallIntegerField()
    member_age = models.PositiveSmallIntegerField()


### Function to determine member's age:  ###
# from datetime import date
#
# def calculate_age(birth_date):
#    today = date.today()
#    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
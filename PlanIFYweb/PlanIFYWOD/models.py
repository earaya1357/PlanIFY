from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = [
    ('ACTIVE', 'ACTIVE'),
    ('INACTIVE', 'INACTIVE'),
    ('DISABLED', 'DISABLED'),
]

EVENT_STATUS = [
    ('ACTIVE', 'ACTIVE'),
    ('INACTIVE', 'INACTIVE'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('CANCELLED', 'CANCELLED'),
    ('POSTPONED', 'POSTPONED')
]
SIZE = [
    ('10-50', 50),
    ('50-100', 100),
    ('100-200', 200),
    ('200-500', 500)
   ]

EVENT_TYPE = [
    ('Individual', 'Individual'),
    ('Team', 'Team'),
    ('Coed', 'Coed'),
]

WORKOUT_TYPES = [
    ('Every Minute On The Minute(EMOM)', 'EMOM'),
    ('As Many Reps As Possible (AMRAP)', 'AMRAP'),
    ('For Time', 'Time'),
    ('Tabata', 'Tabata'),
]

GENDERS = [
    ('Male', 'Male'),
    ('Female', 'Female')
]




class UserAccount(models.Model):
    username = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True, db_column='username')
    user_id_number = models.AutoField(primary_key=True, unique=True)
    status_user = models.CharField(max_length=20, choices=STATUS, default='ACTIVE', null=False, blank=True)
    gener_user = models.CharField(max_length=15, choices=GENDERS, default='Male')
    date_joined_user = models.DateField(null=False, auto_now_add=True, blank=True)
    first_name_user = models.CharField(max_length=25, null=False, blank=True)
    last_name_user = models.CharField(max_length=25, null=False, blank=True)
    age_user = models.IntegerField(null=False, blank=True)
    email_user = models.EmailField(max_length=75, blank=True)
    phone_number_user = models.CharField(max_length=20, blank=True)
    address_user = models.CharField(max_length=100, blank=True)
    city_user = models.CharField(max_length=100, blank=True)
    zip_code_user = models.CharField(max_length=100, blank=True)
    host_user = models.BooleanField(null=True, blank=True)
    athlete_user = models.BooleanField(null=True, blank=True)
    vendor_user = models.BooleanField(null=True, blank=True)
    user_bio = models.TextField(null=True, max_length=250, blank=True)
    user_picture = models.ImageField(null=True, blank=True)


    def __str__(self) -> str:
        return str(self.username)


class Affiliate(models.Model):
    affiliate_id_number = models.AutoField(primary_key=True, unique=True)
    name_affiliate = models.CharField(max_length=50, null=False)
    status_affiliate = models.CharField(max_length=20, choices=STATUS, default='ACTIVE', null=False)
    date_joined_affiliate = models.DateField(null=False, auto_now_add=True)
    email_affiliate = models.EmailField(max_length=75)
    phone_number_affiliate = models.CharField(max_length=20)
    address_affiliate = models.CharField(max_length=100)
    city_affiliate = models.CharField(max_length=100)
    zip_code_affiliate = models.CharField(max_length=100)
    bio_affiliate = models.TextField(null=True, max_length=500)
    website_affiliate = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name_affiliate
    

class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name_vendor = models.CharField(max_length=100)
    description_vendor = models.TextField(max_length=500)
    email_vendor = models.EmailField(max_length=75, blank=True)
    phone_number_vendor = models.CharField(max_length=20, blank=True)
    address_vendor = models.CharField(max_length=100, blank=True)
    city_vendor = models.CharField(max_length=100, blank=True)
    zip_code_vendor = models.CharField(max_length=100, blank=True)
    webiste_vendor = models.URLField(blank=True)



class AffiliateMember(models.Model):
    row_id = models.AutoField(primary_key=True, unique=True)
    name_of_affiliate = models.ForeignKey(Affiliate, on_delete=models.Case, related_name='+')
    id_of_user = models.ForeignKey(UserAccount, on_delete=models.Case, related_name='+')
    first_name_of_member = models.ForeignKey(UserAccount, on_delete=models.Case, related_name='+')
    last_name_of_member = models.ForeignKey(UserAccount, on_delete=models.Case, related_name='+')
    approved_member = models.BooleanField(default=False)
    date_requested_to_join = models.DateField(auto_now=True)
    date_approved = models.DateField(auto_now=True)
    

class Event(models.Model):
    event_id = models.AutoField(primary_key=True, unique=True)
    event_host_user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, db_column='username')
    event_host_affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    event_status = models.CharField(max_length=25, choices=EVENT_STATUS, default='ACTIVE',null=False)
    event_name = models.CharField(max_length=100, unique=True)
    event_date_created = models.DateField(null=False, auto_now=True)
    event_date = models.DateField(null=False)
    event_size = models.CharField(max_length=10, choices=SIZE, default='50-100', null=False)
    event_location = models.CharField(max_length=100)
    event_address = models.CharField(max_length=100)
    event_phone_number = models.CharField(max_length=20)
    event_description = models.TextField(max_length=512)
    event_tshirts = models.BooleanField(default=False)
    event_type = models.TextField(max_length=20, choices=EVENT_TYPE, default='Individual',null=False)
    event_registration_date_open = models.DateField(null=True)
    event_registration_date_close = models.DateField(null=True)
    event_price_athlete = models.FloatField(default=0.00)
    event_price_general = models.FloatField(default=0.00)
    event_promo_code = models.BooleanField(default=False)
    event_waiver = models.BooleanField(default=False)
    event_waiver_document = models.FileField(null=True, blank=True)
    event_prizes = models.BooleanField(default=False)
    event_vendors = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.event_name
    


class EventParticipant(models.Model):
    participants = models.AutoField(primary_key=True)
    event_id_number = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name_of_athlete = models.ForeignKey(UserAccount, on_delete=models.CASCADE, blank=True, null=True)
    last_name_of_athlete = models.CharField(max_length=100, blank=True, null=True)
    email_of_athlete = models.CharField(max_length=100, blank=True)
    event_joing_date = models.DateField(null=False, auto_created=True)



class EventWorkOut(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    event = models.ForeignKey(Event, null=False, blank=False, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=50, choices=WORKOUT_TYPES)
    workout_description = models.TextField(max_length=250, blank=True, null=True)
    workout_time = models.TimeField(null=True, blank=True)
    workout_floater = models.BooleanField(default=False)
    

class EventVendor(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
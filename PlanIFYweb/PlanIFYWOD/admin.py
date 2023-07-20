from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Affiliate)
admin.site.register(AffiliateMember)
admin.site.register(Event)
admin.site.register(EventParticipant)
admin.site.register(Vendor)
admin.site.register(EventVendor)
admin.site.register(EventWorkOut)
admin.site.register(EventTeam)
admin.site.register(RegisteredEvents)
admin.site.register(EventPrizes)


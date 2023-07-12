from django.contrib import admin
from .models import UserAccount, Event, Affiliate, EventParticipant, AffiliateMember, Vendor, EventVendor, EventWorkOut, EventTeam

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


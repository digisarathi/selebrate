from django.contrib import admin
from selebrate.models import User, Vendor, Event, ServiceType, EventType

admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Event)
admin.site.register(ServiceType)
admin.site.register(EventType)

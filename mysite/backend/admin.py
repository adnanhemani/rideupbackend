from django.contrib import admin

# Register your models here.

from .models import User, Group, EventRequests, Event, EventRideGroup

admin.site.register(User)
admin.site.register(Group)
admin.site.register(EventRequests)
admin.site.register(Event)
admin.site.register(EventRideGroup)

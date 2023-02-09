from django.contrib import admin
from .models import User, Events, EventUser

admin.site.register(User)
admin.site.register(Events)
admin.site.register(EventUser)
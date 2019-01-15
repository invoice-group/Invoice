from django.contrib import admin
from web.models import Profile, User, Invoice, Statistics

# Register your models here.
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Invoice)
admin.site.register(Statistics)
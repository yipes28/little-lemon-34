from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Booking)
admin.site.register(models.MenuItem)

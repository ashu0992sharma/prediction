from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Hostel)
admin.site.register(models.Gallery)
admin.site.register(models.Room)
admin.site.register(models.Notices)

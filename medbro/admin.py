from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Check_time)

admin.site.register(models.Chat)
admin.site.register(models.Notification)
admin.site.register(models.Time)


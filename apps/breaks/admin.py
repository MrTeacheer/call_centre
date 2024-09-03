from django.contrib import admin
from . import models
@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id','name','director')

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','name','organization','manager','min_active')
from django.contrib import admin
from . import models
@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id','name','director')

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','name','organization','manager','min_active')


@admin.register(models.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id','group','date','break_start','break_finish','break_max_duration')

@admin.register(models.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('id','code','name','is_active')

@admin.register(models.ReplacementEmployee)
class ReplacementEmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','replacement','employee','status')
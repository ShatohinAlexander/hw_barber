from django.contrib import admin

from .models import Master, Service, Visit

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "contact_info")

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
     list_display = (
        "name",
        "phone",
        "created_at",
        "status",
        "master",
    )
     
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
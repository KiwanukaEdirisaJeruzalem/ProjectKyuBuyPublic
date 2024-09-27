from django.contrib import admin

from RetailsAndTechs.models import Rating, Retailer, Technician


# Register your models here.
@admin.register(Rating)
class RetailerAdmin(admin.ModelAdmin):
    pass


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    pass


@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    pass
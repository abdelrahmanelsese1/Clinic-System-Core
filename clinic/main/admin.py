from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Clinic)
admin.site.register(Doctor)
admin.site.register(Assistant)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Labs)
admin.site.register(Prescription)
admin.site.register(Bill)
admin.site.register(Surgery)
admin.site.register(Material)
admin.site.register(Clinic_Phone)
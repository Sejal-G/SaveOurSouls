from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(User_Base)
admin.site.register(Hospital_Base)
admin.site.register(Hospital_Location)
admin.site.register(Hospital_Wards)
admin.site.register(Hospital_OPD)

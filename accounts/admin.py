from django.contrib import admin
from .models import crime, criminal

# Register your models here.

admin.site.register(criminal)
admin.site.register(crime)
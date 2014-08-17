from django.contrib import admin

# Register your models here.
from court.models import UserProfile


admin.site.register(UserProfile)

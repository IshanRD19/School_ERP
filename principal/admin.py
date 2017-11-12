from django.contrib import admin
from .models import login_info, Personal_Info
# Register your models here.
admin.site.register(login_info)
admin.site.register(Personal_Info)
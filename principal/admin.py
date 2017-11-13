from django.contrib import admin
from .models import login_info, Personal_Info, Subjects, Rooms_2018
# Register your models here.
admin.site.register(login_info)
admin.site.register(Personal_Info)
admin.site.register(Subjects)
admin.site.register(Rooms_2018)
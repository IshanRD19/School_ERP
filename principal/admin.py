from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(login_info)
admin.site.register(Personal_Info)
admin.site.register(Subjects)
admin.site.register(Rooms)
admin.site.register(AssignmentParameters)
admin.site.register(Messages)
from django.contrib import admin
from Question_Bank.models import *

# Register your models here.

admin.site.register(Questions)
admin.site.register(Question_Papers)
admin.site.register(Log)
admin.site.register(Session)
admin.site.register(Responses)

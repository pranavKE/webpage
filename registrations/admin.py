from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Recruiter)
admin.site.register(Partner)
admin.site.register(Skills)
admin.site.register(Work_Loc)

admin.site.register(Worker_model)

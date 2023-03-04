from django.contrib import admin

from .models import Finch, Ribbon, Nest

# Register your models here.
admin.site.register(Finch)
admin.site.register(Nest)
admin.site.register(Ribbon)

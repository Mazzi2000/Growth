from django.contrib import admin
from .models import Grow
# Register your models here.

class GrowAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'completed')

admin.site.register(Grow, GrowAdmin)
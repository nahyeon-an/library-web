from django.contrib import admin
from dashboard.models import Blindbook

# Register your models here.
@admin.register(Blindbook)
class BlindbookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'publisher')
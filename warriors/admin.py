from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('email','username')
    list_display = ('email','username')

# @admin.register(Explain)
# class ExplainAdmin(admin.ModelAdmin):
#     pass
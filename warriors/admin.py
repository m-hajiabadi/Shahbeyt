from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('email','username')
    list_display = ('email','username')


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    search_fields = ('ghaleb','id','beyt_numbers')
    list_display = ('ghaleb','id','beyt_numbers')


@admin.register(Beyt)
class BeytAdmin(admin.ModelAdmin):
    search_fields = ('context','id')
    list_display = ('context','id')

# @admin.register(Explain)
# class ExplainAdmin(admin.ModelAdmin):
#     pass
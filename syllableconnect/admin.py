from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(WordBank)
class WordBankAdmin(admin.ModelAdmin):
    list_display = ['word']  # Shows word column in the list view
    search_fields = ['word']  # Adds search functionality


@admin.register(SyllableBank)
class SyllableBankAdmin(admin.ModelAdmin):
    list_display = ['word']
    search_fields = ['word']
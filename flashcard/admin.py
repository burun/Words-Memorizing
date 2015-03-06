from django.contrib import admin
from flashcard.models import FlashCard


class FlashCardAdmin(admin.ModelAdmin):
    fields = ['front', 'back', 'user']
    list_display = (
        'front', 'back', 'user', 'next_practice', 'times_practiced', 'easy_factor')

admin.site.register(FlashCard, FlashCardAdmin)

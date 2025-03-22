from django.contrib import admin
from .models import Poll, Option, Response


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'question', 'active_until', 'status')
    list_filter = ('status',)
    search_fields = ['title', 'question']

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'poll')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'response_time', 'poll')





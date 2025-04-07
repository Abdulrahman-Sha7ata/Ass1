from django.contrib import admin
from django import forms
from .models import Poll, Option, Response

class PollOptionInline(admin.TabularInline):
    model = Option
    extra = 1

class PollAdminForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Symbols' in title:
            raise forms.ValidationError('No Symbols Allowed in title -:)')
        return title

class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'question', 'active_until', 'status', 'status_display', 'responses_count')
    list_filter = ('status',)
    inlines = [PollOptionInline]
    form = PollAdminForm
    search_fields = ('title', 'question')

    def responses_count(self, obj):
        return obj.responses.count()
    responses_count.short_description = 'Number of Responses'

    def status_display(self, obj):
        return str(obj.status).upper() if obj.status is not None else ''
    status_display.short_description = 'Status Display'

admin.site.register(Poll, PollAdmin)

class PollOptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'poll_title', 'poll_option_list', 'poll_question')
    list_filter = ('poll',)
    search_fields = ('title', 'poll__question')

    def poll_question(self, obj):
        return obj.poll.question    
    poll_question.short_description = 'P Question'

    def poll_title(self, obj):
        return obj.poll.title
    poll_title.short_description = 'P Title'

    def poll_option_list(self, obj):
        return ", ".join(option.title for option in obj.poll.options.all())

    poll_option_list.short_description = 'P Options'

admin.site.register(Option, PollOptionAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'response_time', 'poll', 'option_display')
    list_filter = ('poll', 'option')

    def response_time(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M:%S') if hasattr(obj, 'created_at') and obj.created_at else ''
    response_time.short_description = 'Response Time'

    def option_display(self, obj):
        return str(obj.option)
    option_display.short_description = 'Option'

admin.site.register(Response, ResponseAdmin)

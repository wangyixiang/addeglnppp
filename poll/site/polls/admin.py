from models import Poll
from models import Choice
from django.contrib import admin

# Register your models here.

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    # fields = [
    #     "pub_date",
    #     "question"
    # ]
    fieldsets = [
        (None, {'fields':['question']}),
        ('Date Infomation', {'fields':['pub_date'], 'classes':['collapse']})
    ]

    inlines = [ChoiceInline]

    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
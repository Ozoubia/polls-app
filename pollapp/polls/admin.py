from django.contrib import admin

from .models import Question, Choice

# changing the title and header in the admin area
admin.site.site_header = "Polls admin"
admin.site.site_title = "Polls admin area"
admin.site.index_title = "Welcome to the polls admin area"


# used to add the choices inside the questions
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']},)
                 ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


# these are used to show the models in the admin django page
# admin.site.register(Question)
# admin.site.register(Choice)




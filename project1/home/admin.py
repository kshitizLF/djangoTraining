from django.contrib import admin


from .models import Member,Question,Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date',"question_text"]

admin.site.register(Member)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
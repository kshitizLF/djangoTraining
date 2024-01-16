from django.contrib import admin


from .models import Member,Question,Choice
# Register your models here.
admin.site.register(Member)
admin.site.register(Question)
admin.site.register(Choice)
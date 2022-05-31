from django.contrib import admin
from .models import BankTestModel, UserAnswer


class BankTestAdmin(admin.ModelAdmin):
    list_display = ['question', 'first_answer', 'second_answer', 'third_answer', 'correct_answer']


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'question', 'answer', 'status']
    list_filter = ['user', 'created_at', 'status']


admin.site.register(BankTestModel, BankTestAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)

from django.contrib import admin
from .models import User, Student, StudentAnswer, Quiz, Question, Answer, TakenQuiz, Degree_Batch
from django.contrib.auth.admin import UserAdmin


class Degree_BatchAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)
admin.site.register(Degree_Batch, Degree_BatchAdmin)

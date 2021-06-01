from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class Degree_BatchAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Degree_Batch, Degree_BatchAdmin)

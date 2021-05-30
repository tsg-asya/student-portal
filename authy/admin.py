from django.contrib import admin
from .models import *


class Degree_BatchAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Degree_Batch, Degree_BatchAdmin)

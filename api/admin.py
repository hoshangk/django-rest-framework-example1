from django.contrib import admin
from .models import movie
# Register your models here.

class movieAdmin(admin.ModelAdmin):
	list_display = ['name','director','_99popularity','imdb_score','genre']


admin.site.register(movie, movieAdmin)

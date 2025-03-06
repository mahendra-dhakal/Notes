from django.contrib import admin
from .models import Note , NoteCategory

# Register your models here.
admin.site.register(Note)
admin.site.register(NoteCategory)

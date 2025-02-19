from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NoteCategory(models.Model):
    name=models.CharField(max_length=200)

class Note(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField()
    date_created=models.DateField(auto_now_add=True)
    notecategory=models.ForeignKey(NoteCategory, on_delete=models.SET_NULL, null=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    





    


from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteCategory  

# Create your views here.

def home(request):
    note_obj=Note.objects.all()
    data={'notes':note_obj}
    return render(request, 'index.html', context=data)

def create(request):
    notecategory_obj=NoteCategory.objects.all()
    note_category={'notecategory':notecategory_obj}
    return render(request,'create.html',context=note_category)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, NoteCategory  
from .forms import NoteCategoryForm

# Create your views here.

def home(request):
    note_obj=Note.objects.all() 
    note_category_obj= NoteCategory.objects.all()
    
    data={'notes':note_obj , 'note_categories':note_category_obj}
    return render(request, 'index.html', context=data,)

    


def create_note(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        category_id=request.POST.get('category')
        
        note_category_object = NoteCategory.objects.get(id=category_id)   #brings notecategory as a object with help of id given to get method
        
        # name and description can be stored directly as values in the database but notecategory cannot be stored in the database directly as their value because it is relation field . so we have to pass the object to store value 
        
        Note.objects.create(name=name, description= description,notecategory=note_category_object)
        
    notecategory_obj=NoteCategory.objects.all()
    note_category={'notecategory':notecategory_obj}
    return render(request,'create_note.html',context=note_category)

def create_note_category(request):
    if request.method=='POST':
        form=NoteCategoryForm(request.POST)
        if form.is_valid():
            form.save()
    
    note_category_form=NoteCategoryForm()
    data={'notecategory_form':note_category_form}
    return render(request,'create_note_category.html',context=data)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note, NoteCategory  
from .forms import NoteCategoryForm

# Create your views here.

def home(request):
    note_obj=Note.objects.all().order_by('id')
    note_category_obj= NoteCategory.objects.all().order_by('id')
    
    data={'notes':note_obj , 'note_categories':note_category_obj}
    return render(request, 'index.html', context=data,)

    


def create_note(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        category_id=request.POST.get('notecategory')
        
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
        else:
            return render(request,'create_note_category',context={'form':form})
     
    note_category_form=NoteCategoryForm()
    data={'notecategory_form':note_category_form}
    return render(request,'create_note_category.html',context=data)

def edit_note(request,pk):
    note_obj=Note.objects.get(id=pk)
    
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        category_id=request.POST.get('notecategory')
        
        note_category_obj=NoteCategory.objects.get(id=category_id)
        
        # Update the existing note
        note_obj.name=name
        note_obj.description=description
        note_obj.notecategory=note_category_obj
        note_obj.save()
        
        #redirect the page to home page
        return redirect('/')
       

        
    
    notecategory_obj=NoteCategory.objects.all()
    content={'notecategory':notecategory_obj,'note':note_obj}
    return render(request,'edit_note.html',context=content)

def edit_note_category(request,pk):
    note_category_obj=NoteCategory.objects.get(id=pk)
    
    if request.method=='POST':
        form=NoteCategoryForm(request.POST, instance=note_category_obj)
        dataa={'notecategory':form}
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'edit_notecategory.html',context=dataa)
    

    note_category_form=NoteCategoryForm(instance=note_category_obj)
    data={'notecategory':note_category_form}
    return render(request,'edit_notecategory.html',context=data)

def delete_note_category(request,pk):
    note_category_obj=NoteCategory.objects.get(id=pk)
    
    if request.method=='POST':
        note_category_obj.delete()
        return redirect('/')

    return render(request,'delete.html')

def delete_note(request,pk):
    note_obj=Note.objects.get(id=pk)
    note_obj.delete()
    return redirect('/')
    
    
    
    
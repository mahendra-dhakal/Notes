from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note, NoteCategory  
from .forms import NoteCategoryForm, UserForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        note_obj=Note.objects.filter(user=request.user).order_by('id')
        note_category_obj= NoteCategory.objects.filter(user=request.user).order_by('id')
        
        data={'notes':note_obj , 'note_categories':note_category_obj}
        return render(request, 'index.html', context=data,)
    else:
        return redirect('start-page')

    

@login_required
def create_note(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        category_id=request.POST.get('notecategory')
        
        note_category_object = NoteCategory.objects.get(id=category_id, user=request.user)   # Ensure category belongs to user
        
        #brings notecategory as a object with help of id given to get method
        
        # name and description can be stored directly as values in the database but notecategory cannot be stored in the database directly as their value because it is relation field . so we have to pass the object to store value 
        
        Note.objects.create(name=name, description= description,notecategory=note_category_object,user=request.user)  # Associate note with user
        return redirect('home')
        
    notecategory_obj=NoteCategory.objects.filter(user=request.user)  # Filter categories by user
    note_category={'notecategory':notecategory_obj}
    return render(request,'create_note.html',context=note_category)


@login_required
def create_note_category(request):
    if request.method=='POST':
        form=NoteCategoryForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False) # doesn't save to the database immediately.
            instance.user=request.user  #modify or change the instance before saving it 
            instance.save()   # now saves the data in database
            return redirect('home')
        else:
            return render(request,'create_note_category',context={'form':form})
     
    note_category_form=NoteCategoryForm()
    data={'notecategory_form':note_category_form}
    return render(request,'create_note_category.html',context=data)


@login_required
def edit_note(request,pk):
    note_obj=Note.objects.get(id=pk, user=request.user)
    
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        category_id=request.POST.get('notecategory')
        
        note_category_obj=NoteCategory.objects.get(id=category_id,user=request.user) #ensures that notecategory belongs to user
        
        # Update the existing note
        note_obj.name=name
        note_obj.description=description
        note_obj.notecategory=note_category_obj
        note_obj.save()
        
        #redirect the page to home page
        return redirect('/')
       

        
    
    notecategory_obj=NoteCategory.objects.filter(user=request.user)
    content={'notecategory':notecategory_obj,'note':note_obj}
    return render(request,'edit_note.html',context=content)

@login_required
def edit_note_category(request,pk):
    note_category_obj=NoteCategory.objects.get(id=pk,user=request.user) 
    
    if request.method=='POST':
        form=NoteCategoryForm(request.POST, instance=note_category_obj)
        #here two positional arguments are required
        #at first : data that is to be added or new data 
        # at second : data that is to be changed or old data
        
        dataa={'notecategory':form}
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'edit_notecategory.html',context=dataa)
    

    note_category_form=NoteCategoryForm(instance=note_category_obj)
    data={'notecategory':note_category_form}
    return render(request,'edit_notecategory.html',context=data)


@login_required
def delete_note_category(request,pk):
    note_category_obj=NoteCategory.objects.get(id=pk,user=request.user)
    
    if request.method=='POST':
        note_category_obj.delete()
        return redirect('/')

    return render(request,'delete.html')

@login_required
def delete_note(request,pk):
    note_obj=Note.objects.get(id=pk,user=request.user)
    note_obj.delete()
    return redirect('/')

def register_user(request):
    
    if request.method == 'POST':
        data=request.POST.copy()
        password=request.POST.get('password')
        hash_password=make_password(password)
        data['password']=hash_password
        form=UserForm(data)
        if form.is_valid():
            form.save()
            return redirect('start-page')
        else:
            return render(request,'register.html',context={'form':form})
    
    form=UserForm()
    data={'form':form}
    return render(request,'register.html',context=data)

def user_login(request):
    form=UserForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user== None:
            return render(request,'login.html',context={'form':form,'error':'Invalid username and password'})
        else:
            login(request,user)
            return redirect('home')
    
    data={'form':form}
    return render(request,'login.html',context=data)
    

def log_out(request):
    logout(request)
    return redirect('start-page')

def start_page(request):
    return render(request,'home.html')
    
       
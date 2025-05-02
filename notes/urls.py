"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import home, create_note, create_note_category, edit_note, edit_note_category,delete_note_category,delete_note, register_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('create-note/', create_note,name='create-note'),
    path('create-note-category/',create_note_category, name='create-note-category'),
    path('edit-note/<int:pk>/',edit_note, name='edit-note'),
    path('edit-note-category/<int:pk>', edit_note_category, name='edit-note-category'),
    path('delete-note-category/<int:pk>', delete_note_category, name='delete-notecategory'),
    path('delete-note/<int:pk>',delete_note,name='delete-note'),
    path('register-user/',register_user,name='register-user')
    
]

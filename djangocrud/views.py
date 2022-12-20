from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import CreateTask,Categories
from django.contrib.auth.models import User 
from .form import FormTask
from django.urls import  reverse
from django.contrib.auth import login, authenticate
from django.contrib  import messages
from django.utils import timezone
from django.http import HttpResponseRedirect
from Users.models import LibraryCategory



class Home(View):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            tasks = CreateTask.objects.filter(user=self.request.user , datecompleted=None)
            
            if len(tasks) == 0:
                status=True
                
                context = {
                'status': status,
                'title' : "Pending"
                }

                return render(request, 'pages/index.html', context)
            
            else: 
                context = {
                    'tasks' : tasks,
                    'title' : "Pending"

                }

                return render(request, 'pages/index.html', context)
        else:
            return render(request, 'pages/index.html')

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

            email = request.POST['email']
            password = request.POST['password']
            try:
                user = authenticate(username=email, password=password)
                login(self.request, user)
                return redirect('home')
            except ValueError:
                messages.warning(self.request, 'Invalid username or password')



        return render(request, 'pages/index.html', {} )

  

@login_required
def ImportantTask(request):
    
    tasks = CreateTask.objects.filter(important=True, datecompleted=None, user=request.user)
    context = {
        'tasks':tasks,
        'title': 'Important'
    }
    return render(request, 'pages/index.html', context)

@login_required
def FinishedTask(request):
    tasks = CreateTask.objects.filter(finished=True, user=request.user)
    context = {
       'tasks':tasks,            
       'title': 'Finished'
    }
    return render(request, 'pages/index.html', context)
    



            
class CreateTaskUser(LoginRequiredMixin, View):
   

    def get(self, request, *args, **kwargs):
        print(self.request.user)
        categories = LibraryCategory.objects.get(user=self.request.user)
        form= FormTask()
        context = {
            'categories': categories,
            'form': form
        }
        return render(request, 'pages/task/create.html',context)
    

    def post(self, request, *args, **kwargs):
            
        if request.method == 'POST':
            form=FormTask(request.POST)
            if form.is_valid():
                form.user=request.user
                title = form.cleaned_data.get('title')
                description = form.cleaned_data.get('description')
                important = form.cleaned_data.get('important')
                categories = Categories.objects.get(name=request.POST['categories'])
                p, create = CreateTask.objects.get_or_create(user=form.user,title=title,description=description, categories=categories, important=important)
                p.save()
                return redirect('home')

        return render(request, 'pages/task/create.html', {})


class DetailTask(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(CreateTask, id=self.kwargs["id"], user=self.request.user)
        return render(request, 'pages/task/detail.html', {'task': task})

    def post(self, request, *args, **kwargs): 
        if request.method=="POST":
            task = get_object_or_404(CreateTask, id=self.kwargs["id"], user=request.user)
            task.datecompleted=timezone.now()
            task.finished=True
            task.save()
            return HttpResponseRedirect(reverse('detail',
                                    args=[task.id]
            ))
        
  

    

class  UpdateTask(LoginRequiredMixin, View):
    
    def get(self, request, pk, *args, **kwargs):
        categories = LibraryCategory.objects.get(user=self.request.user)
        form= CreateTask.objects.get(id=pk)
        print(form.important )
        context = {
            'categories': categories,
            'form': form
        }
        return render(request, 'pages/task/update.html',context)
    
    
    def post(self, request, pk, *args, **kwargs):
        
        form= CreateTask.objects.get(id=pk)
    
        if request.POST['important'] == "on":
            form.important =  "True"
    

        form.title = request.POST['title']
        form.description = request.POST['description']
        
        
        form.categories = Categories.objects.get(name=request.POST['categories'])
        form.save()
        return HttpResponseRedirect(reverse('detail',
                                    args=[form.id]))




@login_required
def DeleteTask(request, id):
        task = get_object_or_404(CreateTask, id=id , user=request.user)
        task.delete()
        return redirect('home')




def CreateCategory(request):
    if request.method == 'POST':
        name = request.POST['name']
        
        try:
            category=Categories.objects.get(name=name)
            library=LibraryCategory.objects.get(user=request.user)
            library.categories.add(category)
        except:
            category= Categories.objects.create(user=request.user, name=name)
            library=LibraryCategory.objects.get(user=request.user)
            library.categories.add(category)
        return redirect('create')
    

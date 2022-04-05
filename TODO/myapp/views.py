from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from myapp.forms import TaskForm
from .models import Task
# Create your views here.
def home(request):
    tasks =Task.objects.all()
    all_task = tasks.count()

    completed = Task.objects.filter(status=True)
    completed_task = completed.count()

    Incompleted = Task.objects.filter(status=False)
    Incompleted_task = Incompleted.count()

    form = TaskForm
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks,'form':form, 'all_task':all_task,'completed':completed_task,'Incompleted':Incompleted_task}  
    return render(request ,'home.html', context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('home')
    context={
        'item':item
    }
    return render(request,'delete.html')

def update_Task(request,pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    
    if request.method=='POST':
        form = TaskForm(request.POST,instance=task)
        form.save()
        return redirect('home')

    context ={
        'form':form
    }

    return render(request, 'update.html', context)
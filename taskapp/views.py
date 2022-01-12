from django.shortcuts import render, redirect
from . models import TaskModel
from . forms import TaskModelForm, TaskUpdateForm

# Create your views here.
def index(request):
    # Create and Save data into the database 
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskModelForm()
    # Querry to fetch data from the database
    task = TaskModel.objects.all().order_by('-date')
    # Querry to calculate objects
    total_task = TaskModel.objects.all().count()
    completed_task = TaskModel.objects.filter(complete=True).count()
    uncompleted_task = total_task - completed_task
    data = [total_task, completed_task, uncompleted_task]
    context = {
        'task': task,
        'form': form,
        'total_task':total_task,
        'completed_task':completed_task,
        'uncompleted_task': uncompleted_task,
        'data':data
    }
    return render(request, 'taskapp/index.html', context)

def about(request):
    return render(request, 'taskapp/about.html')

def delete(request, pk):
    task = TaskModel.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'taskapp/delete.html')
    
def update(request, pk):
    task = TaskModel.objects.get(id=pk)
    if request.method == "POST":
        form = TaskUpdateForm(request.POST ,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskUpdateForm(instance=task)
    context ={
        'form': form
    }

    return render(request, 'taskapp/update.html', context)
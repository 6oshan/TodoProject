from django.shortcuts import render, redirect

from .forms import Todoform
from .models import Task
# Create your views here.
def doc(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('Task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
# def details(request):
#     return render(request,'details.html',)
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    fi=Todoform(request.POST or None, instance=task)
    if fi.is_valid():
        fi.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'fi':fi})
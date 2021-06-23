from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def list(request):
    orders= Order.objects.all()  
    form=OrderForm()
    if request.method=='POST':
        form= OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context={'order':orders,'form':form}

    return render(request,'newapp/list.html',context)

def updatelist(request,pk):
    demand= Order.objects.get(id=pk)
    form= OrderForm(instance=demand)

    if request.method=='POST':
        form=OrderForm(request.POST,instance=demand)
        if request.POST.get('submit')=='Update':
            if form.is_valid():
                form.save()
                return redirect('/')
        elif request.POST.get('submit')=='Cancel':
            if form.is_valid():
                return redirect('/')
    context={'form':form}
    return render(request,'newapp/update.html',context)

def deletelist(request,pk):
    task= Order.objects.get(id=pk)
    #form= OrderForm()

    if request.method=='POST':
        if request.POST.get('submit')=='Yes,Delete':
            task.delete()
            return redirect('/')
        else:
            return redirect('/')
    context={'task':task}
    return render(request,'newapp/delete.html',context)

def contact(request):
    form1= ContactForm()

    if request.method=='POST':
        form1= ContactForm(request.POST)

        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request, 'newapp/contact.html', context={'form1': form1})
   
        
def about(request):
    return render(request,'newapp/about.html')



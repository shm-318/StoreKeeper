from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.



def register(request):
    
    registered=False

    if(request.method=='POST'):
        user_form= UserForm(data=request.POST)
        profile_form= UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)

            profile.user=user #One to one relationship indicator(Will research into it in some moments)

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form =UserProfileInfoForm()

    return render(request,'newapp/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
        
def user_login(request):

    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']# gets the username and password from the form supplied
        
        
        user=authenticate(request,username=username,password=password) #authenticates the user in a single line of code, Hail Django!
        print("user:",user)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('list') #if user has logged in successfully, he/she would be redirected to the index page  
            else:
                return HttpResponse("User not active")
        else:
            print("Someone tried to login who was not registered")
            print("username: {}, password: {}".format(username,password))
            return HttpResponse("Invalid Login details Supplied")
            #if a user who was not registered tries to login, then this happens
    else:
        return render(request,'newapp/index.html',{})

@login_required   #a decorator which ensures this fn gets executed iff the user has logged in
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required   
def list(request):
    orders= Order.objects.all()  
    form=OrderForm()
    if request.method=='POST':
        form= OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('newapp:list')
    
    context={'order':orders,'form':form}

    return render(request,'newapp/list.html',context)

@login_required
def updatelist(request,pk):
    demand= Order.objects.get(id=pk)
    form= OrderForm(instance=demand)

    if request.method=='POST':
        form=OrderForm(request.POST,instance=demand)
        if request.POST.get('submit')=='Update':
            if form.is_valid():
                form.save()
                return redirect('newapp:list')
        elif request.POST.get('submit')=='Cancel':
            if form.is_valid():
               return redirect('newapp:list')
    context={'form':form}
    return render(request,'newapp/update.html',context)

@login_required
def deletelist(request,pk):
    task= Order.objects.get(id=pk)
    #form= OrderForm()

    if request.method=='POST':
        if request.POST.get('submit')=='Yes,Delete':
            task.delete()
            return redirect('newapp:list')
        else:
            return redirect('newapp:list')
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



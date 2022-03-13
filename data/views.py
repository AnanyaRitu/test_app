
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from .decorators import *
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.http import JsonResponse
import requests

# Create your views here.


def parent_registration(request):
    if request.method == "POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='Parent')
            user.groups.add(group)
            Parent.objects.create(user=user)
            return redirect('log_in')
            messages.success(request, "Registration successful." )
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form=NewUserForm()
    context={"form":form}

    return render(request, "parent_registration.html", context)



def child_registration(request):
    
    if request.method == "POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            user=form.save()
            parent_username=request.POST.get('dropdown')
            selected_parent=Parent.objects.get(user__username=parent_username)
            group = Group.objects.get(name='Child')
            user.groups.add(group)
            Child.objects.create(user=user, parent=selected_parent)
            return redirect('log_in')

    form=NewUserForm()
    parents=Parent.objects.all()
    context={"form":form, "parents":parents}

    return render(request, "child_registration.html", context)


@unauthenticated_user
def log_in(request):
    form = Log_in_form()

    if request.method == 'POST':
        #form = Log_in_form(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('logged in')
            login(request, user)
            group = request.user.groups.all()[0].name

            if group == 'Parent':
                return redirect('parent_home')

            elif group == 'Child':
                print("in child")
                return redirect('child_home')
    context = {'form': form}
    return render(request, 'login.html', context)
        


@login_required(login_url='log_in')
def log_out(request):
    logout(request)
    return redirect('log_in')






@login_required(login_url='log_in')
@allowed_users(allowed_roles=['Parent'])
def parent_home(request):
    parent=Parent.objects.get(user=request.user)
    if request.method=="POST":
        api_path="http://127.0.0.1:8000/parent_data_delete/"+request.user.username
        requests.delete(api_path)
        return redirect("parent_home")
    return render(request, "parent_home.html", {"parent":parent})




@login_required(login_url='log_in')
@allowed_users(allowed_roles=['Parent'])
def parent_create_data_view(request):
    if request.method == 'POST':
        form = ParentDataCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            api_url="http://127.0.0.1:8000/parent_data_create/"+request.user.username
            requests.post(api_url, data=form.cleaned_data)
            return redirect('parent_home')
    else:
        form = ParentDataCreationForm()
    return render(request, "parent_create_data.html", {"form":form})





@login_required(login_url='log_in')
@allowed_users(allowed_roles=['Parent'])
def parent_update_data_view(request):
    print('yoo')
    if request.method == 'POST':
        form = ParentDataCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            api_url="http://127.0.0.1:8000/parent_data_update/"+request.user.username
            requests.post(api_url, data=form.cleaned_data)
            return redirect('parent_home')
    else:
        form = ParentDataCreationForm()
    return render(request, "parent_update_data.html", {"form":form})




@login_required(login_url='log_in')
@allowed_users(allowed_roles=['Child'])
def child_home(request):
    child=Child.objects.get(user=request.user)
    if request.method=="POST":
        api_path="http://127.0.0.1:8000/child_data_delete/"+request.user.username
        requests.delete(api_path)
        return redirect("child_home")
    return render(request, "child_home.html",{"child":child})




@login_required(login_url='log_in')
@allowed_users(allowed_roles=['Child'])
def child_create_data_view(request):
    if request.method == 'POST':
        form = ChildDataCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            api_url="http://127.0.0.1:8000/child_data_create/"+request.user.username
            requests.post(api_url, data=form.cleaned_data)
            return redirect('child_home')
    else:
        form = ChildDataCreationForm()
    return render(request, "child_create_data.html", {"form":form})





@login_required(login_url='log_in')
@allowed_users(allowed_roles=['Child'])
def child_update_data_view(request):
    print('yoo')
    if request.method == 'POST':
        form = ChildDataCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            api_url="http://127.0.0.1:8000/child_data_update/"+request.user.username
            requests.post(api_url, data=form.cleaned_data)
            return redirect('child_home')
    else:
        form = ChildDataCreationForm()
    return render(request, "child_update_data.html", {"form":form})





"""
Parent Api functions

"""
@api_view(['GET'])
def parent_username_list(request):
    parent_list=Parent.objects.all()
    parents={}
    for parent in parent_list:
        parents[parent.id]=parent.user.username
    return Response(parents)



@api_view(['POST'])
def parent_data_create(request, parent):
    serializer = ParentSerializer(data=request.data)
    if serializer.is_valid():
        parent=Parent.objects.get(user__username=parent)
        if not parent.firstName and not parent.lastName and not parent.street and not parent.city and not parent.state and not parent.zip:
            parent.firstName=serializer.data['firstName']
            parent.lastName=serializer.data['lastName']
            parent.street=serializer.data['street']
            parent.city=serializer.data['city']
            parent.state=serializer.data['state']
            parent.zip=serializer.data['zip']
            parent.save()
            print(parent.firstName)
        else:
            return Response("data already exists. Try updating the data")
    return Response(serializer.data)



@api_view(['POST'])
def parent_data_update(request, parent):
    serializer = ParentSerializer(data=request.data)
    if serializer.is_valid():
        parent=Parent.objects.get(user__username=parent)
        parent.firstName=serializer.data['firstName']
        parent.lastName=serializer.data['lastName']
        parent.street=serializer.data['street']
        parent.city=serializer.data['city']
        parent.state=serializer.data['state']
        parent.zip=serializer.data['zip']
        parent.save()
        print(parent.firstName)
    return Response(serializer.data)


@api_view(['DELETE'])
def parent_data_delete(request, parent):
    parent=Parent.objects.get(user__username=parent)
    if not parent.firstName and not parent.lastName and not parent.street and not parent.city and not parent.state and not parent.zip:
        return Response("data does not exist")
        
    else:
        parent.firstName=None
        parent.lastName=None
        parent.street=None
        parent.city=None
        parent.state=None
        parent.zip=None
        parent.save()
        print(parent.firstName)
        return Response("data successfully deleted")



"""
Child Api functions

"""
@api_view(['GET'])
def child_username_list(request):
    child_list=Child.objects.all()
    children={}
    for child in child_list:
        children[child.id]=child.user.username
    return Response(children)


@api_view(['POST'])
def child_data_create(request, child):
    serializer = ChildSerializer(data=request.data)
    if serializer.is_valid():
        child=Child.objects.get(user__username=child)
        if not child.firstName and not child.lastName:
            child.firstName=serializer.data['firstName']
            child.lastName=serializer.data['lastName']
            child.save()
            print(child.firstName)
        else:
            return Response("data already exists. Try updating the data")
    return Response(serializer.data)



@api_view(['POST'])
def child_data_update(request, child):
    serializer = ChildSerializer(data=request.data)
    if serializer.is_valid():
        child=Child.objects.get(user__username=child)
        child.firstName=serializer.data['firstName']
        child.lastName=serializer.data['lastName']
        child.save()
        print(child.firstName)
    return Response(serializer.data)


@api_view(['DELETE'])
def child_data_delete(request, child):
    child=Child.objects.get(user__username=child)
    if not child.firstName and not child.lastName:
        return Response("data does not exist")       
    else:
        child.firstName=None
        child.lastName=None
        child.save()
        print(child.firstName)
        return Response("data successfully deleted")

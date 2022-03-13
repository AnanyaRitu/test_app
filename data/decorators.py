from django.http import HttpResponse
from django.shortcuts import redirect, render

#if loggedin, cannot view the login page.
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'Parent':
                    return redirect('parent_home')

                elif group == 'Child':
                    print("in child")
                    return redirect('child_home')
            else:
                return HttpResponse("You are not authorized to any group")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


#only allowed users can access a specific page
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorized to view this page')
        return wrapper_func
    return decorator
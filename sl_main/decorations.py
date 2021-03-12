from django.http import HttpResponse
from django.shortcuts import redirect


def unauthentification_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('base')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Доступ запрещен')

        return wrapper_func

    return decorator


def edit_contractor(view_func):
    def wrapper_func(request, *args, **kwargs):

        print(all_item)
        # if request.item in all_item:
        #     print ("ok")
        #
        # else:
        #     return HttpResponse('Доступ запрещен')

    return wrapper_func


def contractor_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'contractor':
            return redirect('user-page')
        else:
            return view_func(request, *args, **kwargs)

        # if group == 'admin':
        #     return view_func(request, *args, **kwargs)

    return wrapper_func

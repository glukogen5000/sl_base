from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ItemForm
from .decorations import unauthentification_user, allowed_users, contractor_only, edit_contractor


# from .forms import UserForm
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import ShcoolSerialezer

# def list_school(request):
#     list_school = School.objects.all()
#     list_statusAddres = StatusAddres.objects.all()
#     list_statusID = StatusID.objects.all()
#     list_statusKD = StatusKD.objects.all()
#     color = {"green": 'class="bg-success">',
#              "yellow": 'class="bg-warning">',
#              "red": 'class="bg-danger">',
#              "blue": 'class="bg-info"}>'}
#
#     return render(request, 'sl_main/list_school.html', {'title': "main",
#                                                'list_school': list_school,
#                                                'list_statusKD': list_statusKD,
#                                                'color': color

@unauthentification_user
def loginPage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('base')

    context = {}
    return render(request, 'sl_main/login.html', context)


@login_required(login_url='login')
def logout_User(request):
    logout(request)
    return redirect('login')


#
#
#           })
# @admin_only
@contractor_only
@login_required(login_url='login')
def index(request):
    return render(request, 'sl_main/base.html', {'page_name': "Главная"})


@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def contractor(request, pk):
    contractor = Contractor.objects.get(id=pk)
    list_item = contractor.itemproject_set.all()

    page_name = 'Подрядчик'

    context = {'contractor': contractor, 'list_item': list_item}
    return render(request, 'sl_main/contractor.html', context)


@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def object(request, pk):
    object = ItemProject.objects.get(id=pk)

    page_name = 'Объект'
    context = {'object': object}
    return render(request, 'sl_main/object.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def contractor_list(request):
    # page_name = 'Список подрядчиков'
    contractor_list = Contractor.objects.all()
    context = {'page_name': "Список подрядчиков", 'contractor_list': contractor_list}
    return render(request, 'sl_main/contractor_list.html', context)


@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def list_object(request):
    page_name = "Список объектов"
    item_project = ItemProject.objects.all()
    return render(request, 'sl_main/list_object.html', {'page_name': "Список объектов",
                                                        'item_project': item_project})


@login_required(login_url='login')
@allowed_users(allowed_roles=['contractor'])
def userPage(request):
    all_item = request.user.contractor.itemproject_set.all()

    context = {'all_item': all_item}
    return render(request, 'sl_main/user.html', context)

@login_required(login_url='login')
# @edit_contractor
def updateItem(request, pk):
    item = ItemProject.objects.get(id=pk)
    form = ItemForm(instance=item)
    all_item = request.user.contractor.itemproject_set.all()
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')



    context = {'form': form}
    return render(request, 'sl_main/update_item.html', context)


@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.location = 'media'
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        print(url)
    return render(request, 'sl_main/upload.html')

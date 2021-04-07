from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import *
from .forms import *
from .decorations import unauthentification_user, allowed_users, contractor_only, edit_contractor
from .filters import ItemFilter


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
    # .id.contractor.itemproject_set.all()
    print(list_item)

    page_name = 'Подрядчик'

    context = {'contractor': contractor, 'list_item': list_item}
    return render(request, 'sl_main/contractor.html', context)


@allowed_users(allowed_roles=['admin', 'contractor'])
@login_required(login_url='login')
def object(request, pk):
    object1 = ItemProject.objects.get(id=pk)
    comment = Comment.objects.filter(item_p=pk).order_by('-date_create')
    files = object1.document_set.all()
    my_form = CommentForm()
    form_doc = DocumentForm()
    # print (request.POST)
    if request.method == 'POST' and 'formOne' in request.POST.values():
        my_form = CommentForm(request.POST)
        if my_form.is_valid():
            obj = my_form.save(commit=False)
            obj.author = request.user
            obj.item_p = object1
            obj.save()
            return HttpResponseRedirect('/object/' + pk)

    if request.method == 'POST' and 'formTwo' in request.POST.values():
        form_doc = DocumentForm(request.POST, request.FILES)
        if form_doc.is_valid():
            obj = form_doc.save(commit=False)
            obj.user_upload = request.user
            obj.item_proj = object1
            obj.save()
        return HttpResponseRedirect('/object/' + pk)

    #     my_form = CommentForm()
    #     form_doc = DocumentForm()
    # page_name = 'Объект'
    capacity = MaterialforItem.objects.filter(item_m=pk)
    context = {'object': object1, 'comment': comment, 'form': my_form, 'form_doc': form_doc, 'files': files,
               'capacity': capacity}
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

    myFilter = ItemFilter(request.GET, queryset=item_project)
    item_project = myFilter.qs

    return render(request, 'sl_main/list_object.html', {'page_name': "Список объектов",
                                                        'item_project': item_project, 'myFilter': myFilter})


@login_required(login_url='login')
@allowed_users(allowed_roles=['contractor'])
def userPage(request):
    all_item = request.user.contractor.itemproject_set.all()

    context = {'all_item': all_item}
    return render(request, 'sl_main/user.html', context)


#
@login_required(login_url='login')
# @edit_contractor
def updateItem(request, pk):
    item = ItemProject.objects.get(id=pk)
    form = ItemForm(instance=item)
    comment = Comment.objects.filter(item_p=pk)
    form_com = CommentForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'comment': comment, 'form_com': form_com}
    return render(request, 'sl_main/update_item.html', context)


@login_required(login_url='login')
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = DocumentForm()
    return render(request, {
        'form': form
    })

# @login_required(login_url='login')
# def model_form_upload(View):
#     def get(self, request):
#         document_list = Document.objects.all()
#         return render(self.request, 'sl_main/model_form_upload.html', {'documents': document_list})
#
#     def post(self, request):
#         form = DocumentForm(self.request.POST, self.request.FILES)
#         if form.is_valid():
#             document = form.save()
#             data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)

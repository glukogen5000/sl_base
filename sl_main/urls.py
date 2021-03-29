from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views

#app_name = 'base'
urlpatterns = [
    path('', views.index, name='base'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logout_User, name='logout'),
    path('list_object/', views.list_object, name='list_object'),
    path('contractor_list/', views.contractor_list, name='contractor_list'),
    path('contractor/<str:pk>/', views.contractor, name='contractor'),
    path('object/<str:pk>/', views.object, name='object'),
    path('user/', views.userPage, name='user-page'),
    # path('upload/',views.model_form_upload, name='upload'),
    path('update_item/<str:pk>/', views.updateItem, name='update_item'),
    # path('list_school/', views.list_school, name='list_school'),
    # path('school_<int:pk>/', views.list_school, name='list_school'),
    # path('contractor/', views.contractor, name='contractor'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

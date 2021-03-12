from django.contrib import admin
from django.urls import path, include

from sl_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sl_main.urls'))

]
import debug_toolbar
from django.contrib import admin
from django.urls import path, include


from sl_main import views

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', include('sl_main.urls'))


]
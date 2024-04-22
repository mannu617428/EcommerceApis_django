from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/' , views.Master , name='master'),
    path('' , views.Index , name='index'),
]

"""
URL configuration for taskmore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import load_data
from .views import completed
from .views import Overdue
from .views import delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('getprofile/', views.getprofile, name='getprofile'),
    path('load-data/', load_data, name='load_data'),
    path('completed/', completed, name='completed'),
    path('Overdue/', Overdue, name='Overdue'),
    path('delete/', delete, name='delete'),
    path('delete/delete/<int:id>', views.deleted, name='deleted'),
    path('delete/<int:id>', views.deleted, name='deleted'),
    path('login/', views.user, name='log'),
    path('login/new/', views.new, name='newacc'),
    path('create/', views.new, name='create'),

]

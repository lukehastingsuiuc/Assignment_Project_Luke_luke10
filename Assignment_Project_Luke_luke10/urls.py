"""
URL configuration for Assignment_Project_Luke_luke10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from Study_Buddy.views import (user_list_view, user_list_render, UserDetail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("userlist/", user_list_view),
    path("users/", user_list_render),

    path('user/<int:primary_key>/',
        UserDetail.as_view(),
        name='user_detail-url'),

]

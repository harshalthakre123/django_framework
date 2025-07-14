"""
URL configuration for project project.

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
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("alldata/", views.alldata, name="alldata"),
    path("myfilter/", views.myfilter, name="myfilter"),
    path("myorder/", views.myorder, name="myorder"),
    path("myreverse/", views.myreverse, name="myreverse"),
    path("myvalue/", views.myvalue, name="myvalue"),
    path("myvaluelist/", views.myvaluelist, name="myvaluelist"),
    path("myslice/", views.myslice, name="myslice"),
    path("singledata/", views.singledata, name="singledata"),
]

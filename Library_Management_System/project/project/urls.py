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
    path("",views.manage, name="manage"),

    path("book/",views.book, name="book"),
    path("addbook/",views.addbook, name="addbook"),
    
    path("branch/",views.branch, name="branch"),
    path("addbranch/",views.addbranch, name="addbranch"),

    path("library/",views.library, name="library"),
    path("addlib_id/",views.addlib_id, name="addlibid"),

    path("student/",views.student, name="student"),
    path("studata/",views.studata, name="studata"),

    path("issue/",views.issue, name="issue"),
    path("book_issued/",views.book_issued, name="bookissued"),


# Data Accessing
    path("data/", views.data, name="data"),

    
]

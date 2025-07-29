"""
URL configuration for myntra project.

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

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepg, name="homepg"),
    path("men/",views.men, name='men'),
    path("women/",views.women, name='women'),
    path("kids/",views.kids, name='kids'),
    path("home/",views.home, name='home'),
    path("beauty/",views.beauty, name='beauty'),
    path("genz/",views.genz, name='genz'),
    path("studio/",views.studio, name='studio'),
    path("wishlist/",views.wishlist, name='wishlist'),
    path("bag/",views.bag, name='bag'),

    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("logout/", views.logout, name="logout")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


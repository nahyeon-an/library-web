"""libraries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.decorators.csrf import csrf_exempt
from libraries.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', csrf_exempt(UserCreateView.as_view()), name='register'),
    path('accounts/register/done/', csrf_exempt(UserCreateDoneView.as_view()), name='register_done'),
    # main dashboard
    path('', HomeView.as_view(), name='home'),
    path('all/', DataView.as_view(), name='all'),
    path('si/', SiDataView.as_view(), name='si'),
    path('gun/', GunDataView.as_view(), name='gun'),
    # apps
    path('dashboard/', include('dashboard.urls')),
    path('search/', include('search.urls')),
]

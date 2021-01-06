from django.urls import path, re_path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
from django.urls import path
from . import views

app_name = 'api_library'
urlpatterns = [
    path('', views.LibraryView.as_view()),
    path('<str:si>', views.LibraryView.as_view(), name='si'),
]
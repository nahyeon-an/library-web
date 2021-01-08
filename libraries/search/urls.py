from django.urls import path, re_path
from search import views

app_name = 'search'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('all/', views.AllLibraryListView.as_view(), name='all'),
    path('list/<str:name>', views.LibraryListView.as_view(), name='list'),
    path('detail/', views.DetailView.as_view(), name='detail_view'),
    path('detail/<str:name>', views.LibraryDetailView.as_view(), name='detail'),
]
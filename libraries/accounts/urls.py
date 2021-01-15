from django.urls import path, re_path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/request', views.RegisterRequestView.as_view(), name='registration'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('login/request', views.LoginRequestView.as_view(), name='login_request'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change/', views.PasswordChangeView.as_view(), name='change'),
    path('recover/', views.PasswordRecoverView.as_view(), name='recover'),
]

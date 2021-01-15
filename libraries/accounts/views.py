import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings

class RegisterView(TemplateView):
    template_name = 'accounts/register.html'

class RegisterRequestView(View):
    def post(self, request):
        if request.method == "POST":
            if request.POST["password"] == request.POST["repeat-password"]:
                user = User.objects.create_user(username=request.POST["username"],\
                                                password=request.POST["password"],\
                                                email=request.POST["email"])
                return render(request, 'accounts/register_done.html')

            return render(request, 'accounts/register.html')

class LoginView(TemplateView):
    template_name = 'accounts/login.html'

class LoginRequestView(View):
    def post(self, request):
        if request.method == "POST":
            user = User.objects.get_by_natural_key(request.POST["username"])
            if user.check_password(request.POST['password']):
                auth.login(request, user)
                request.session['username'] = user.username
                request.session['is_active'] = user.is_active
                remember = request.POST.get('auto', False)

                if remember=='on':
                    request.session['remember'] = True
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                else:
                    request.session['remember'] = False
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                    request.session.set_expiry(1800)
                return render(request, 'home.html')

            return render(request, 'accounts/login.html')

class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        request.session.clear()
        return redirect('/')

# 아래는 폼 요소 처리 필요
class PasswordChangeView(TemplateView):
    template_name = 'accounts/password_change.html'

class PasswordRecoverView(TemplateView):
    template_name = 'accounts/password_recovery.html'
from django.shortcuts import render, HttpResponseRedirect

from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin

# IMPORTAMOS EL FORM VIEW DESDE AQUÍ
from django.views.generic.edit import FormView

from django.views.generic import View, TemplateView

# IMPORTAMOS EL MODELO CON EL QUE
# TRABAJAREMOS
from .models import User

# IMPORTAMOS EL FORMULARIO
from .forms import UserRegisterForm,LoginForm

# IMPORTAMOS PARA LOS MENSAJES
from django.contrib import messages

# Create your views here.
class UserRegisterView(FormView):
    template_name = 'users/userRegister.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('registerUser') # ACA LE DIGO A DONDE RETORNAR
    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            genero=form.cleaned_data['genero']
        )
        messages.add_message(request=self.request, level=messages.SUCCESS, message="Registro exitoso")

        return super(UserRegisterView, self).form_valid(form)

class UserLogin(FormView):
    template_name="users/userLogin.html"
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(UserLogin,self).form_valid(form)


class UserLogout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('loginUser')
        )

class UserDashboard(LoginRequiredMixin,TemplateView):
    model = User
    template_name= "users/userDashboard.html"
    login_url = "loginUser"
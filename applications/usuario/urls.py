from django.urls import path

from .views import UserRegisterView,UserLogin,UserLogout,UserDashboard

urlpatterns = [
    path('users/register/', UserRegisterView.as_view(), name='registerUser'),
    path('users/login/', UserLogin.as_view(), name='loginUser'),
    path('users/logout/', UserLogout.as_view(), name='logoutUser'),
    path('users/dashboard/', UserDashboard.as_view(), name='dashboardUser'),
]

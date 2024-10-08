from django.urls import path
from . import views

urlpatterns = [
    
    #path("main/",views.main,name="main"),
    path("register/",views.register,name="register"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path("login/",views.login,name="login"),
    path("",views.main,name="main"),

]

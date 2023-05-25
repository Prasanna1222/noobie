from django.contrib import admin
from django.urls import path
from CHEEMS import views
urlpatterns = [
    path('',views.front,name="FRONT"),
    path('login/',views.login,name="Login"),
    path('Register/',views.register,name="registration"),
    path('Register/registerAction',views.registerAction,name="registerAction"),
    path('Login/login_logic',views.login_logic,name="login_logic"),
    path('Allcustomer/',views.allcustomer,name="AllCustomer"),
    path('Allcustomer/modifyAction',views.modifyAction,name="modifyAction"),
    path('Allcustomer/customerEditAction',views.customerEditAction,name='customerEditAction'),
    path('CustomerHome/',views.BuyDogs,name="BuyDogs"),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.account_signup, name="account_signup"),
    path('dashboard/', views.account_dashboard, name="account_dashboard"),
    path('login/', views.account_login, name="account_login"),
    path('logout/', views.account_logout, name="account_logout"),
]

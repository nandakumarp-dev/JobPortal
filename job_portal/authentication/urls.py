from django.urls import path

from . import views

urlpatterns = [

    path('login/',views.LoginView.as_view(),name='login_page'),

    path('register/',views.RegisterUserView.as_view(),name='register_user_page'),
    
]
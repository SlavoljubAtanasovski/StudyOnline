from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup, name='sign-up'),
    path('signin/', views.signin, name='sign-in'),
    path('signout/', views.signout, name='sign-out'),
    path('auth/', views.authorize, name='authorize'),
    # path('resetpass/', views.reset_password, name='reset-pass'),
]

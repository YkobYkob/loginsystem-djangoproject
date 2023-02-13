from django.urls import include, path
from . import views

#The URL patterns for this specific app ("mainapp")
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]

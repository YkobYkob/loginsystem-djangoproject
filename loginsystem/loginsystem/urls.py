
from django.contrib import admin
from django.urls import include, path

#The URL patterns for the whole project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
]

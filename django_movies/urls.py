from django.contrib import admin
from django.urls import path
from core.views import hello_world, movies


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('home/', movies, name='movies'),
]

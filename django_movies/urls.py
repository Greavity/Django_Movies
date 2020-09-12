from django.contrib import admin
from django.urls import path
from core.views import hello_world, MovieView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('', MovieView.as_view(), name='index'),
]

from django.contrib import admin
from core.models import Movie, Genre, Director, Country
from accounts.models import Profile

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Country)
admin.site.register(Profile)

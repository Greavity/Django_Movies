from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils import Choices

AGE_LIMITS = Choices(
        (0, 'kids', 'kids'),
        (1, 'teens', 'teens'),
        (2, 'adults', 'adults'),
)


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(choices=AGE_LIMITS, null=True, blank=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    released = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
    countries = models.ManyToManyField(Country, related_name='movies')

    class Meta:
        unique_together = ('title', 'released', 'director')

    def __str__(self):
        return f"{self.title} from {self.released}"



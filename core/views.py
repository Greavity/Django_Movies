from django.shortcuts import render
from core.models import Movie, AGE_LIMITS
from django import views
from django.views.generic import TemplateView


def hello_world(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beatuiful', 'cruel', 'wonderful']},
    )


class MovieView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all(),
                     'limits': AGE_LIMITS
                     }
    # MovieView(views.View) <----- class tak bylo wczesniej
    # def get(self, request):
    #     return render(
    #         request,
    #         template_name='movies.html',
    #         context={'movies': Movie.objects.all(),
    #                  'limits': AGE_LIMITS
    #         },
    #     )

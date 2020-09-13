from django.shortcuts import render
from core.models import Movie, AGE_LIMITS
from django import views
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from core.forms import MovieForm
import logging


def hello_world(request):
    LOGGER.info('Cos smiesznego, hello')
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beatuiful', 'cruel', 'wonderful']},
    )


class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['limits'] = AGE_LIMITS
        return context

    # PO REFAKTORZE MOVIEVIEW JEST NIE UZYWANY
    # MovieView(TemplateView)
    # template_name = 'movies.html'
    # extra_context = {'movies': Movie.objects.all(),
    #                  'limits': AGE_LIMITS
    #                 }
    # MovieView(views.View) <----- class tak bylo wczesniej
    # def get(self, request):
    #     return render(
    #         request,
    #         template_name='movies.html',
    #         context={'movies': Movie.objects.all(),
    #                  'limits': AGE_LIMITS
    #         },
    #     )


logging.basicConfig(
    filename='log.txt',
    filemode='w',
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)


class MovieCreateView(CreateView):
    title = 'Add Movie'              # <-- nie potrzebne raczej, pojawia sie w logerze
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        LOGGER.info(f"Successfully added new movie: {self.request.POST.get('title')}")
        return super().post(request, *args, **kwargs)


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieDeleteView(DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('core:movie_list')


class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movie


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie


class IndexView(MovieListView):
    template_name = 'index.html'

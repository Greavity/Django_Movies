from django.shortcuts import render
from core.models import Movie, AGE_LIMITS
from django import views
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from core.forms import MovieForm
import logging
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin



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


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class MovieCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
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


class MovieUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    def test_func(self):
        return super().test_func() and self.request.user.is_superuser

    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('core:movie_list')


class MovieListView(ListView):   # <- zadanie domowe, user widzi tylko filmy dodane przez siebie (zrobic to w widoku, scope persmision)
    template_name = 'movie_list.html'
    model = Movie


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie


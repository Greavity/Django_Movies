from django.shortcuts import render


def hello_world(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beatuiful', 'cruel', 'wonderful']},
    )


def movies(request):
    return render(
        request,
        template_name='movies.html'
    )
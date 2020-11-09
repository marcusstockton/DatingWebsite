from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'home/index.html', context)


def about(request):
    context = {}
    return render(request, 'home/about.html', context)

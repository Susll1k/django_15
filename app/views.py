from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная страница',
        'items': ['Элемент 1', 'Элемент 2', 'Элемент 3']
    }
    return render(request, 'index.html', context)


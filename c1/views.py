from django.shortcuts import render


def general_page(request):
    return render(request, 'c1/general.html')


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'c1/index.html', context=context_dict)

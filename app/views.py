from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'app/index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'app/login.html')
    elif request.method == 'POST':
        context = {
            'errors': []
        }
        if request.POST.get('email', '') == '':
            context['errors'].append('Внесете email адреса')
        if request.POST.get('password', '') == '':
            context['errors'].append('Внесете лозинка')

        if len(context['errors']) > 0:
            return render(request, 'app/login.html', context)

        user = authenticate(username=request.POST['email'],
                            password=request.POST['password'])
        if user is None:
            context['errors'].append('Внесовте погрешен email и/или лозинка.')
            return render(request, 'app/login.html', context)

        return redirect('index')

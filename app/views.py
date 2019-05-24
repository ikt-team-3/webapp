from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Predmet, Tema, Poraka, Korisnik


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

        user = authenticate(request, username=request.POST['email'],
                            password=request.POST['password'])
        if user is None:
            context['errors'].append('Внесовте погрешен email и/или лозинка.')
            return render(request, 'app/login.html', context)

        auth_login(request, user)
        return redirect('index')


def register(request):
    if request.method == 'GET':
        return render(request, 'app/register.html')
    elif request.method == 'POST':
        context = {
            'errors': []
        }
        if request.POST.get('email', '') == '':
            context['errors'].append('Внесете email адреса')
        if request.POST.get('password', '') == '':
            context['errors'].append('Внесете лозинка')
        if request.POST.get('confirmpassword', '') == '':
            context['errors'].append('Внесете ја лозинката повторно')
        if request.POST.get('confirmpassword', '') != request.POST.get('password', ''):
            context['errors'].append('Лозинките не се совпаѓаат')
        if len(request.POST.get('password', '.......')) < 6:
            context['errors'].append('Лозинката треба да има повеќе од 6 карактери')

        if len(context['errors']) > 0:
            return render(request, 'app/register.html', context)

        if User.objects.filter(email=request.POST.get('email')).exists():
            context['errors'].append('Веќе постои корисник со дадената email адреса')
            return render(request, 'app/register.html', context)

        new_user = User.objects.create_user(request.POST.get('email'), request.POST.get('email'), request.POST.get('password'))
        new_korisnik = Korisnik(user=new_user)
        new_korisnik.save()
        return render(request, 'app/successful_register.html')


def forum_homepage(request):
    context = {
        'predmeti': Predmet.objects.all()
    }
    return render(request, 'app/forum_homepage.html', context)


def forum_predmet(request, predmet):
    predmet_object = get_object_or_404(Predmet, naslov_id=predmet)
    context = {
        'predmet': predmet_object
    }
    return render(request, 'app/forum_predmet.html', context)


def forum_tema(request, predmet, tema):
    tema_object = get_object_or_404(Tema, id=tema)
    if tema_object.predmet.naslov_id != predmet:
        raise Http404
    context = {
        'tema': tema_object
    }
    if request.method == 'GET':
        return render(request, 'app/forum_tema.html', context)
    elif request.method =='POST':
        if request.user.is_authenticated:
            if len(request.POST.get('poraka', '')) == 0:
                context['errors'] = ['Внесете порака']
                return render(request, 'app/forum_tema.html', context)
            nova_poraka = Poraka(avtor=request.user.korisnik,
                                 tekst=request.POST.get('poraka'),
                                 tema=tema_object)
            nova_poraka.save()
            return render(request, 'app/forum_tema.html', context)


@login_required
def forum_nova_tema(request, predmet):
    predmet_object = get_object_or_404(Predmet, naslov_id=predmet)
    context = {
        'predmet': predmet_object,
        'errors': []
    }
    if request.method == 'GET':
        return render(request, 'app/forum_nova_tema.html', context)
    elif request.method == 'POST':
        if len(request.POST.get('poraka', '')) == 0:
            context['errors'].append('Внесете порака')
        if len(request.POST.get('naslov', '')) == 0:
            context['errors'].append('Внесете тема')
        if context['errors']:
            return render(request, 'app/forum_nova_tema.html', context)

        nova_tema = Tema(avtor=request.user.korisnik,
                         predmet=predmet_object,
                         naslov=request.POST.get('naslov'))
        nova_tema.save()
        nova_poraka = Poraka(avtor=request.user.korisnik,
                             tema=nova_tema,
                             tekst=request.POST.get('poraka'))
        nova_poraka.save()
        return redirect('forum_tema', predmet=predmet_object.naslov_id, tema=nova_tema.id)


@csrf_exempt
def api_register(request):
    if request.method == 'POST':
        context = {
            'errors': []
        }
        if request.POST.get('email', '') == '':
            context['errors'].append('Внесете email адреса')
        if request.POST.get('password', '') == '':
            context['errors'].append('Внесете лозинка')
        if request.POST.get('confirmpassword', '') == '':
            context['errors'].append('Внесете ја лозинката повторно')
        if request.POST.get('confirmpassword', '') != request.POST.get('password', ''):
            context['errors'].append('Лозинките не се совпаѓаат')
        if len(request.POST.get('password', '.......')) < 6:
            context['errors'].append('Лозинката треба да има повеќе од 6 карактери')

        if len(context['errors']) > 0:
            return JsonResponse(context)

        if User.objects.filter(email=request.POST.get('email')).exists():
            context['errors'].append('Веќе постои корисник со дадената email адреса')
            return JsonResponse(context)

        new_user = User.objects.create_user(request.POST.get('email'), request.POST.get('email'), request.POST.get('password'))
        new_korisnik = Korisnik(user=new_user)
        new_korisnik.save()
        return JsonResponse({'status': 'OK'})

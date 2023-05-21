# from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserRegistrationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet(request):
    if request.method == "GET":  # Получить страницу с формой
        form = SnippetForm()
        context = {'form': form,
                   'pagename': 'Добавление нового сниппета'}
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":  # Получить данные от формы
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
        return redirect('snippets-list')


# # Получаем данные формы --> Создаем сниппет
# def snippet_create(request):
#     if request.method == "POST":
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             snippet = form.save(commit=False)
#             snippet.user = request.user
#             snippet.save()
#         return redirect('snippets-list')


def snippet_delete(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.delete()
    return redirect('snippets-list')


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов',
               'snippets': snippets}
    return render(request, 'pages/view_snippets.html', context)


@login_required
def snippets_my(request):
    my_snippets = Snippet.objects.filter(user=request.user)
    context = {'pagename': 'Мои сниппеты',
               'snippets': my_snippets}
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    context = {
        'pagename': 'Информация о сниппете',
        'snippet': snippet,
    }
    return render(request, 'pages/snippet_detail.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect('home')


def logout_page(request):
    auth.logout(request)
    return redirect('home')


def registration(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        context = {'form': form,
                   'pagename': 'Регистрация'}
        return render(request, 'pages/registration.html', context)
    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form,
                       'pagename': 'Регистрация'}
            return render(request, 'pages/registration.html', context)
        return redirect('home')

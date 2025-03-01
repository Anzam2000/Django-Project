# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyForm


def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Здесь можно, например, сохранить данные в базу данных или отправить email
            print(f"Имя: {name}, Email: {email}, Сообщение: {message}")

            # Перенаправление на другую страницу после успешной обработки
            return HttpResponseRedirect('/thanks/')
    else:
        form = MyForm()

    return render(request, 'myapp/index.html', {'form': form})


def thanks(request):
    return render(request, 'myapp/thanks.html')
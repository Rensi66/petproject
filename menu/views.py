from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ContactForm

def welcome(request):
    return render(request, 'menu/welcome.html')

def about(request):
    return render(request, 'menu/about.html')

def menu(request, category=None):
    cat = Dishes_Category.objects.all()
    selected_category = category
    if selected_category:
        dishes = Dishes.objects.filter(category__type=selected_category)
    else:
        dishes = None

    return render(request, 'menu/menu.html', {'cat': cat, 'selected_category': selected_category, 'dishes': dishes})


def callback_view(request):
    success_message = None  # по умолчанию

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = 'Спасибо! Мы вам перезвоним.'
            form = ContactForm()  # очистить форму
    else:
        form = ContactForm()

    return render(request, 'menu/reservation.html', {
        'form': form,
        'success_message': success_message
    })



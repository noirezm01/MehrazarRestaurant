from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Food


def test(request):
    return HttpResponse('hello django')


def main(request):
    return render(request, 'welcome.html')


def food_list(request):
    f_list = Food.objects.all()
    context = {
        'foods': f_list
    }
    return render(request, 'foods/food_list.html', context)


def food_detail(request, id):
    food = Food.objects.get(id=id)
    context = {
        'food': food
    }
    return render(request, 'foods/detail.html', context)





def gallery(request):
    f_list = Food.objects.all()
    context = {
        'foods': f_list
    }
    return render(request, 'foods/gallery.html', context)

from django.http import Http404
from django.shortcuts import render

from main.models import Car
from main.models import Sale

def cars_list_view(request):
    # получите список авто
    cars = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, {'cars': cars})  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    try:
        car = Car.objects.get(id=car_id)
        template_name = 'main/details.html'
        return render(request, template_name, {'car': car})
    except Car.DoesNotExist:
        raise Http404('Нет такой машины')
    #template_name = 'main/details.html'
    #return render(request, template_name, {})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        # получите авто и его продажи
        car = Car.objects.get(id=car_id)
        sale = Sale.objects.get(id=car)
        template_name = 'main/sales.html'
        return render(request, template_name, {'sale': sale})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')

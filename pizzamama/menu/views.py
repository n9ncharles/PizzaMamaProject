from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


# Create your views here.
def index(request):
    # pizzas = Pizza.objects.all()
    # pizzas_list = [f"{pizza.name} : {pizza.price} €" for pizza in pizzas]
    # pizzas_list_str = ", ".join(pizzas_list)
    # return HttpResponse(f"Les menus : {pizzas_list_str}")
    pizzas = Pizza.objects.all().order_by("name")
    return render(request, 'menu/index.html', {
                                                                                "pizzas": pizzas
    })

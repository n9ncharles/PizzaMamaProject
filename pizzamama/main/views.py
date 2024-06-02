from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first_page(request):
    return render(request, 'firstpage/first_page.html')

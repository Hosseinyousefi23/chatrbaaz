from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def main_page(request):
    return HttpResponse(request, 'main_page.html', {})

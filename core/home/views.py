from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect , HttpResponseNotAllowed

# def home(request):
#     return render(request, 'home/index.html')

def main(request):
    return render(request, 'home/index.html')

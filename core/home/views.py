from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect , HttpResponseNotAllowed

# def home(request):
#     return render(request, 'home/index.html')

def abhi(request):
    return render(request, 'home/abhi.html')

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def error_404_view(request, exception):
    return render(request, 'home/404.html', status=404)


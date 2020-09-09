from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    "Home Page"
    return render(request, 'mini/index.html')
    